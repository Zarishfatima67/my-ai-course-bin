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
df = pd.read_csv('USStartupGrowth.csv',delimiter=',')

print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")

#kind='hist'  
g=sns.displot(data=dffilter, x="Country" , y="Number of Investors" , hue="Growth Rate (%)",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Country , y=Number of Investors , hue=Growth Rate (%),  kind='hist'  )")

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.displot(data=dffilter, x="Country" , y="Number of Investors" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Country , y=Number of Investors , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.kdeplot(data=dffilter, x="Country")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=Country)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.scatterplot(x='Country', y='Number', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='Country', y='Number of Investors', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.lineplot(data=dffilter, x="Country" , y="Number of Investors"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=Country , y=Number of Investors  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.barplot(data=dffilter, x="Country", y="Number of Investors", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=Country, y=Number of Investors, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.catplot(data=dffilter, x="Country", y="Number of Investors")
g.figure.suptitle("sns.catplot(data=df, x=Country, y=Number of Investors)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

glue = dffilter.pivot(columns="Country", values="Number of Investors")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=Country, values=Number of Investors)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
