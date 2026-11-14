"""
CSE 163 Final Project - Part 2 (EDA)
Person 1: dataset structure, missingness, and descriptive statistics.

Reads the files written by data_cleaning.py and, for each dataset and each
dataset combination, reports size, missing data, seven-number summaries of
quantitative variables, and counts of categorical variables. Tables are
saved to results/tables/ and a readable summary to results/eda_summary.md,
which is the source for the Dataset and EDA Results sections of eda.pdf.

Run from the repository root:
    python src/data_cleaning.py
    python src/eda_stats.py
"""

import os

import pandas as pd

import data_cleaning as dc

RESULTS_DIR = os.path.join(dc.ROOT, 'results')
TABLE_DIR = os.path.join(RESULTS_DIR, 'tables')
TRACT_SHAPEFILE = os.path.join(dc.RAW_DIR, 'tl_2020_53_tract',
                               'tl_2020_53_tract.shp')


# ---------------------------------------------------------------------------
# Generic summaries
# ---------------------------------------------------------------------------

def missing_summary(df):
    """
    Returns a DataFrame with the number and percentage of missing values
    in each column of df, keeping only columns with at least one missing
    value.
    """
    counts = df.isna().sum()
    result = pd.DataFrame({'n_missing': counts,
                           'pct_missing': counts / len(df) * 100})
    return result[result['n_missing'] > 0]


def seven_number_summary(df, columns, by=None):
    """
    Returns the seven-number summary (mean, std, min, 25%, 50%, 75%, max)
    and count of the given numeric columns, optionally for each group of
    the column `by`.
    """
    stats = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    if by is None:
        return df[columns].describe().loc[stats].T
    result = df.groupby(by)[columns].describe()
    result = result.stack(level=0, future_stack=True)[stats]
    return result


def reliability_summary(need, estimate_col, by='language'):
    """
    For each group, returns the number of rows, how many have a zero or
    missing estimate, and how many nonzero estimates have a coefficient
    of variation above 30% (commonly treated as unreliable).
    """
    df = need.assign(
        zero_or_missing=~(need[estimate_col] > 0),
        cv_over_30=need['need_cv'] > 30)
    result = df.groupby(by).agg(rows=(estimate_col, 'size'),
                                zero_or_missing=('zero_or_missing', 'sum'),
                                cv_over_30=('cv_over_30', 'sum'),
                                median_cv=('need_cv', 'median'))
    result['pct_nonzero_unreliable'] = (
        result['cv_over_30']
        / (result['rows'] - result['zero_or_missing']).where(
            lambda x: x > 0) * 100)
    return result


def category_counts(df, column):
    """
    Returns every unique value of a categorical column with its count
    (missing values included).
    """
    return df[column].value_counts(dropna=False).rename_axis(
        column).reset_index(name='count')


# ---------------------------------------------------------------------------
# Dataset combinations
# ---------------------------------------------------------------------------

def broad_vs_detailed(b16004_need, c16001_need):
    """
    Combines county-level B16004 (65+, broad groups) with C16001
    (5+, detailed languages) on the broad language group. Each row is one
    detailed language with its 5+ need, its share of its broad group's
    5+ need, and the 65+ need of its broad group. C16001 is not subtracted
    from B16004 because the two cover different age ranges.
    """
    detailed = c16001_need[['language', 'broad_group', 'total_5plus',
                            'need_5plus', 'need_pct']].copy()
    detailed['share_of_group_need_pct'] = (
        detailed['need_5plus']
        / detailed.groupby('broad_group')['need_5plus'].transform('sum')
        * 100)
    broad = b16004_need[['language', 'total_65plus', 'need_65plus',
                         'need_pct']].rename(columns={
                             'language': 'broad_group',
                             'need_pct': 'group_need_pct_65plus'})
    merged = detailed.merge(broad, on='broad_group', how='left',
                            validate='many_to_one')
    return merged.sort_values(['broad_group', 'need_5plus'],
                              ascending=[True, False])


def tract_boundary_check(tract_need, shapefile):
    """
    Merges tract-level 65+ need with the 2020 TIGER tract polygons for
    King County on the 11-digit GEOID and returns a dict describing the
    merge (sizes, key uniqueness, unmatched GEOIDs) plus the merged
    GeoDataFrame.
    """
    import geopandas as gpd
    tracts = gpd.read_file(shapefile)
    tracts = tracts[tracts['COUNTYFP'] == dc.COUNTY]
    acs_ids = pd.Series(tract_need['GEOID'].unique())
    merged = tracts.merge(tract_need, on='GEOID', how='inner')
    info = {
        'boundary_rows': len(tracts),
        'boundary_columns': tracts.shape[1],
        'boundary_geoid_unique': tracts['GEOID'].is_unique,
        'acs_tracts': len(acs_ids),
        'acs_not_in_boundaries': sorted(set(acs_ids) - set(tracts['GEOID'])),
        'boundaries_not_in_acs': sorted(set(tracts['GEOID']) - set(acs_ids)),
        'merged_rows': len(merged),
    }
    return info, merged


