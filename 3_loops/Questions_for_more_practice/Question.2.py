'''A sequence of integers of even length is said to be left-heavy if the sum of the terms in the 
left-half of the sequence is greater than the sum of the terms in the right half. It is termed 
right-heavy if the sum of the second half is greater than the first half. It is said to be balanced 
if both the sums are equal. Accept a sequence of comma-separated integers as input. Determine if 
the sequence is left-heavy, right-heavy or balanced and print this as the output.'''

# Solution

L = input().split(',')
p = []
for i in L:
    p.append(int(i))
n = len(p)
left_sum = sum(p[:n//2])
right_sum = sum(p[n//2:])

if right_sum > left_sum:
    print('right-heavy')
elif left_sum > right_sum:
    print('left-sum')
else:
    print('balanced')

#------------------------------------------------------------------------------------------------#
