import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Create an empty dataframe
process = pd.DataFrame()

# ['review_count','is_open','cat','city','stars']
# Import data from csv
df = pd.read_csv('C:/Hary/Bigdata/Apache/Data/ML3/0_0_0.csv', encoding = "ISO-8859-1")
df.head()

# Create our target variable
process['stars'] = df['stars']

# Create our feature variables
process['review_count'] = df['review_count']
process['is_open'] = df['is_open']
process['cat'] = df['cat']
process['city'] = df['city']
process['cat_value'] = [0]*len(df)
process['city_value'] = [0]*len(df)

# Create list to hold string value for category and city
l1_list=(df['cat']).unique()
l2_list=(df['city']).unique()

# Create Dictonary to generate unique id for each string in category and city
result_cat_dict = {}
for i in range(len(l1_list)):
    result_cat_dict[l1_list[i]] = i
#print(result_cat_dict)


result_city_dict = {}
for i in range(len(l2_list)):
    result_city_dict[l2_list[i]] = i
#print(result_city_dict)

# Checking Dictonary to get value using key and key using value
# print(result_city_dict['Chandler'])
# print(list(result_city_dict.keys())[list(result_city_dict.values()).index(2)])

#Update the dataframe with the key values
for i in range(len(result_cat_dict)):
    process.loc[df['cat'] == list(result_cat_dict.keys())[list(result_cat_dict.values()).index(i)], 'cat_value'] = i

for i in range(len(result_city_dict)):
    process.loc[df['city'] == list(result_city_dict.keys())[list(result_city_dict.values()).index(i)], 'city_value'] = i



data, test = train_test_split(process, test_size = 0.2)

# Number of 5*
n_5 = data['stars'][data['stars'] == 5].count()

# Number of 4.5*
n_45 = data['stars'][data['stars'] == 4.5].count()

# Number of 4*
n_4 = data['stars'][data['stars'] == 4].count()

# Number of 3.5*
n_35 = data['stars'][data['stars'] == 3.5].count()

# Number of 3*
n_3 = data['stars'][data['stars'] == 3].count()

# Number of 2.5*
n_25 = data['stars'][data['stars'] == 2.5].count()

# Number of 2*
n_2 = data['stars'][data['stars'] == 2].count()

# Number of 1.5*
n_15 = data['stars'][data['stars'] == 1.5].count()



print("5 Star count  ",n_5)
print("4.5 Star count",n_45)
print("4 Star count  ",n_4)
print("3.5 Star count",n_35)
print("3 Star count  ",n_3)
print("2.5 Star count",n_25)
print("2 Star count  ",n_2)
print("1.5 Star count",n_15)


# Total rows
total_start = data['stars'].count()

# Proability of 5* , 4* --- 1*
P_n_5 = n_5/total_start
P_n_45 = n_45/total_start
P_n_4 = n_4/total_start
P_n_35 = n_35/total_start
P_n_3 = n_3/total_start
P_n_25 = n_25/total_start
P_n_2 = n_2/total_start
P_n_15 = n_15/total_start


# Group the data by stars and calculate the means of each feature
data_means = data.groupby('stars').mean()

# View the values
print(">>>>>>>>> Mean calculation <<<<<<<<<<")
print(data_means)
print(">>>>>>>>> **************** <<<<<<<<<<")
print("\n")

# Group the data by gender and calculate the variance of each feature
data_variance = data.groupby('stars').var()

# View the values
print(">>>>>>>>> Variance calculation <<<<<<<<<<")
print(data_variance)
print(">>>>>>>>> ******************** <<<<<<<<<<")

# Means for 1.5 star
stars_rc_mean15 = data_means['review_count'][data_variance.index == 1.5].values[0]
stars_io_mean15 = data_means['is_open'][data_variance.index == 1.5].values[0]
stars_catV_mean15 = data_means['cat_value'][data_variance.index == 1.5].values[0]
stars_cityV_mean15 = data_means['city_value'][data_variance.index == 1.5].values[0]

