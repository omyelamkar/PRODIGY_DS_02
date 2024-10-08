
import pandas as p
import matplot

data=p.read_csv("/content/train.csv")
print(data.head(),end="\n")                   #prints the first 5 rows from my train dataset

print(data.tail(),end='\n')                   #prints the last 5 rows from my train dataset

print(data.info(),end='\n')                   #General information about the dataset like non-null count and datatype of each column

print(data.describe(),end='\n')               #It describes my dataset like mean,standard deviation, minimum, maximum etc...

print(data.isnull().sum(),end='\n')           #It returns the null values count in each column

''' Data Cleaning process'''
data['Age'].fillna(data['Age'].median(),inplace=True) #filling the missing value by using the median value of that column age.

data['Embarked'].fillna(method='ffill',inplace=True)  #Filling the missing value in embarked with the value forward filling method.

data['Cabin'].fillna(method='bfill',inplace=True)     #filling the missing value in cabin column using backward fill method.

data.dropna(how='any',inplace=True)            #Incase there is any other possible null values so i am drop those rows alone.
print(data.isnull().sum())                     #After clean the data, now i am check the count of null value and the result is zero.

data.plot(kind='line',x='Age',y='Fare',color='red')
# plt.title('Relationship between Age and Fare')
plt.show()

data.plot(kind='line',x='Sex',y='Fare',color='blue')
plt.title=('Relationship between Age and their Sex')
plt.show()