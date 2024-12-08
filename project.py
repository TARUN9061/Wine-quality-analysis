import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Task 1
data=pd.read_csv('Wine Quality Dataset.csv')

#print(data.head())

#print(data.shape)

#print(data.index)

#print(data.columns)

#print(data.info())

#checking for null values
#coverting 0's to null
#column=list(data)
#data[column[0:]]=data[column[0:]].replace(0,np.nan)
#print(data.isnull().sum())

#[From the first task observations made are 1.There are total of 4898 rows and 12 columns 
# 2.Each row consist of different acids in wine and quality]

#Task 2
#Visualize the distribution of values of each feature in the data set and calculate central tendency

# 1'st feature
#histogram for fixed acidity feature
#plt.figure(figsize=(11,6))

#sns.histplot(data=data,x='fixed acidity',bins=5,color='orange',edgecolor='linen',alpha=0.5)
#plt.title('Histogram of fixed acidity',fontsize=15)
#plt.xlabel('Fixed acidity',fontsize=15)
#plt.ylabel('Count',fontsize=15)
#plt.show()
#[I observed that 1.histogram for fixed acidity feature is normally distributed
# 2.The maximum values of fixed acidity lies between 6 to 8]


#calculating central tendency for fixed acidity

#calculating mean of fixed acidity feature
#print(round(data['fixed acidity'].mean(),2))

#calculating median of fixed acidity feature
#print(data['fixed acidity'].median())

#creating a histogram for fixed acidity feature and also mean and median of it
#plt.figure(figsize=(11,6))

#sns.histplot(data=data,x='fixed acidity',bins=5,color='orange',edgecolor='linen',alpha=0.5)
#plt.title('Histogram of fixed acidity',fontsize=15)
#plt.xlabel('Fixed acidity',fontsize=15)
#plt.ylabel('Count',fontsize=15)
#plt.vlines(data['fixed acidity'].mean(),ymin=0,ymax=4000,color='blue',label='Mean')
#plt.vlines(data['fixed acidity'].median(),ymin=0,ymax=4000,color='red',label='Median')
#plt.legend()
#plt.show()
#[I observed mean and median are very close to each other. hence i use mean as my central tendency ]


# 2'nd feature
#histogram for volatile acidity feature
#plt.figure(figsize=(11,6))

#sns.histplot(data=data,x='volatile acidity',bins=5,color='green',edgecolor='linen',alpha=0.5)
#plt.title('Histogram of volatile acidity',fontsize=15)
#plt.xlabel('volatile acidity',fontsize=15)
#plt.ylabel('Count',fontsize=15)
#plt.show()
#[I observed that volatile acidity values are not well distributed. There is a positive skewness. So we check distribution using distplot
# the maximum values lies at 0.2]


#Dist plot for volatile acidity feature
#plt.figure(figsize=(11,6))

#sns.distplot(data['volatile acidity'],color='blue')
#plt.title('dist plot of volatile acidity',fontsize=15)
#plt.xlabel('volatile acidity',fontsize=15)
#plt.ylabel('Density',fontsize=15)
#plt.show()
#[I observed dist plot shows normal distribution. It has a bell curve]

#we calculate skewness
#print(data['volatile acidity'].skew())
#[Skewness is 1.57 which is greater than 0. hence it is positively skewed ]

#calculating central tendency for volatile acidity

#calculating mean of volatile acidity feature
#print(round(data['volatile acidity'].mean(),2))

#calculating median of volatile acidity feature
#print(data['volatile acidity'].median())


#creating a histogram for volatile acidity feature and also mean and median of it
#plt.figure(figsize=(11,6))

#sns.histplot(data=data,x='volatile acidity',bins=5,color='green',edgecolor='linen',alpha=0.5)
#plt.title('Histogram of volatile acidity',fontsize=15)
#plt.xlabel('volatile acidity',fontsize=15)
#plt.ylabel('Count',fontsize=15)
#plt.vlines(data['volatile acidity'].mean(),ymin=0,ymax=4000,color='blue',label='Mean')
#plt.vlines(data['volatile acidity'].median(),ymin=0,ymax=4000,color='red',label='Median')
#plt.legend()
#plt.show()
#[I observed mean and median are very close to each other. hence i use mean as my central tendency ]