# Variance for 1.5 star
stars_rc_variance15 = data_variance['review_count'][data_variance.index == 1.5].values[0]
stars_io_variance15 = data_variance['is_open'][data_variance.index == 1.5].values[0]
stars_catV_variance15 = data_variance['cat_value'][data_variance.index == 1.5].values[0]
stars_cityV_variance15 = data_variance['city_value'][data_variance.index == 1.5].values[0]

# Means for 2.0 star
stars_rc_mean2 = data_means['review_count'][data_variance.index == 2.0].values[0]
stars_io_mean2 = data_means['is_open'][data_variance.index == 2.0].values[0]
stars_catV_mean2 = data_means['cat_value'][data_variance.index == 2.0].values[0]
stars_cityV_mean2 = data_means['city_value'][data_variance.index == 2.0].values[0]

# Variance for 2.0 star
stars_rc_variance2 = data_variance['review_count'][data_variance.index == 2.0].values[0]
stars_io_variance2 = data_variance['is_open'][data_variance.index == 2.0].values[0]
stars_catV_variance2 = data_variance['cat_value'][data_variance.index == 2.0].values[0]
stars_cityV_variance2 = data_variance['city_value'][data_variance.index == 2.0].values[0]

# Means for 2.5 star
stars_rc_mean25 = data_means['review_count'][data_variance.index == 2.5].values[0]
stars_io_mean25 = data_means['is_open'][data_variance.index == 2.5].values[0]
stars_catV_mean25 = data_means['cat_value'][data_variance.index == 2.5].values[0]
stars_cityV_mean25 = data_means['city_value'][data_variance.index == 2.5].values[0]

# Variance for 2.5 star
stars_rc_variance25 = data_variance['review_count'][data_variance.index == 2.5].values[0]
stars_io_variance25 = data_variance['is_open'][data_variance.index == 2.5].values[0]
stars_catV_variance25 = data_variance['cat_value'][data_variance.index == 2.5].values[0]
stars_cityV_variance25 = data_variance['city_value'][data_variance.index == 2.5].values[0]

# Means for 3.0 star
stars_rc_mean3 = data_means['review_count'][data_variance.index == 3.0].values[0]
stars_io_mean3 = data_means['is_open'][data_variance.index == 3.0].values[0]
stars_catV_mean3 = data_means['cat_value'][data_variance.index == 3.0].values[0]
stars_cityV_mean3 = data_means['city_value'][data_variance.index == 3.0].values[0]

# Variance for 3.0 star
stars_rc_variance3 = data_variance['review_count'][data_variance.index == 3.0].values[0]
stars_io_variance3 = data_variance['is_open'][data_variance.index == 3.0].values[0]
stars_catV_variance3 = data_variance['cat_value'][data_variance.index == 3.0].values[0]
stars_cityV_variance3 = data_variance['city_value'][data_variance.index == 3.0].values[0]

# Means for 3.5 star
stars_rc_mean35 = data_means['review_count'][data_variance.index == 3.5].values[0]
stars_io_mean35 = data_means['is_open'][data_variance.index == 3.5].values[0]
stars_catV_mean35 = data_means['cat_value'][data_variance.index == 3.5].values[0]
stars_cityV_mean35 = data_means['city_value'][data_variance.index == 3.5].values[0]

# Variance for 3.5 star
stars_rc_variance35 = data_variance['review_count'][data_variance.index == 3.5].values[0]
stars_io_variance35 = data_variance['is_open'][data_variance.index == 3.5].values[0]
stars_catV_variance35 = data_variance['cat_value'][data_variance.index == 3.5].values[0]
stars_cityV_variance35 = data_variance['city_value'][data_variance.index == 3.5].values[0]

# Means for 4.0 star
stars_rc_mean4 = data_means['review_count'][data_variance.index == 4.0].values[0]
stars_io_mean4 = data_means['is_open'][data_variance.index == 4.0].values[0]
stars_catV_mean4 = data_means['cat_value'][data_variance.index == 4.0].values[0]
stars_cityV_mean4 = data_means['city_value'][data_variance.index == 4.0].values[0]

# Variance for 4.0 star
stars_rc_variance4 = data_variance['review_count'][data_variance.index == 4.0].values[0]
stars_io_variance4 = data_variance['is_open'][data_variance.index == 4.0].values[0]
stars_catV_variance4 = data_variance['cat_value'][data_variance.index == 4.0].values[0]
stars_cityV_variance4 = data_variance['city_value'][data_variance.index == 4.0].values[0]

