'''Find the average height of all the students in the class room, using Lists.'''

#Anwser:

#take input from user and convert it into list
heights = input("Input a list of student heights separated by space: ").split()
print(heights)
#convert string list into integer list
for n in range(0, len(heights)):
    heights[n]=int(heights[n])

#calculate the total sum of heights and students
sum_heights=0
students=0
for height in heights:
    #sum all the heights
    sum_heights+=height
    #count all the students
    students+=1

#calculate the average height and round it off
average_height=round(sum_heights/students)

#print the average height
print(f'The average height of all the students in the class room is {average_height}')

#----------------------------------------------------------------------------------------#

