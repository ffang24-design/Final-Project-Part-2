"""
CSE 163 Final Project - Part 2 (EDA)
Person 1: data collection and cleaning.

Downloads ACS 2024 5-year tables B16004 and C16001 for King County, WA
(county and census-tract level) from the Census API, cleans them, and
writes tidy CSV files to data/clean/ for the rest of the analysis.

Raw API responses are saved to data/raw/ so the analysis can be rerun
without an API key. To download fresh data, put a Census API key in the
CENSUS_API_KEY environment variable or in the file ~/.census_api_key
(free key: https://api.census.gov/data/key_signup.html).

Run from the repository root:  python src/data_cleaning.py
"""

import json
import os

import numpy as np
import pandas as pd
import requests

API_BASE = 'https://api.census.gov/data/2024/acs/acs5'
STATE = '53'     # Washington
COUNTY = '033'   # King County
TABLES = ['B16004', 'C16001']
GEOGRAPHIES = ['county', 'tract']

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(ROOT, 'data', 'raw')
CLEAN_DIR = os.path.join(ROOT, 'data', 'clean')
SITE_FILE = os.path.join(RAW_DIR, 'sound_generations_sites.csv')

OLDER_ADULTS = '65 years and over'
NEED_LEVELS = ['well', 'not well', 'not at all']
LESS_THAN_VERY_WELL = 'less than very well'

# C16001 detailed language -> B16004 broad language group (ACS 4-group
# classification). Used for research question 3.
DETAILED_TO_BROAD = {
    'Spanish': 'Spanish',
    'French, Haitian, or Cajun': 'Other Indo-European languages',
    'German or other West Germanic languages':
        'Other Indo-European languages',
    'Russian, Polish, or other Slavic languages':
        'Other Indo-European languages',
    'Other Indo-European languages': 'Other Indo-European languages',
    'Korean': 'Asian and Pacific Island languages',
    'Chinese (incl. Mandarin, Cantonese)':
        'Asian and Pacific Island languages',
    'Vietnamese': 'Asian and Pacific Island languages',
    'Tagalog (incl. Filipino)': 'Asian and Pacific Island languages',
    'Other Asian and Pacific Island languages':
        'Asian and Pacific Island languages',
    'Arabic': 'Other languages',
    'Other and unspecified languages': 'Other languages',
}

# Census API uses large negative numbers as codes for "not available".
# Any value at or below this threshold is treated as missing.
SENTINEL_THRESHOLD = -111111111


# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------

def read_api_key():
    """
    Returns the Census API key from the CENSUS_API_KEY environment variable
    or ~/.census_api_key, or None if neither exists.
    """
    key = os.environ.get('CENSUS_API_KEY')
    if key:
        return key.strip()
    path = os.path.expanduser('~/.census_api_key')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return None


def geography_params(geography):
    """
    Returns the Census API 'for'/'in' parameters for King County
    ('county') or all King County census tracts ('tract').
    """
    if geography == 'county':
        return {'for': 'county:' + COUNTY, 'in': 'state:' + STATE}
    if geography == 'tract':
        return {'for': 'tract:*',
                'in': 'state:' + STATE + ' county:' + COUNTY}
    raise ValueError('Unknown geography: ' + geography)


def download_metadata(table):
    """
    Downloads the variable metadata (code -> label) for an ACS table and
    saves it as data/raw/<table>_variables.json. Returns the file path.
    """
    path = os.path.join(RAW_DIR, table + '_variables.json')
    url = API_BASE + '/groups/' + table + '.json'
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    variables = response.json()['variables']
    labels = {code: info['label'] for code, info in variables.items()}
    with open(path, 'w') as f:
        json.dump(labels, f, indent=1, sort_keys=True)
    return path


def download_table(table, geography, key):
    """
    Downloads all variables of an ACS table for the given geography and
    saves the response as data/raw/<table>_<geography>.csv with every
    value kept as text. Returns the file path.
    """
    path = os.path.join(RAW_DIR, table + '_' + geography + '.csv')
    params = {'get': 'group(' + table + ')', 'key': key}
    params.update(geography_params(geography))
    response = requests.get(API_BASE, params=params, timeout=120)
    if 'missing_key' in response.url or 'invalid_key' in response.url:
        raise RuntimeError('Census API rejected the API key.')
    response.raise_for_status()
    rows = response.json()
    raw = pd.DataFrame(rows[1:], columns=rows[0])
    raw.to_csv(path, index=False)
    return path


def download_all():
    """
    Downloads metadata and county/tract data for every table into
    data/raw/, skipping files that already exist.
    """
    os.makedirs(RAW_DIR, exist_ok=True)
    key = read_api_key()
    for table in TABLES:
        meta_path = os.path.join(RAW_DIR, table + '_variables.json')
        if not os.path.exists(meta_path):
            print('Downloading metadata for', table)
            download_metadata(table)
        for geography in GEOGRAPHIES:
            path = os.path.join(RAW_DIR, table + '_' + geography + '.csv')
            if os.path.exists(path):
                continue
            if key is None:
                raise RuntimeError('No Census API key found; see the '
                                   'module docstring.')
            print('Downloading', table, geography)
            download_table(table, geography, key)