# Means for 4.5 star
stars_rc_mean45 = data_means['review_count'][data_variance.index == 4.5].values[0]
stars_io_mean45 = data_means['is_open'][data_variance.index == 4.5].values[0]
stars_catV_mean45 = data_means['cat_value'][data_variance.index == 4.5].values[0]
stars_cityV_mean45 = data_means['city_value'][data_variance.index == 4.5].values[0]

# Variance for 4.5 star
stars_rc_variance45 = data_variance['review_count'][data_variance.index == 4.5].values[0]
stars_io_variance45 = data_variance['is_open'][data_variance.index == 4.5].values[0]
stars_catV_variance45 = data_variance['cat_value'][data_variance.index == 4.5].values[0]
stars_cityV_variance45 = data_variance['city_value'][data_variance.index == 4.5].values[0]

# Means for 5.0 star
stars_rc_mean5 = data_means['review_count'][data_variance.index == 5.0].values[0]
stars_io_mean5 = data_means['is_open'][data_variance.index == 5.0].values[0]
stars_catV_mean5 = data_means['cat_value'][data_variance.index == 5.0].values[0]
stars_cityV_mean5 = data_means['city_value'][data_variance.index == 5.0].values[0]

# Variance for 5.0 star
stars_rc_variance5 = data_variance['review_count'][data_variance.index == 5.0].values[0]
stars_io_variance5 = data_variance['is_open'][data_variance.index == 5.0].values[0]
stars_catV_variance5 = data_variance['cat_value'][data_variance.index == 5.0].values[0]
stars_cityV_variance5 = data_variance['city_value'][data_variance.index == 5.0].values[0]

print("Variance and mean for star 5",stars_rc_variance5,stars_rc_mean5)
# Creating function that calculates p(x | y):
def p_x_given_y(x, mean_y, variance_y):

    # Input the arguments into a probability density function
    p = 1/(np.sqrt(2*np.pi*variance_y)) * np.exp((-(x-mean_y)**2)/(2*variance_y))

    # return p
    return p


def predict_model(rc,io,cav,civ):
    # Numerator of the posterior if the unclassified observation is a 1.5 stars
    star_15=(P_n_15 * \
p_x_given_y(rc, stars_rc_mean15, stars_rc_variance15) * \
p_x_given_y(io, stars_io_mean15, stars_io_variance15) * \
p_x_given_y(cav, stars_catV_mean15, stars_catV_variance15) * \
p_x_given_y(civ, stars_cityV_mean15, stars_cityV_variance15))

# Numerator of the posterior if the unclassified observation is a 2 stars
    star_2=(P_n_2 * \
p_x_given_y(rc, stars_rc_mean2, stars_rc_variance2) * \
p_x_given_y(io, stars_io_mean2, stars_io_variance2) * \
p_x_given_y(cav, stars_catV_mean2, stars_catV_variance2) * \
p_x_given_y(civ, stars_cityV_mean2, stars_cityV_variance2))

# Numerator of the posterior if the unclassified observation is a 2.5 stars
    star_25=(P_n_25 * \
p_x_given_y(rc, stars_rc_mean25, stars_rc_variance25) * \
p_x_given_y(io, stars_io_mean25, stars_io_variance25) * \
p_x_given_y(cav, stars_catV_mean25, stars_catV_variance25) * \
p_x_given_y(civ, stars_cityV_mean25, stars_cityV_variance25))

# Numerator of the posterior if the unclassified observation is a 3 stars
    star_3=(P_n_3 * \
p_x_given_y(rc, stars_rc_mean3, stars_rc_variance3) * \
p_x_given_y(io, stars_io_mean3, stars_io_variance3) * \
p_x_given_y(cav, stars_catV_mean3, stars_catV_variance3) * \
p_x_given_y(civ, stars_cityV_mean3, stars_cityV_variance3))

# Numerator of the posterior if the unclassified observation is a 3.5 stars
    star_35=(P_n_35 * \
p_x_given_y(rc, stars_rc_mean35, stars_rc_variance35) * \
p_x_given_y(io, stars_io_mean35, stars_io_variance35) * \
p_x_given_y(cav, stars_catV_mean35, stars_catV_variance35) * \
p_x_given_y(civ, stars_cityV_mean35, stars_cityV_variance35))

