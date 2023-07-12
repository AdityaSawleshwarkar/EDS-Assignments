import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.cluster 
# import KMeans

#including the dataset
df = pd.read_csv("Titanic.csv")
class_counts = df['Pclass'].value_counts()

#Print count of passengers who were in 1st
#class ,2nd class ,3rd class?
count_1 = len(df.loc[df['Pclass']==1])
count_2 = len(df.loc[df['Pclass']==2])
count_3 = len(df.loc[df['Pclass']==3])

print("No. of passengers of 1st class: ",count_1)
print("No. of passengers of 2nd class: ",count_2)
print("No. of passengers of 3rd class: ",count_3)

#Print no. of passengers who survived
count = len(df.loc[df['Survived']==1])
print('No of passengers who survived: ',count)

#Print count of passengers who didn't survived
count = len(df.loc[df['Survived']==0])
print("The no. of passengers who didn't survived: ",count)

#Use groupby funtion to count the number of passengers embarked from C,Q,S spot?
a = df.groupby("Embarked").count()
print(a)

#count the number of passengers in each class
passenger_counts = df['Pclass'].value_counts()

#create a bar chart
plt.bar(passenger_counts.index, passenger_counts.values)
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.title('No. of passenger and Class')
plt.show()

#create a pie chart
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%')
plt.title('Passenger Class Distribution')
plt.show()

#count the number of survivors and non-survivors
survivor = df['Survived'].value_counts()

#create a pie chart
plt.pie(survivor.values, labels=survivor.index, autopct='%1.1f%%')
plt.title('Passenger Survival Rate')
plt.show()

sns.countplot(data=df, x='Embarked',hue='Survived')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.title('Embarked and Survival')
plt.show()

age_data = df['Age']
plt.hist(age_data, bins=20)
plt.xlabel('Age')
plt.ylabel('Number')
plt.title('Passenger age distribution')
plt.show()



#Predictive technique(Kmean)
Data = {'x':df['Age'],'y':df["Fare"]}
df = pd.DataFrame(Data, columns=['x','y'])

plt.xlabel("Age")
plt.ylabel("Fare")
plt.scatter(df['x'],df['y'])
plt.show()
