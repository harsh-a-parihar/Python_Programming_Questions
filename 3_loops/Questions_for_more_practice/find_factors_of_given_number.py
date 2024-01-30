'''Count the number of factors and print them, a given number has.'''

#Solution:

num=int(input('Enter the number: '))
count=0
factors=[]

for i in range(1,num):
    if num%i==0:
        count+=1
        factors.append(i)
print(f'All the factors of {num} are: {factors}\n')
print(f'Total number of factors are {count}.')

#------------------------------------------------------------#
