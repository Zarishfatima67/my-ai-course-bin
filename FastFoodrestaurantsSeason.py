import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Sample data
data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

# Set the theme
sns.set_theme(style='darkgrid')
# Alternatively
# sns.set_style('darkgrid')

# Create a plot
sns.lineplot(x='x', y='y', data=data)
plt.show()


# Other themes can be set similarly
sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x', y='y', data=data)
plt.show()


sns.set_theme(style='white')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.show()

# Customize the theme
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

# Create a plot
sns.lineplot(x='x', y='y', data=data)
plt.show()

#RealEstate-USA - based examples
# Load data from a CSV file
df = pd.read_csv('FastFoodRestaurants.csv',delimiter=',')

print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")

#kind='hist'  
g=sns.displot(data=dffilter, x="latitude" , y="name" , hue="longitude",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=latiude , y=name , hue=longitude,  kind='hist'  )")

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.displot(data=dffilter, x="latitude" , y="date_added" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=latitude , y=date_added , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.histplot(data=dffilter, x='latitude', y='name', hue='longitude', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='latitude', y='name', hue='longitude', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")

g = sns.scatterplot(x='latitude', y='name', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='latitude', y='name', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.lineplot(data=dffilter, x="latitude" , y="name"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=latitude , y=name  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.barplot(data=dffilter, x="latitude", y="name", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=latitude, y=name, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.catplot(data=dffilter, x="latitude", y="name")
g.figure.suptitle("sns.catplot(data=df, x=latiude, y=name)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

glue = dffilter.pivot(columns="latitude", values="name")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=latitude, values=name)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
