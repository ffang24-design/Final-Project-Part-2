import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

b16004_county = pd.read_csv('b16004_county_need65.csv')
b16004_tract = pd.read_csv('b16004_tract_need65.csv')
c16001_county = pd.read_csv('c16001_county_need.csv')
c16001_tract = pd.read_csv('c16001_tract_need.csv')
tracts = gpd.read_file('tl_2020_53033_tract20.shp')

b16004_county = b16004_county.sort_values(
                'need_65plus',ascending=False)
sns.catplot(x='language', y='need_65plus', kind='bar', 
            color='blue', data=b16004_county)
plt.title('Older Adults By Language that Need English Assistance')
plt.xlabel('Language Group')
plt.ylabel('Number of Older Adults')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('plot1_older_adult_need_count.png')
plt.show()

b16004_county = b16004_county.sort_values(
                'need_pct', ascending=False)
sns.catplot(x='language', y='need_pct', kind='bar',
            color='orange', data=b16004_county)
plt.title('Percentage of Older Adults That Need English Assistance')
plt.xlabel('Language Group')
plt.ylabel('Percentage That Need Asistance')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('plot2_older_adult_need_percentage.png')
plt.show()

tracts['GEOID'] = tracts['GEOID20'].astype(str)
b16004_tract['GEOID'] = b16004_tract['GEOID'].astype(str)
tracts = tracts[
    tracts['GEOID'].str.startswith('53033')
]
map_data = tracts.merge(
    b16004_tract,
    on='GEOID',
    how='inner'
)
languages = [
    'Spanish',
    'Other Indo-European languages',
    'Asian and Pacific Island languages',
    'Other languages'
]
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))
for language, ax in zip(languages, axs.flatten()):
    language_data = map_data[
        map_data['language'] == language]
    language_data.plot(
        column='need_65plus',
        cmap='OrRd',
        legend=True,
        ax=ax,
        edgecolor='white')
    ax.set_title(language)
    ax.set_axis_off()
plt.suptitle('Geographic Distribution of Older Adults That Need English Assistance')
plt.tight_layout()
plt.savefig('plot3_geographic_language_needs.png')
plt.show()

c16001_county = c16001_county.sort_values(
                'need_pct', ascending=False)
sns.catplot(
    x='language',
    y='need_pct',
    kind='bar',
    color='purple',
    data=c16001_county
)
plt.title('Percentage That Need English Assistance by Detailed Language')
plt.xlabel('Detailed Language Group')
plt.ylabel('Percentage Needing Assistance (%)')
plt.xticks(rotation=65, ha='right')
plt.tight_layout()
plt.savefig('plot4_detailed_language_percentage.png')
plt.show()


c16001_county = c16001_county.sort_values(
                'need_5plus', ascending=False)
sns.catplot(
    x='language',
    y='need_5plus',
    kind='bar',
    color='teal',
    data=c16001_county
)
plt.title('Amount That Need English Assistance by Detailed Language')
plt.xlabel('Detailed Language Group')
plt.ylabel('Estimated Amount That Need Assistance')
plt.xticks(rotation=65, ha='right')
plt.tight_layout()
plt.savefig('plot5_detailed_language_count.png')
plt.show()
c16001_tract['GEOID'] = c16001_tract['GEOID'].astype(str)
detailed_map = tracts.merge(
    c16001_tract,
    on='GEOID',
    how='inner'
)
detailed_languages = (
    c16001_county.groupby('language')['need_5plus']
    .sum().sort_values(ascending=False)
    .head(4).index)
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))
for language, ax in zip(detailed_languages, axs.flatten()):
    language_data = detailed_map[
        detailed_map['language'] == language
    ]
    language_data.plot(
        column='need_5plus',
        cmap='OrRd',
        legend=True,
        ax=ax,
        edgecolor='white'
    )
    ax.set_title(language)
    ax.set_axis_off()
plt.suptitle('Geographic Distribution of Detailed Language Assistance Needs')
plt.tight_layout()
plt.savefig('plot6_detailed_language_maps.png')
plt.show()
