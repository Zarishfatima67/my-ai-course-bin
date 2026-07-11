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
df = pd.read_csv('RealEstate-USA.csv',delimiter=",")

print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")

#kind='hist'  
g=sns.displot(data=dffilter, x="street" , y="price" , hue="zip_code",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=street , y=price , hue=zip_code,  kind='hist'  )")

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

sns.set(style='whitegrid')

g=sns.displot(data=dffilter, x="street" , y="price" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=street , y=price , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#https://seaborn.pydata.org/generated/seaborn.kdeplot.html
#kind='kde'
g=sns.kdeplot(data=dffilter, x="street")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=street)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.histplot(data=dffilter, x='street', y='price', hue='zip_code', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='street', y='price', hue='zip_code', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")

g = sns.scatterplot(x='street', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='street', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.lineplot(data=dffilter, x="street" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=street , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.barplot(data=dffilter, x="street", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=street, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.catplot(data=dffilter, x="street", y="price")
g.figure.suptitle("sns.catplot(data=df, x=street, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

glue = dffilter.pivot(columns="street", values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=street, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

