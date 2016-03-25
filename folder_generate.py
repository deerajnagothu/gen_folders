import csv
import os
def remove_brackets( name ): #remove brackets from the list items
    length = len(name)
    k = length-2
    name = name[2:k]
    return name


student_list=[]
list = csv.reader(open('list.csv','U'),dialect='excel')  #Input excel sheet from the same folder as the script
for row in list:
    student_list.append(row)
for x in range(0, len(student_list)):
    student_list[x]=str(student_list[x])
    student_list[x]=remove_brackets(student_list[x])
print (student_list)
for student in student_list:
    name=str(student)
    os.mkdir(name)  #Create the directory

