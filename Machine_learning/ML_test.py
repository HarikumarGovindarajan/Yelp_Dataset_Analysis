# Required Python Machine learning Packages
import pandas as pd
import numpy as np
# For preprocessing the data
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
# To split the dataset into train and test datasets
from sklearn.cross_validation import train_test_split
# To model the Gaussian Navie Bayes classifier
from sklearn.naive_bayes import GaussianNB
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score

#Data set
#1 - business_id
#2 - stars
#3 - review_count
#4 - is_open
#5 - cat
#6 - city
#7 - user_review_count
#8 - useful
#9 - funny
#10 - cool
#11 - fans
#12 - average_stars
#13 - tip_like_count

#business_id,stars,review_count,is_open,cat,city,user_review_count,useful,funny,cool,fans,average_stars,tip_like_count

# create data frame containing your data, each column can be accessed # by df['column   name']
df = pd.read_csv('C:/Hary/Bigdata/Apache/Data/ML/0_0_0.csv',header = None, delimiter=' *, *', engine='python')

df.columns = ['review_count','is_open','cat','city','stars']

print(df.isnull().sum())

df_rev = df

df_rev.describe(include='all')


le = preprocessing.LabelEncoder()
review_count = le.fit_transform(df.review_count)
is_open = le.fit_transform(df.is_open)
cat   = le.fit_transform(df.cat)
city = le.fit_transform(df.city)
stars = le.fit_transform(df.stars)

#initialize the encoded categorical columns
df_rev['review_count'] = review_count
df_rev['is_open'] = is_open
df_rev['cat'] = cat
df_rev['city'] = city
df_rev['stars'] = stars

num_features = ['review_count','is_open','cat','city','stars']

scaled_features = {}
for each in num_features:
    mean, std = df_rev[each].mean(), df_rev[each].std()
    scaled_features[each] = [mean, std]
    df_rev.loc[:, each] = (df_rev[each] - mean) / std


features = df_rev.values[:,:4]
target = df_rev.values[:,5]
features_train, features_test, target_train, target_test = train_test_split(features,
                                                                            target, test_size = 0.33, random_state = 10)

clf = GaussianNB()
clf.fit(features_train, target_train)
target_pred = clf.predict(features_test)

print(accuracy_score(target_test, target_pred, normalize = True))

