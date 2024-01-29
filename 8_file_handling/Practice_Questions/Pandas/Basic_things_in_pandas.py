'''Fetch data from the .csv file in the directory 'example_files'.'''

# Solution:

# import pandas
import pandas

# read and save the csv file
pincodes=pandas.read_csv('8_file_handling\Practice_Questions\example_files\pincodes.csv')

# print (no.of rows,no. of columns)
print(pincodes.shape)

# print all the data given
print(pincodes.count)

# print maximum among all
print(pincodes.max())

# print minimum among all
print(pincodes.min())

# print average of all the given all values
print(pincodes.mean())

# print the sum of ...
print(pincodes.sum())

# sort the values
print(pincodes.sort_values(ascending=False))       # By default it sorts in ascending order


# dataframe and series

# fetch sample data
print(pincodes.head())      # by default frist 5 rows
print(pincodes.tail())      # by defualt last 5 rows

# return a data of a particular
print(pincodes.groupby())       # returns a dictionary

#---------------------------------------------------------------------------------------------#
