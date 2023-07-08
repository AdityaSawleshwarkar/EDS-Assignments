import pandas as pd
df = pd.read_csv("grainsales.csv")

#print All the name of states
print(df["State"])

#print all the states and sales
print("\n",df[["State","Sales"]])

#print max sales
print("\nThe Highest Sales is",df["Sales"].max())

#Find sum of sales
print("\nThe sumation of all the salaries is",df["Sales"].sum())

#Find average sales
print("\nThe average sales is",df["Sales"].sum()/len(df["Sales"]))

#Print top 5 records
print("\nTop 5 records are \n",df.head(5))

# Print bottom 5 records
print("\nBottom 5 records are \n",df.tail(5))

# Print all records stored at even index position
print("\n",df.iloc[::2])

# Print all records stored at odd index position
print("\n",df.iloc[1::2])

#Print all grain names stored at even position
print("\n",df.iloc[::2,0])

#Print all months and years stored at even position
print("\n",df.iloc[::2,3:5])

#print all the entries with state maharashtra
print("\n",df[df["State"]=="Maharashtra"])

#print all the entries with sales greater than 30,00,000
print("\n",df[df["Sales"]>=3000000])

#print the states with sales less than 30,00,000 and grains ragi
print("\n",(df[(df["Sales"]<=3000000) & (df["GrainName"]=="Ragi")]))

#print count of all the Grains
print("\n",df.groupby("GrainName").count())

#best sales month
print("\n",df.groupby("Months").sum())

print('\n',df[df['GrainName']=='Ragi'])

print('\n',df[df['State']=='Tamil Nadu'])

print('\n',df.loc[1:20])
print('\n',df.iloc[1])
print('\n',df.sort_values(by=['Sales'],ascending=[False]))