def sites_vs_need(sites, b16004_need, c16001_need):
    """
    Counts distinct sites per standardized language and left-merges the
    counts onto the detailed (C16001) language needs so every population
    group is kept; groups with no documented site get 0.
    """
    counts = (sites.groupby('language')['site'].nunique()
              .rename('n_sites').reset_index())
    merged = c16001_need.merge(counts, on='language', how='left')
    merged['n_sites'] = merged['n_sites'].fillna(0).astype(int)
    return merged


# ---------------------------------------------------------------------------
# Report writing
# ---------------------------------------------------------------------------

class Report:
    """Collects markdown text and saves tables for the EDA summary."""

    def __init__(self):
        self._lines = []

    def heading(self, text, level=2):
        self._lines.append('\n' + '#' * level + ' ' + text + '\n')

    def text(self, text):
        self._lines.append(text + '\n')

    def table(self, df, name, title=None, index=True):
        """Adds df to the report and saves it as results/tables/<name>.csv."""
        df.to_csv(os.path.join(TABLE_DIR, name + '.csv'), index=index)
        if title:
            self._lines.append('**' + title + '** (`results/tables/' + name
                               + '.csv`)\n')
        body = df.to_string(index=index, float_format=lambda x:
                            '{:,.2f}'.format(x))
        self._lines.append('```\n' + body + '\n```\n')

    def save(self, path):
        with open(path, 'w') as f:
            f.write('\n'.join(self._lines))


def describe_shape(report, name, df, row_meaning):
    report.text('- **' + name + '**: ' + '{:,}'.format(df.shape[0])
                + ' rows x ' + str(df.shape[1]) + ' columns. ' + row_meaning)


def describe_missing(report, df, name, title):
    missing = missing_summary(df)
    if len(missing) == 0:
        report.text('`' + title + '`: `df.isna().sum().sum()` = 0, '
                    'no missing values.')
    else:
        report.table(missing, name, title)


def read_clean(name):
    return pd.read_csv(os.path.join(dc.CLEAN_DIR, name + '.csv'),
                       dtype={'GEOID': str})


def read_raw_wide(table, geography):
    raw = pd.read_csv(os.path.join(dc.RAW_DIR, table + '_' + geography
                                   + '.csv'), dtype=str)
    return raw, dc.clean_table(raw, table)


def acs_section(report, table, need_name, need_cols, by_age):
    """Writes the EDA section for one ACS table (county and tract)."""
    raw_c, wide_c = read_raw_wide(table, 'county')
    raw_t, wide_t = read_raw_wide(table, 'tract')
    tidy_t = read_clean(table.lower() + '_tract_tidy')
    need_c = read_clean(table.lower() + '_county_' + need_name)
    need_t = read_clean(table.lower() + '_tract_' + need_name)
    n_est = sum(1 for c in wide_t.columns if c.endswith('E')
                and c.startswith(table))
    prefix = table.lower()

    report.heading(table, 2)
    report.heading('Size', 3)
    describe_shape(report, 'Raw API response, tract', raw_t,
                   'Each row is one King County census tract; columns are '
                   'GEO_ID, NAME, state, county, tract and, for each of the '
                   + str(n_est) + ' variables, an estimate (E), margin of '
                   'error (M) and two annotation columns (EA, MA).')
    describe_shape(report, 'Raw API response, county', raw_c,
                   'One row for King County as a whole.')
    describe_shape(report, 'Cleaned wide table, tract', wide_t,
                   'GEOID, NAME, and numeric E and M columns '
                   '(annotations dropped).')
    describe_shape(report, 'Tidy table, tract', tidy_t,
                   'One row per tract x variable with parsed label parts.')
    describe_shape(report, 'Need table, tract', need_t,
                   'One row per tract x non-English language group.')
    describe_shape(report, 'Need table, county', need_c,
                   'One row per non-English language group.')
    report.text('Unique tract GEOIDs: '
                + str(wide_t['GEOID'].nunique()) + ' (all 11 digits: '
                + str((wide_t['GEOID'].str.len() == 11).all()) + ').')

    report.heading('Missing data', 3)
    describe_missing(report, wide_t, prefix + '_tract_missing',
                     table + ' tract cleaned wide table')
    describe_missing(report, wide_c, prefix + '_county_missing',
                     table + ' county cleaned wide table')
    describe_missing(report, need_t, prefix + '_tract_need_missing',
                     table + ' tract need table')
    zero_tracts = wide_t.loc[wide_t[table + '_001E'] == 0, 'GEOID']
    report.text('Tracts with a population of 0 in this table: '
                + str(len(zero_tracts)) + ' ' + str(list(zero_tracts))
                + '. Percentages with a zero denominator are left as NaN.')

    report.heading('Categorical variables', 3)
    cats = ['language', 'english_ability']
    if by_age:
        cats = ['age_group'] + cats
    one_tract = tidy_t[tidy_t['GEOID'] == tidy_t['GEOID'].iloc[0]]
    for col in cats:
        report.table(category_counts(one_tract, col),
                     prefix + '_counts_' + col,
                     'Values of `' + col + '` (rows per tract)',
                     index=False)

    report.heading('Quantitative variables', 3)
    report.table(need_c.drop(columns=['GEOID', 'NAME']).set_index(
        'language'), prefix + '_county_need', 'King County totals')
    report.table(seven_number_summary(need_t, need_cols, by='language'),
                 prefix + '_tract_seven_number',
                 'Seven-number summary across tracts, by language')

    report.heading('Reliability of tract estimates (margins of error)', 3)
    est_col = need_cols[1]
    report.table(reliability_summary(need_t, est_col),
                 prefix + '_tract_reliability',
                 'Coefficient of variation of `' + est_col + '` by language')
    return need_c, need_t


