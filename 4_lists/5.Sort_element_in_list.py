'''Sort the given list without using 'sort() function' and then print sorted list'''

#Answer:

#collecting elments and converting into list
list1=input("Enter the number(elements) seperated by space\nInput: ").split()

#converting string elements into integer
for n in range(0, len(list1)):
    list1[n]=int(list1[n])

#create a empty list to store sorted elements
list2=[]

#loop the sorting process until list1 is empty
while (len(list1)>0):
    #initializing mininum value as first element of list1
    min=list1[0]
    #loop to find mininum value
    for elem in range(len(list1)):
        if list1[elem]<min:
            min=list1[elem]
    #append minimum value to list2
    list2.append(min)
    #remove minimum value from list1
    list1.remove(min)

#display sorted list
print(f'The sorted list is: {list2}')

#------------------------------------------------------------------------------------------#
