"""
Tests for the EDA statistical analysis functions.
"""

import math
import numpy as np
import pandas as pd
import eda_stats as es


def test_missing_summary():
    """
    Tests whether missing_summary correctly counts missing values,
    calculates missing percentages, and excludes columns without
    missing values.
    """
    df = pd.DataFrame({
        'a': [1, np.nan, 3, np.nan],
        'b': [1, 2, 3, 4],
    })

    result = es.missing_summary(df)

    assert result.loc['a', 'n_missing'] == 2
    assert result.loc['a', 'pct_missing'] == 50
    assert 'b' not in result.index


def test_seven_number_summary():
    """
    Tests whether seven_number_summary correctly calculates
    descriptive statistics, including the mean, minimum,
    quartiles, maximum, and sample standard deviation.
    """
    df = pd.DataFrame({
        'value': [1, 2, 3, 4, 5]
    })

    result = es.seven_number_summary(df, ['value'])

    assert result.loc['value', 'mean'] == 3
    assert result.loc['value', 'min'] == 1
    assert result.loc['value', '25%'] == 2
    assert result.loc['value', '50%'] == 3
    assert result.loc['value', '75%'] == 4
    assert result.loc['value', 'max'] == 5
    assert math.isclose(result.loc['value', 'std'], math.sqrt(2.5))


def test_category_counts():
    """
    Tests whether category_counts correctly counts the occurrences
    of each category, including missing values, and returns the
    expected frequency for each language.
    """
    df = pd.DataFrame({
        'language': ['Spanish', 'Chinese', 'Spanish', None]
    })

    result = es.category_counts(df, 'language')

    assert result['count'].sum() == 4
    counts = dict(zip(result['language'], result['count']))
    assert counts['Spanish'] == 2
    assert counts['Chinese'] == 1
    assert result['language'].isna().sum() == 1


def test_broad_vs_detailed():
    """
    Tests whether broad_vs_detailed correctly combines broad
    language-group data with detailed language data, calculates
    each language's share of its group's total need, and preserves
    the corresponding older-adult need count.
    """
    broad = pd.DataFrame({
        'language': ['Asian and Pacific Island Languages'],
        'total_65plus': [100],
        'need_65plus': [60],
        'need_pct': [60.0],
    })

    detailed = pd.DataFrame({
        'language': ['Chinese', 'Korean'],
        'broad_group': ['Asian and Pacific Island Languages'] * 2,
        'total_5plus': [200, 100],
        'need_5plus': [80, 20],
        'need_pct': [40.0, 20.0],
    })

    result = es.broad_vs_detailed(broad, detailed)
    result = result.set_index('language')

    assert result.loc['Chinese', 'share_of_group_need_pct'] == 80
    assert result.loc['Korean', 'share_of_group_need_pct'] == 20
    assert result.loc['Chinese', 'need_65plus'] == 60
    assert len(result) == 2


def test_sites_vs_need():
    """
    Tests whether sites_vs_need correctly counts service sites
    for each language and includes languages with no sites,
    assigning those languages a site count of zero.
    """
    sites = pd.DataFrame({
        'site': ['A', 'B', 'C'],
        'language': ['Chinese', 'Chinese', 'Spanish'],
    })

    broad = pd.DataFrame()
    detailed = pd.DataFrame({
        'language': ['Chinese', 'Spanish', 'Korean'],
        'need_5plus': [100, 50, 30],
    })

    result = es.sites_vs_need(sites, broad, detailed)
    result = result.set_index('language')

    assert result.loc['Chinese', 'n_sites'] == 2
    assert result.loc['Spanish', 'n_sites'] == 1
    assert result.loc['Korean', 'n_sites'] == 0
    assert len(result) == 3


def main():
    test_missing_summary()
    test_seven_number_summary()
    test_category_counts()
    test_broad_vs_detailed()
    test_sites_vs_need()
    print("All EDA statistics tests passed.")


if __name__ == '__main__':
    main()