def main():
    os.makedirs(TABLE_DIR, exist_ok=True)
    report = Report()
    report.heading('EDA summary (generated by eda_stats.py)', 1)

    b_need_c, b_need_t = acs_section(
        report, 'B16004', 'need65',
        ['total_65plus', 'need_65plus', 'need_pct'], by_age=True)
    c_need_c, c_need_t = acs_section(
        report, 'C16001', 'need',
        ['total_5plus', 'need_5plus', 'need_pct'], by_age=False)

    report.heading('Combination: B16004 x C16001 (county)', 2)
    combo = broad_vs_detailed(b_need_c, c_need_c)
    report.text('- ' + str(combo.shape[0]) + ' rows x '
                + str(combo.shape[1]) + ' columns; one row per C16001 '
                'detailed language, joined to its B16004 broad group.')
    unmatched = combo['broad_group'].isna().sum()
    report.text('- Detailed languages without a broad group: '
                + str(unmatched))
    describe_missing(report, combo, 'combo_b_c_missing',
                     'B16004 x C16001 combined table')
    report.table(combo.set_index('language'), 'combo_broad_vs_detailed',
                 'Detailed languages within broad groups')
    report.table(seven_number_summary(
        combo, ['need_5plus', 'need_pct', 'share_of_group_need_pct']),
        'combo_seven_number', 'Seven-number summary')
    report.table(category_counts(combo, 'broad_group'),
                 'combo_counts_broad_group',
                 'Detailed languages per broad group', index=False)

    report.heading('Combination: B16004 tracts x 2020 tract boundaries', 2)
    if os.path.exists(TRACT_SHAPEFILE):
        info, merged = tract_boundary_check(b_need_t, TRACT_SHAPEFILE)
        for key, value in info.items():
            report.text('- ' + key + ': ' + str(value))
        describe_missing(report, pd.DataFrame(merged.drop(
            columns='geometry')), 'combo_tract_geo_missing',
            'Merged tract table')
    else:
        report.text('Shapefile not found at `' + TRACT_SHAPEFILE
                    + '`; skipped.')

    report.heading('Sound Generations site list', 2)
    site_path = os.path.join(dc.CLEAN_DIR, 'sites_languages.csv')
    if os.path.exists(site_path):
        sites = pd.read_csv(site_path)
        describe_shape(report, 'Site-language table', sites,
                       'One row per site x language offered.')
        describe_missing(report, sites, 'sites_missing', 'Site table')
        report.table(category_counts(sites, 'language'),
                     'sites_counts_language', 'Sites per language',
                     index=False)
        report.table(sites_vs_need(sites, b_need_c, c_need_c),
                     'combo_sites_vs_need', 'Site counts vs. need',
                     index=False)
    else:
        report.text('Site list not found; skipped.')

    report.save(os.path.join(RESULTS_DIR, 'eda_summary.md'))
    print('Wrote', os.path.join(RESULTS_DIR, 'eda_summary.md'))


if __name__ == '__main__':
    main()
