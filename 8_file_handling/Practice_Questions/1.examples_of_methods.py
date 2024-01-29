'''File Handling concepts explained with the examples.'''

#Solution:

# To open a file
f=open('8_file_handling\Practice_Questions\example_files\example.txt','rt')    # 'r' read and 't' text are the default values

# Write something in the file with write 'w' mode
f=open('8_file_handling\Practice_Questions\example_files\example.txt','w')

# first line
f.write('line one')

# write in next line
f.write('\n')

# secode line
f.write('line two')

# Close the opened file after writing. If once closed, you can't access it.
f.close()

# To read what is in the file open in reading 'r' mode
x=open('8_file_handling\Practice_Questions\example_files\example.txt','r')
print(x.read())     # by default .read() reads the whole text, you can also specify character

# To read what is in the file line-by-line
x=open('8_file_handling\Practice_Questions\example_files\example.txt','r')
print(x.readline())

# To change the position of a file and return the new one
x=open('8_file_handling\Practice_Questions\example_files\example.txt','r')
x.seek(4)
print(x.readline())

#-----------------------------------------------------------------------------------------------------------#