# ---------------------------------------------------------------------------
# Cleaning
# ---------------------------------------------------------------------------

def load_labels(table):
    """
    Returns the saved variable metadata for a table as a dict mapping
    variable codes (e.g. 'B16004_046E') to labels.
    """
    with open(os.path.join(RAW_DIR, table + '_variables.json')) as f:
        return json.load(f)


def make_geoid(df):
    """
    Returns a Series of GEOID strings built from the state, county and
    (if present) tract columns, keeping leading zeros: 5 digits for a
    county and 11 digits for a tract.
    """
    geoid = (df['state'].astype(str).str.zfill(2)
             + df['county'].astype(str).str.zfill(3))
    if 'tract' in df.columns:
        geoid = geoid + df['tract'].astype(str).str.zfill(6)
    return geoid


def clean_values(series):
    """
    Converts a Series of API values to numbers. Text that is not a number
    and Census "not available" codes (large negative numbers) become NaN,
    never zero.
    """
    numbers = pd.to_numeric(series, errors='coerce')
    return numbers.mask(numbers <= SENTINEL_THRESHOLD, np.nan)


def clean_table(raw, table):
    """
    Takes a raw API DataFrame for one table and returns a wide DataFrame
    with GEOID, NAME, and one numeric column per estimate (…E) and margin
    of error (…M). Annotation columns (…EA, …MA) are dropped.
    """
    value_cols = [c for c in raw.columns
                  if c.startswith(table + '_') and c[-1] in ('E', 'M')
                  and not c.endswith(('EA', 'MA'))]
    ids = pd.DataFrame({'GEOID': make_geoid(raw), 'NAME': raw['NAME']})
    values = raw[value_cols].apply(clean_values)
    return pd.concat([ids, values], axis=1)


def parse_label(label, table):
    """
    Splits an ACS label into its parts. For B16004 returns
    (age_group, language, english_ability); for C16001 returns
    (language, english_ability). Missing levels are 'Total'.

    Example: 'Estimate!!Total:!!65 years and over:!!Speak Spanish:!!'
    'Speak English "well"' -> ('65 years and over', 'Spanish', 'well')
    """
    parts = [p.rstrip(':') for p in label.split('!!')[2:]]
    cleaned = []
    for part in parts:
        if part.startswith('Speak English '):
            part = part[len('Speak English '):].replace('"', '')
        elif part == 'Speak only English':
            part = 'Only English'
        elif part.startswith('Speak '):
            part = part[len('Speak '):]
            part = part[0].upper() + part[1:]
        cleaned.append(part)
    size = 3 if table == 'B16004' else 2
    cleaned = cleaned + ['Total'] * (size - len(cleaned))
    return tuple(cleaned)


def tidy_table(wide, table, labels):
    """
    Reshapes a cleaned wide table into a long (tidy) DataFrame with one row
    per geography and variable: GEOID, NAME, variable, the label parts from
    parse_label, estimate, and moe.
    """
    est_cols = [c for c in wide.columns if c.endswith('E')
                and c.startswith(table + '_')]
    est = wide.melt(id_vars=['GEOID', 'NAME'], value_vars=est_cols,
                    var_name='variable', value_name='estimate')
    moe_cols = [c[:-1] + 'M' for c in est_cols]
    moe = wide.melt(id_vars=['GEOID'], value_vars=moe_cols,
                    var_name='variable', value_name='moe')
    moe['variable'] = moe['variable'].str[:-1] + 'E'
    tidy = est.merge(moe, on=['GEOID', 'variable'], how='left')
    if table == 'B16004':
        names = ['age_group', 'language', 'english_ability']
    else:
        names = ['language', 'english_ability']
    parts = tidy['variable'].map(lambda v: parse_label(labels[v], table))
    for i, name in enumerate(names):
        tidy[name] = parts.str[i]
    return tidy[['GEOID', 'NAME', 'variable'] + names
                + ['estimate', 'moe']]


def percent(numerator, denominator):
    """
    Returns numerator / denominator * 100, with NaN wherever the
    denominator is zero or missing.
    """
    denominator = denominator.where(denominator > 0)
    return numerator / denominator * 100


def combined_moe(moes):
    """
    Returns the approximate margin of error of a sum of ACS estimates:
    the square root of the sum of squared MOEs (Census ACS handbook).
    """
    return np.sqrt((moes ** 2).sum(min_count=1))


def coefficient_of_variation(estimate, moe):
    """
    Returns the coefficient of variation (%) of ACS estimates: the
    standard error (MOE / 1.645 for 90% MOEs) divided by the estimate.
    NaN where the estimate is zero or missing. Above 30% is commonly
    treated as unreliable.
    """
    return (moe / 1.645) / estimate.where(estimate > 0) * 100


