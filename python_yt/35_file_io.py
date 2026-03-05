# file read
file = open('file.txt','r')
file_read_data = file.read()
print(file_read_data)
print(file.readline)
print(file.readline())
print(file.readline(5))

file_data_read_again = file.read()
print(file_data_read_again)
file.seek(0)

file_data_read_again = file.read()
print(file_data_read_again)
file.close()
# file write
file = open('file.txt','w')
file.write("This is First Lesson - Python File I/o Write")
# file_read_data = file.read()
file.close()
# file read and write mode
file = open('file.txt','r+')
file.write("File read write with r+")
file_read_data = file.read()
print(file_read_data)
# file append
file = open('file.txt','a+')
file.write("Appended text to the end of file")
file.close()
