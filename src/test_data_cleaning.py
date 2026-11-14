"""
CSE 163 Final Project - Part 2 (EDA)
Tests for data_cleaning.py on small hand-made inputs whose answers can be
checked by hand. No network access or downloaded data is needed.

Run from the repository root:  python src/test_data_cleaning.py
"""

import math

import numpy as np
import pandas as pd

import data_cleaning as dc

B_LABELS = {
    'B16004_046E': 'Estimate!!Total:!!65 years and over:',
    'B16004_058E': 'Estimate!!Total:!!65 years and over:!!'
                   'Speak Asian and Pacific Island languages:',
    'B16004_059E': 'Estimate!!Total:!!65 years and over:!!'
                   'Speak Asian and Pacific Island languages:!!'
                   'Speak English "very well"',
    'B16004_060E': 'Estimate!!Total:!!65 years and over:!!'
                   'Speak Asian and Pacific Island languages:!!'
                   'Speak English "well"',
    'B16004_061E': 'Estimate!!Total:!!65 years and over:!!'
                   'Speak Asian and Pacific Island languages:!!'
                   'Speak English "not well"',
    'B16004_062E': 'Estimate!!Total:!!65 years and over:!!'
                   'Speak Asian and Pacific Island languages:!!'
                   'Speak English "not at all"',
}


def make_raw_b16004():
    """
    Two fake tracts. Tract 000100: 100 older API-language speakers, of whom
    10 + 20 + 30 = 60 speak English less than very well. Tract 000200 has
    no older API-language speakers.
    """
    raw = pd.DataFrame({
        'GEO_ID': ['x', 'y'], 'NAME': ['Tract 1', 'Tract 2'],
        'state': ['53', '53'], 'county': ['033', '033'],
        'tract': ['000100', '000200'],
    })
    values = {'046': (500, 0), '058': (100, 0), '059': (40, 0),
              '060': (10, 0), '061': (20, 0), '062': (30, 0)}
    for code, (first, second) in values.items():
        raw['B16004_' + code + 'E'] = [str(first), str(second)]
        raw['B16004_' + code + 'M'] = ['3', '-555555555']
        raw['B16004_' + code + 'EA'] = [None, None]
    return raw


def test_make_geoid():
    raw = make_raw_b16004()
    geoid = dc.make_geoid(raw)
    assert list(geoid) == ['53033000100', '53033000200']
    assert (geoid.str.len() == 11).all()
    county = raw.drop(columns='tract')
    assert dc.make_geoid(county).iloc[0] == '53033'


def test_clean_values():
    result = dc.clean_values(pd.Series(['12', '-666666666', 'N', '0']))
    assert result.iloc[0] == 12
    assert math.isnan(result.iloc[1])
    assert math.isnan(result.iloc[2])
    assert result.iloc[3] == 0


def test_clean_table():
    wide = dc.clean_table(make_raw_b16004(), 'B16004')
    assert 'B16004_046EA' not in wide.columns
    assert wide.shape == (2, 2 + 12)
    assert math.isnan(wide.loc[1, 'B16004_046M'])


def test_parse_label():
    assert dc.parse_label(B_LABELS['B16004_061E'], 'B16004') == (
        '65 years and over', 'Asian and Pacific Island languages',
        'not well')
    assert dc.parse_label(B_LABELS['B16004_046E'], 'B16004') == (
        '65 years and over', 'Total', 'Total')
    assert dc.parse_label(
        'Estimate!!Total:!!Korean:!!Speak English less than "very well"',
        'C16001') == ('Korean', 'less than very well')


def test_older_adult_need():
    wide = dc.clean_table(make_raw_b16004(), 'B16004')
    tidy = dc.tidy_table(wide, 'B16004', B_LABELS)
    need = dc.older_adult_need(tidy).set_index('GEOID')
    assert len(need) == 2
    assert need.loc['53033000100', 'total_65plus'] == 100
    assert need.loc['53033000100', 'need_65plus'] == 60
    assert need.loc['53033000100', 'need_pct'] == 60
    assert math.isclose(need.loc['53033000100', 'need_moe'],
                        math.sqrt(27))
    # zero denominator -> missing percentage, not 0 or an error
    assert need.loc['53033000200', 'need_65plus'] == 0
    assert math.isnan(need.loc['53033000200', 'need_pct'])


def test_percent_and_cv():
    result = dc.percent(pd.Series([1, 5, 2]), pd.Series([4, 0, np.nan]))
    assert result.iloc[0] == 25
    assert math.isnan(result.iloc[1]) and math.isnan(result.iloc[2])
    cv = dc.coefficient_of_variation(pd.Series([100.0, 0.0]),
                                     pd.Series([16.45, 5.0]))
    assert math.isclose(cv.iloc[0], 10)
    assert math.isnan(cv.iloc[1])


def test_detailed_to_broad_covers_c16001():
    assert len(dc.DETAILED_TO_BROAD) == 12
    assert set(dc.DETAILED_TO_BROAD.values()) == {
        'Spanish', 'Other Indo-European languages',
        'Asian and Pacific Island languages', 'Other languages'}


def test_clean_site_list():
    sites = pd.DataFrame({
        'site': ['A', 'B ', 'C'],
        'languages': ['Chinese, Vietnamese; chinese', 'Spanish and Korean',
                      None],
    })
    clean = dc.clean_site_list(sites, language_map={'chinese': 'Chinese'})
    pairs = set(zip(clean['site'], clean['language']))
    assert pairs == {('A', 'Chinese'), ('A', 'Vietnamese'),
                     ('B', 'Spanish'), ('B', 'Korean'), ('C', 'Unknown')}
    assert not clean.duplicated(['site', 'language']).any()


def main():
    test_make_geoid()
    test_clean_values()
    test_clean_table()
    test_parse_label()
    test_older_adult_need()
    test_percent_and_cv()
    test_detailed_to_broad_covers_c16001()
    test_clean_site_list()
    print('All data_cleaning tests passed.')


if __name__ == '__main__':
    main()