# 3'rd feature
#histogram for citric acidity feature
#plt.figure(figsize=(11,6))

#sns.histplot(data=data,x='citric acid',bins=5,color='red',edgecolor='linen',alpha=0.5)
#plt.title('Histogram of citric acid',fontsize=15)
#plt.xlabel('citric acid',fontsize=15)
#plt.ylabel('Count',fontsize=15)
#plt.show()
#[I observed that histogram of citric acid is not well distributed, it has skewness]

#calculating skewness of citric acid
#print(data['citric acid'].skew())
#[Skewness is 1.28 which means it is positively skewed]

#calculating central tendency for citric acid

#calculating mean of citric acid feature
#print(round(data['citric acid'].mean(),2))

#calculating median of citric acid feature
#print(data['citric acid'].median())


#creating a histogram for citric acid feature and also mean and median of it
#plt.figure(figsize=(11,6))

#sns.histplot(data=data,x='citric acid',bins=5,color='red',edgecolor='linen',alpha=0.5)
#plt.title('Histogram of citric acid',fontsize=15)
#plt.xlabel('citric acid',fontsize=15)
#plt.ylabel('Count',fontsize=15)
#plt.vlines(data['citric acid'].mean(),ymin=0,ymax=4000,color='blue',label='Mean')
#plt.vlines(data['citric acid'].median(),ymin=0,ymax=4000,color='red',label='Median')
#plt.legend()
#plt.show()
#[I observed mean and median are very close to each other. hence i use mean as my central tendency ]


#Dist plot for citric acid feature
#plt.figure(figsize=(11,6))

#sns.distplot(data['citric acid'],color='red')
#plt.title('dist plot of citric acid',fontsize=15)
#plt.xlabel('citric acid',fontsize=15)
#plt.ylabel('Density',fontsize=15)
#plt.show()
#[I observed dist plot shows normal distribution. It has a bell curve]




#Create count plot for quality feature
#plt.figure(figsize=(11,6))

#sns.countplot(data['quality'])
#plt.title('count plot of quality',fontsize=15)
#plt.xlabel('quality',fontsize=15)
#plt.ylabel('count',fontsize=15)
#plt.show()

#count number of occurences of quality feature
#print(data['quality'].value_counts())
#[I observed that 6 has ocuured many times of 2198. hence 6 is a mode of quality feature]

#[Observations from task 2
# 1.Saw the distribution of the varios features in the data set using appropriate plots
# 2.Calculated central tendency measures like mean, median and mode of various features
# 3.mean and median of all above features has close values, so we choose mean
# 4.mode of quality feature can be choosen as a representative value]

#Task 3
#Create a new pandas series that contains the details of the representative quality for the different types of acid

#rep_acid=pd.Series(index=['fixed acidity','volatile acidity','citric acid','quality'],
 #                   data=[data['fixed acidity'].mean(),data['volatile acidity'].mean(),data['citric acid'].mean(),data['quality'].value_counts().index[0]])

#print(rep_acid)

#[From task 3 I observed
# 1.The mean value of fixed acidity would be 6.854
# 2.The mean value of volatile acidity would be 0.278
# 3.The mean value of citric acid would be 0.334
# 4.The quality would be 6]


#correlation matrix
corr_matrix=data.corr()
print(corr_matrix)

#heatmap plot for correlation
#plt.figure(figsize=(10,6))

#sns.heatmap(corr_matrix,annot=True)
#plt.title('Heatmap')
#plt.show()


#[I observed from heatmap
# 1.Residual sugars and density are strong positive correlated
# 2.Free sulpher dioxide and total sulpher dioxide are moderatly positive correlated
# 3.Total sulpher dioxide and density are moderatly positive correlated
# 4.density and alcohol are strong negative correlated
# 5.Residual sugars and alcohol are moderately negative correlated]



#calculating mean quality by alcohol by groupby analysis
#mean_quality_by_alcohol=data.groupby('alcohol')['quality'].mean()
#print(mean_quality_by_alcohol)
#[i observed as alcohol increses mean of quality increses
# for alcohol value of 14.20 has quality of 7]


#Filter wines with high quality
#high_quality_wine=data[data['quality']>=7]
#print(high_quality_wine)

#sns.scatterplot(x=high_quality_wine['alcohol'],y=high_quality_wine['quality'])
#plt.show()