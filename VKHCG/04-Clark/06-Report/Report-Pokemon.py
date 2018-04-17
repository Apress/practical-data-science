# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + 'VKHCG'
else:
    Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sInputFileName='00-RawData/Pokemon.csv'
################################################################
sOutputFileName='06-Report/01-EDS/02-Python/Report-Pokemon.csv'
Company='04-Clark'
################################################################
### Import Pokemon Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
PokemonRaw=pd.read_csv(sFileName,header=0, index_col=0, \
                       low_memory=False, encoding="latin-1")
print('################################')
################################################################
print(PokemonRaw.head())

sns.lmplot(x='Attack', y='Defense', data=PokemonRaw)

sns.lmplot(x='Attack', y='Defense', data=PokemonRaw,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage

sns.lmplot(x='Attack', y='Defense', data=PokemonRaw,
           fit_reg=False, 
           hue='Stage')

plt.ylim(0, None)
plt.xlim(0, None)

sns.boxplot(data=PokemonRaw)

# Pre-format DataFrame
stats_df = PokemonRaw.drop(['Total', 'Stage', 'Legendary'], axis=1)
 
# New boxplot using stats_df
sns.boxplot(data=stats_df)

# Set theme
sns.set_style('whitegrid')
 
# Violin plot
sns.violinplot(x='Type 1', y='Attack', data=PokemonRaw)

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

# Violin plot with Pokemon color palette
sns.violinplot(x='Type 1', y='Attack', data=PokemonRaw, 
               palette=pkmn_type_colors) # Set color palette

# Swarm plot with Pokemon color palette
sns.swarmplot(x='Type 1', y='Attack', data=PokemonRaw, 
              palette=pkmn_type_colors)

# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack', 
               data=PokemonRaw, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=PokemonRaw, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')

# Melt DataFrame
melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                    var_name="Stat") # Name of melted variable
melted_df.head()

print( stats_df.shape )
print( melted_df.shape )
# (151, 9)
# (906, 5)

# Swarmplot with melted_df
sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1')

# 1. Enlarge the plot
plt.figure(figsize=(10,6))
 
sns.swarmplot(x='Stat', 
              y='value', 
              data=melted_df, 
              hue='Type 1', 
              split=True, # 2. Separate points by hue
              palette=pkmn_type_colors) # 3. Use Pokemon palette
 
# 4. Adjust the y-axis
plt.ylim(0, 260)
 
# 5. Place legend to the right
plt.legend(bbox_to_anchor=(1, 1), loc=2)

# Calculate correlations
corr = stats_df.corr()
 
# Heatmap
sns.heatmap(corr)# Distribution Plot (a.k.a. Histogram)
sns.distplot(PokemonRaw.Attack)

# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Type 1', data=PokemonRaw, palette=pkmn_type_colors)
 
# Rotate x-labels
plt.xticks(rotation=-45)

# Factor Plot
g = sns.factorplot(x='Type 1', 
                   y='Attack', 
                   data=PokemonRaw, 
                   hue='Stage',  # Color by stage
                   col='Stage',  # Separate by stage
                   kind='swarm') # Swarmplot
 
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)

# Density Plot
sns.kdeplot(PokemonRaw.Attack, PokemonRaw.Defense)

# Joint Distribution Plot
sns.jointplot(x='Attack', y='Defense', data=PokemonRaw)


