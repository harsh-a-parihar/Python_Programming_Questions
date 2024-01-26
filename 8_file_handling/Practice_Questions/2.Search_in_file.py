'''Find a pincode from a txt file which has a dataset of pincodes of all over India.'''

# Solution:

# Open the dataset file in the read mode and assign variable
pf=open('8_file_handling\Practice_Questions\example_files\pincodes.txt','r')
#take input num
num=int(input("Enter pincode to search: "))

# using while loop with flag
flag=True
s='0'
#continue loop till dataset ends
while(s!=''):
    #read line-by-line 
    s=pf.readline()
    if (s!=''):
        # convert string(s) into int
        x=int(s)
        # check if x is equal to given num
        if (x==num):
            flag=False
            print('Found the pincode')
            break
if flag==True:
    print('Not found the pincode')

#-----------------------------------------------------------------------------------------------------#
