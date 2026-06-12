
import pandas as pd

df=pd.read_csv('RealEstate-USA.csv',delimiter=",")
print(df)
#For Pandas :# filling NaN values with 0
df.fillna(0, inplace=True)
print("df - data types", df.dtypes)

print("df.info():"   , df.info())

print("Last four Rows:")
print(df.tail(4))

print("First four Rows:")
print(df.head(4))
print()


#Summary of Statistics of DataFrame using describe() method.
print('Summary of statistics of Dataframe using Describe() method',df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print('Counting the rows and columns in Dataframe  using shape():' ,df.shape)
print()
# access the Name column
price=df['price']
print("access the Name of colume: df :")
print(price)
print()

# access multiple columns
price_bath=df[['price','bath']]
print("access multiple columns:df:")
print(price_bath)
print()
#Selecting single rows using .loc
Second_row=df.loc[1]
print("#Selecting a single row using .loc")
print(Second_row)
print()
#Selecting  multiple rows using .loc
Second_row2=df.loc[[1,3]]
print("#Selecting a multiple row using .loc")
print(Second_row2)
print()
#Selecting a slice of rows using .loc
Second_row3=df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(Second_row3)
print()
#Conditional selection of rows using .loc
Second_row4=df.loc[df['price']=='Gateway Properties']
print("# Conditional Selecting of rows using.loc ")
print(Second_row4)

#Selecting a single column using .loc
Second_row5 = df.loc[:1,'price']
print("Selecting a single column using .loc")
print(Second_row5)
print()

#Selecting multiple columns using .loc
Second_row6=df.loc[:,['price','bath']]
print("Selecting a multiple column using .loc")
print(Second_row6)
print()
#Selecting a slice of columns using .loc
Second_row7=df.loc[:1,'bath':'price']
print("Selecting a slice of  columns using .loc")
print(Second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['price'] == 'Gateway Properties','bath':'price']
print("#Combined row and column selection using .loc")
print(second_row8)
print()


# Case 1 : using .loc - default case - ends here

print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as street
# Why Second cycle - Note Index - , index_col='street'

df_index_col=pd.read_csv('RealEstate-USA.csv',delimiter=",",index_col='street')
#For Pandas :# filling NaN values with 0
df_index_col.fillna(0, inplace=True)

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
print(df_index_col.index[df_index_col.index.duplicated()])
# Second cycle - with index_col as brokered_by
second_row = df_index_col.loc[1962661]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[1962661,1404990 ]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()


#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[1962661:331151]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()
#Conditional selection of rows using .loc
Second_row4=df.loc[df['price']=='Gateway Properties']
print('#Conditional selection of row using .loc')
print(Second_row4)
print()
#Selecting a single column using .loc
second_row5 = df_index_col.loc[:331151,'price']
print("#Selecting a single column using .loc")
print(second_row5)
print()
#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:331151,['price','bath']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:331151,'bath':'price']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()
#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['price'] == 'Gateway Properties','price':'bath']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col  -  ends here
print("# Case 3 : Using .iloc - starts here")
#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()
#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()
#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[3:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()
#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,6]
print("#Selecting a single column using .iloc")
print(second_row5)
print()
#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,6]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()
#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:6]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()
#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:6]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()