def older_adult_need(b16004_tidy):
    """
    From tidy B16004 data, returns one row per geography and non-English
    language group for adults 65+, with the group total, the number who
    speak English less than "very well" (well + not well + not at all),
    its margin of error, and the within-group percentage.
    """
    older = b16004_tidy[
        (b16004_tidy['age_group'] == OLDER_ADULTS)
        & (~b16004_tidy['language'].isin(['Total', 'Only English']))]
    keys = ['GEOID', 'NAME', 'language']
    total = (older[older['english_ability'] == 'Total']
             .set_index(keys)['estimate'].rename('total_65plus'))
    need_rows = older[older['english_ability'].isin(NEED_LEVELS)]
    grouped = need_rows.groupby(keys)
    need = grouped['estimate'].sum(min_count=1).rename('need_65plus')
    need_moe = grouped['moe'].apply(combined_moe).rename('need_moe')
    result = pd.concat([total, need, need_moe], axis=1).reset_index()
    result['need_pct'] = percent(result['need_65plus'],
                                 result['total_65plus'])
    result['need_cv'] = coefficient_of_variation(result['need_65plus'],
                                                 result['need_moe'])
    return result


def detailed_need(c16001_tidy):
    """
    From tidy C16001 data (ages 5+), returns one row per geography and
    detailed language with the language total, the number who speak
    English less than "very well", its MOE, the within-language
    percentage, and the matching B16004 broad group.
    """
    langs = c16001_tidy[~c16001_tidy['language'].isin(['Total',
                                                       'Only English'])]
    keys = ['GEOID', 'NAME', 'language']
    total = (langs[langs['english_ability'] == 'Total']
             .set_index(keys)['estimate'].rename('total_5plus'))
    need_rows = (langs[langs['english_ability'] == LESS_THAN_VERY_WELL]
                 .set_index(keys))
    result = pd.concat([total,
                        need_rows['estimate'].rename('need_5plus'),
                        need_rows['moe'].rename('need_moe')],
                       axis=1).reset_index()
    result['need_pct'] = percent(result['need_5plus'],
                                 result['total_5plus'])
    result['need_cv'] = coefficient_of_variation(result['need_5plus'],
                                                 result['need_moe'])
    result['broad_group'] = result['language'].map(DETAILED_TO_BROAD)
    return result


# ---------------------------------------------------------------------------
# Sound Generations site list
# ---------------------------------------------------------------------------

def clean_site_list(sites, site_col='site', language_col='languages',
                    language_map=None):
    """
    Takes a DataFrame with one row per site and a column listing the
    languages offered (separated by commas, semicolons, '/' or ' and ').
    Returns one row per unique site-language pair with a standardized
    language name. Sites with no listed language get 'Unknown'.
    language_map maps lower-case raw names to standard names; unmapped
    names are kept in title case.
    """
    if language_map is None:
        language_map = {}
    df = sites.copy()
    df[site_col] = df[site_col].astype(str).str.strip()
    langs = (df[language_col].fillna('').astype(str)
             .str.split(r'\s*(?:,|;|/|\band\b)\s*', regex=True))
    df = df.assign(language_raw=langs).explode('language_raw')
    df['language_raw'] = df['language_raw'].str.strip()
    df.loc[df['language_raw'] == '', 'language_raw'] = np.nan
    lower = df['language_raw'].str.lower()
    df['language'] = lower.map(language_map).fillna(
        df['language_raw'].str.title())
    df['language'] = df['language'].fillna('Unknown')
    df = df.drop(columns=[language_col])
    return df.drop_duplicates(subset=[site_col, 'language']).reset_index(
        drop=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    download_all()
    os.makedirs(CLEAN_DIR, exist_ok=True)
    for table in TABLES:
        labels = load_labels(table)
        for geography in GEOGRAPHIES:
            raw = pd.read_csv(
                os.path.join(RAW_DIR, table + '_' + geography + '.csv'),
                dtype=str)
            tidy = tidy_table(clean_table(raw, table), table, labels)
            name = table.lower() + '_' + geography
            tidy.to_csv(os.path.join(CLEAN_DIR, name + '_tidy.csv'),
                        index=False)
            if table == 'B16004':
                need = older_adult_need(tidy)
                need.to_csv(os.path.join(CLEAN_DIR, name + '_need65.csv'),
                            index=False)
            else:
                need = detailed_need(tidy)
                need.to_csv(os.path.join(CLEAN_DIR, name + '_need.csv'),
                            index=False)
            print('Wrote', name, 'tidy', tidy.shape, 'need', need.shape)

    if os.path.exists(SITE_FILE):
        sites = clean_site_list(pd.read_csv(SITE_FILE))
        sites.to_csv(os.path.join(CLEAN_DIR, 'sites_languages.csv'),
                     index=False)
        print('Wrote sites_languages', sites.shape)
    else:
        print('Site list not found at', SITE_FILE, '- skipped.')


if __name__ == '__main__':
    main()
