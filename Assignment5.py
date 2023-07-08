import pandas as pd
import matplotlib as plt
d= pd.read_csv("grainsales.csv")
#print(d)
t1 = d.groupby("State").count()
t2 = d.groupby("GrainName").count()
#print(t1)

t1.plot(kind="pie" , y = "Sales", autopct = '%1.1f%%')
t2.plot(kind="pie",y="Sales", autopct = '%1.1f%%')
d.plot(kind="bar" , y = "Year")
d.plot.bar(x="Year",y="Sales")
t2.plot.barh(x="Year",y="Sales")
t2.plot(kind="hist" , y = "Year")
d.plot(kind="bar" , y = "Sales", stacked =True)
d.plot.scatter(x="State",y="Sales")
d.plot.scatter(x="GrainName",y="Sales")
d.plot(x="GrainName",y="Sales")