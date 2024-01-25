'''Recursive Binary Search.'''

#Solution:

#this function will recursively compute binary search
def r_binarysearch(lst,num,start,end):
    #if difference between start and end is 0, then just check for start
    if (start==end):
        if (lst[start]==num):
            return 'Present'
        else:
            return 'Not present'
    #if difference between start and end is 1, then num could be either one of them
    if (end-start==1):
        if (lst[start]==num) or (lst[end]==num):
            return 'Present'
        else:
            return 'Not present'
    #if difference between start and end is more than 1, compute middle element and look for 'num' on R/L sides
    if (end-start>1):
        mid=(start+end)//2
        
        if (lst[mid]>num):
            end=mid-1
        if (lst[mid]<num):
            start=mid+1
        if (lst[mid]==num):
            return 'Present'
    #if difference btwn start and end is negative, then nothing found
    if (end-start<0):
        return 'Not present'
    
    return r_binarysearch(lst,num,start,end)

#random list
rlst=list(range(1000*1000))
#end
end_rlst=len(rlst)-1
#userinput
userinput=int(input('Enter num to search: '))
#call the function and show result
result=r_binarysearch(rlst,userinput,0,end_rlst)
print(result)

#------------------------------------------------------------------------------------------------------------#
