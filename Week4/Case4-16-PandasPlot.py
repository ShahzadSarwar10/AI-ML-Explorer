#Pandas Plot
#Pandas provides a convenient way to visualize data directly from DataFrames and Series using the plot() method.
"""Dataset For Data Visualization
We'll use the following dataset to visualize data.

Car	        Weight
Caterham	0.48 tons
Tesla	    1.7 tons
Audi 	    2 tons
BMW	        2 tons
Ford	    2.5 tons
Jeep	    3 tons"""

#Line Plot For Data Visualization
import pandas as pd
import matplotlib.pyplot as plt

car = ["Caterham", "Tesla", "Audi", "BMW", "Ford", "Jeep"]
weight = [0.48, 1.7, 2, 2, 2.3, 3]

# create a DataFrame
data = {'Car': car, 'Weight': weight}
df = pd.DataFrame(data)

# plot using Pandas
df.plot(x='Car', y='Weight', kind='line', marker='o')
plt.xlabel('Car')
plt.ylabel('Weight')
plt.title('Car Weights')
plt.show()

#Scatter Plots For Data Visualization
import pandas as pd
import matplotlib.pyplot as plt

car = ["Caterham", "Tesla", "Audi", "BMW", "Ford", "Jeep"]
weight = [0.48, 1.7, 2, 2, 2.3, 3]

# create a DataFrame
data = {'Car': car, 'Weight': weight}
df = pd.DataFrame(data)

# scatter plot using Pandas
df.plot(x='Car', y='Weight', kind='scatter', marker='o', color='blue')
plt.xlabel('Car')
plt.ylabel('Weight')
plt.title('Car Weights (Scatter Plot)')
plt.grid(True)
plt.show()

#Bar Graphs For Data Visualization

car = ["Caterham", "Tesla", "Audi", "BMW", "Ford", "Jeep"]
weight = [0.48, 1.7, 2, 2, 2.3, 3]

# create a DataFrame
data = {'Car': car, 'Weight': weight}
df = pd.DataFrame(data)

# bar graph using Pandas
df.plot(x='Car', y='Weight', kind='bar', color='green')
plt.xlabel('Car')
plt.ylabel('Weight')
plt.title('Car Weights (Bar Graph)')
plt.tight_layout()
plt.show()

#Histograms For Data Visualization

weight = [0.48, 1.7, 2, 3]

# create a DataFrame
data = {'Weight': weight}
df = pd.DataFrame(data)

# histogram using Pandas
df['Weight'].plot(kind='hist', bins=10, edgecolor='black', color='blue')
plt.show()

