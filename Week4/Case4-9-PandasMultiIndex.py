#Pandas MultiIndex
#A MultiIndex in Pandas is a hierarchical indexing structure that allows us to represent and work with higher-dimensional data efficiently. 

import pandas as pd

# create a dictionary
data = {
    "Continent": ["North America", "Europe", "Asia", "North America", "Asia", "Europe", "North America", "Asia", "Europe", "Asia"],
    "Country": ["United States", "Germany", "China", "Canada", "Japan", "France", "Mexico", "India", "United Kingdom", "Nepal"],
    "Population": [331002651, 83783942, 1439323776, 37742154, 126476461, 65273511, 128932753, 1380004385, 67886011, 29136808]
}

# create dataframe from dictionary
df = pd.DataFrame(data)

print(df)

"""   Continent         Country  Population
0  North America   United States   331002651
1         Europe         Germany    83783942
2           Asia           China  1439323776
3  North America          Canada    37742154
4           Asia           Japan   126476461
5         Europe          France    65273511
6  North America          Mexico   128932753
7           Asia           India  1380004385
8         Europe  United Kingdom    67886011
9           Asia           Nepal    29136808"""

#Create MultiIndex in Pandas
#In Pandas, we achieve hierarchical indexing using the concept of MultiIndex.

# create a dictionary
data = {
    "Continent": ["North America", "Europe", "Asia", "North America", "Asia", "Europe", "North America", "Asia", "Europe", "Asia"],
    "Country": ["United States", "Germany", "China", "Canada", "Japan", "France", "Mexico", "India", "United Kingdom", "Nepal"],
    "Population": [331002651, 83783942, 1439323776, 37742154, 126476461, 65273511, 128932753, 1380004385, 67886011, 29136808]
}

# create dataframe from dictionary
df = pd.DataFrame(data)

# sort the data by continent
df.sort_values('Continent', inplace=True)

# create a multiindex
df.set_index(['Continent','Country'], inplace=True)

print(df)

"""                           Population    
Continent    Country                   
Asia          China           1439323776
              Japan            126476461
              India           1380004385
              Nepal             29136808
Europe        Germany           83783942
              France            65273511
              United Kingdom    67886011
North America United States    331002651
              Canada            37742154
              Mexico           128932753"""


#Access Rows With MultiIndex

# create a dictionary
data = {
    "Continent": ["North America", "Europe", "Asia", "North America", "Asia", "Europe", "North America", "Asia", "Europe", "Asia"],
    "Country": ["United States", "Germany", "China", "Canada", "Japan", "France", "Mexico", "India", "United Kingdom", "Nepal"],
    "Population": [331002651, 83783942, 1439323776, 37742154, 126476461, 65273511, 128932753, 1380004385, 67886011, 29136808]
}

# create dataframe from dictionary
df = pd.DataFrame(data)

# sort the data by continent
df.sort_values('Continent', inplace=True)

# create a multiindex
df.set_index(['Continent','Country'], inplace=True)

# access all entries under Asia
asia = df.loc['Asia']

# access Canada
canada = df.loc[('North America', 'Canada')]

print('Asia\n', asia)
print('\nCanada\n', canada)

"""Asia
         Population
Country            
China    1439323776
Japan     126476461
India    1380004385
Nepal      29136808

Canada
Population    37742154
Name: (North America, Canada), dtype: int64"""

#MultiIndex from Arrays
# create arrays
continent = ['Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'North America', 'North America', 'North America']
country = ['China', 'India', 'Japan', 'Nepal', 'France', 'Germany', 'United Kingdom', 'Canada', 'Mexico', 'United States']
population = [1439323776, 1380004385, 126476461, 29136808, 65273511, 83783942, 67886011, 37742154, 128932753, 331002651]

# create array of arrays
index_array = [continent, country]

# create multiindex from array
multi_index = pd.MultiIndex.from_arrays(index_array, names=['Continent', 'Country'])

# create dataframe using multiindex
df = pd.DataFrame({'Population' :population}, index=multi_index)

print(df)

"""                            Population
Continent     Country                   
Asia          China           1439323776
              India           1380004385
              Japan            126476461
              Nepal             29136808
Europe        France            65273511
              Germany           83783942
              United Kingdom    67886011
North America Canada            37742154
              Mexico           128932753
              United States    331002651"""


