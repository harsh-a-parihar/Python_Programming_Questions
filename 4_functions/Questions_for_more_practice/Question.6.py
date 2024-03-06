'''The scores_dataset is a list of dictionaries one of whose entries is given below for your reference:

{'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 
 'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75, 
 'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}
An institution decides to allow students to create student groups for each subject where students with similar marks can help each other. But it draws up a set of constraints for creating student groups:

A group should be associated with a particular subject.
The difference between the scores of any two students in the group should be at most mark_limit.
It follows that multiple groups can be formed for a given subject.

Write a function called crowded_group that accepts three arguments as input:

scores_dataset
subject
mark_limit

Return the size of the largest possible group in this subject with the given mark_limit.'''

# Solution:

def crowded_group(scores_dataset, subject, mark_limit):
    marks=[]
    for student in scores_dataset:
        marks.append(student[subject])
    
    marks.sort()
    mgroup=1
    while (marks!=[]):
        start = min(marks)
        marks.remove(start)
        group=[start]

        for mark in marks:
            if (mark-start) <= mark_limit:
                group.append(mark)
        
        if len(group) > mgroup:
            mgroup = len(group)
    
    return mgroup

#---------------------------------------------------------------------------------------#