# Numerator of the posterior if the unclassified observation is a 4 stars
    star_4=(P_n_4 * \
p_x_given_y(rc, stars_rc_mean4, stars_rc_variance4) * \
p_x_given_y(io, stars_io_mean4, stars_io_variance4) * \
p_x_given_y(cav, stars_catV_mean4, stars_catV_variance4) * \
p_x_given_y(civ, stars_cityV_mean4, stars_cityV_variance4))

# Numerator of the posterior if the unclassified observation is a 4.5 stars
    star_45=(P_n_45 * \
p_x_given_y(rc, stars_rc_mean45, stars_rc_variance45) * \
p_x_given_y(io, stars_io_mean45, stars_io_variance45) * \
p_x_given_y(cav, stars_catV_mean45, stars_catV_variance45) * \
p_x_given_y(civ, stars_cityV_mean45, stars_cityV_variance45))

# Numerator of the posterior if the unclassified observation is a 5 stars
    star_5=(P_n_5 * \
p_x_given_y(rc, stars_rc_mean5, stars_rc_variance5) * \
p_x_given_y(io, stars_io_mean5, stars_io_variance5) * \
p_x_given_y(cav, stars_catV_mean5, stars_catV_variance5) * \
p_x_given_y(civ, stars_cityV_mean5, stars_cityV_variance5))

    # print("1.5 star rating accuracy", star_15)
    # print("2 star rating accuracy", star_2)
    # print("2.5 star rating accuracy", star_25)
    # print("3 star rating accuracy", star_3)
    # print("3.5 star rating accuracy", star_35)
    # print("4 star rating accuracy", star_4)
    # print("4.5 star rating accuracy", star_45)
    # print("5 star rating accuracy", star_5)

    find_list=[star_15,star_2,star_25,star_3,star_35,star_4,star_45,star_5]
    Largest = max(find_list)
    print(Largest)
    if Largest==star_15:
        print("Restuarant is likely to get 1.5 star rating")
        Lar=1.5
    if Largest==star_2:
        print("Restuarant is likely to get 2 star rating")
        Lar = 2
    if Largest==star_25:
        print("Restuarant is likely to get 2.5 star rating")
        Lar = 2.5
    if Largest==star_3:
        print("Restuarant is likely to get 3 star rating")
        Lar = 3
    if Largest==star_35:
        print("Restuarant is likely to get 3.5 star rating")
        Lar = 3.5
    if Largest==star_4:
        print("Restuarant is likely to get 4 star rating")
        Lar = 4
    if Largest==star_45:
        print("Restuarant is likely to get 4.5 star rating")
        Lar = 4.5
    if Largest==star_5:
        print("Restuarant is likely to get 5 star rating")
        Lar = 5

    # return p
    return Lar


print("Test dataframe length ---> ", len(test))
total_count=len(test);
success_count=0;
round_success_count=0

for index, row in test.iterrows():
    rc=row["review_count"]
    io=row["is_open"]
    ca = row["cat"]
    ci = row["city"]
    cav = row["cat_value"]
    civ = row["city_value"]
    es = row["stars"]

    expected_value=es

    # call the predict function
    resulted_value=predict_model(rc,io,cav,civ)

    print("             Expected star rating value",expected_value)
    print("             Calculated star rating value",resulted_value)
    if expected_value==resulted_value:
        success_count=success_count+1


    round_expected_value = round(expected_value)
    round_resulted_value = round(resulted_value)

    print("             Rounded Expected star rating value", round_expected_value)
    print("             Rounded Calculated star rating value", round_resulted_value)
    if round_expected_value == round_resulted_value:
        round_success_count = round_success_count + 1


print("Total size of the Dataset",len(process))
print("Training dataset size",len(data))
print("Test dataset size",len(test))
#print("Total success count",success_count)
print("Successfully predicted count",round_success_count)
per=(success_count/total_count)*100
#print("100% Accuracy rate",per)
per1=(round_success_count/total_count)*100
print("Accuracy rate",per1)