import seaborn as sns
import pandas as pd

# Load data from a CSV file
df = pd.read_csv('Week3/zameencom-property-data-By-Kaggle-short.csv',delimiter=";",parse_dates=[14], date_format={'date_added': '%d-%m-%Y'} , index_col='property_id')

dffilter= df.head(20)
# Use Seaborn to create a plot
sns.set(style="whitegrid")
plot = sns.scatterplot(x='agency', y='price', data=dffilter)

# Display the plot
plot.figure.show()

read = input("Waitm for me....")
