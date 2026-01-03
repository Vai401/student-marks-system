'''Student marks system using dictionary'''
std_name_marks={}
user= int (input("how many students you want?"))

for i in range(user):
    name= input("Enter student's Name:")
    marks= int(input("Enter Student's Marks:"))
    std_name_marks[name]=marks

    print(std_name_marks)
