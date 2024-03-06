'''para is a sequence of space-separated words. 
All words will be in lower case. There will be a single space between consecutive words. 
The string has no other special characters other than the space. 
Write a function named exact_count that accepts the string para and a positive integer n as arguments. 
You have to return True if there is at least one word in para that occurs exactly n times, and False otherwise.'''

# Solution:

#method1.
def exact_count(para, n):
    words = para.split()
    for word in words:
        if words.count(word) == n:
            return True
        return False

print(exact_count(input(), int(input())))


#method2.
def exact_count(para, n):
    D = dict()
    words = para.split()
    for word in words:
        if word in D:
            D[word]+=1
        D[word] = 0
    
    for word in D:
        if D[word]==n:
            return True
    return False

print(exact_count(input(), int(input())))

#------------------------------------------------------------------------------------------#
