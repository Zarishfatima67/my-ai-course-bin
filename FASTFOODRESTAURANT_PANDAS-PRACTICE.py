import pandas as pd
df=pd.read_csv('FastFoodRestaurants.csv',delimiter=',')
print(df)
print("df - data types" , df.dtypes)
print("df.info():",df.info())

# display the last four rows
print('Last four Rows:')
print(df.tail(4))

# display the first four rows
print('first four Rows:')
print(df.head(4))

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()

# access the Name column
address = df['address']
print("access the Name column: df : ")
print(address)
print()

# access multiple columns
address_latitude = df[['address','latitude']]
print("access multiple columns: df : ")
print(address_latitude)
print()

# Case 1 : using .loc - default case - starts here
#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 4]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:6]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df.loc[df['address'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'address']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:,['address','latitude']]
print("#Selecting multiple columns using .loc")

print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'location':'address']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['address'] == 'Gateway Properties','postalCode':'address']
print("#Combined row and column selection using .loc")
print(second_row8)
print()


# Case 1 : using .loc - default case - ends here
print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as address
# Why Second cycle - Note Index - , index_col='address'
df_index_col=pd.read_csv('FastFoodRestaurants.csv',delimiter=',')
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
# Second cycle - with index_col as address
#Selecting a single row using .loc
second_row = df_index_col.loc[324]
print("#Selecting a single row using .loc")
print(second_row)
print()
#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[324, 408]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()
#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[324:6098]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()
#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['address'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()
#Selecting a single column using .loc
second_row5 = df_index_col.loc[:324,'address']
print("#Selecting a single column using .loc")
print(second_row5)
print()
#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:324,['address','latitude']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()
#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:324,'address':'laltiude']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()
#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['address'] == 'Gateway Properties','location':'address']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 2 : using .loc with index_col  -  ends here
print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here
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
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()
#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,5]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()
#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()
#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here