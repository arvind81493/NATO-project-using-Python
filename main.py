# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

               # squaring of number
#
# numbers=[1,2,3,4,5,6]
# new_numbers=[n*n for n in numbers]
# print(new_numbers)

             # even numbers
# numbers=[1,1,2,3,5,8,13,21,34,55]
# even_numbers=[n for n in numbers if n%2==0]
# print(even_numbers)

       # data overlap

# with open("file1.txt") as file1:
#     f1=file1.readlines()
# with open("file2.txt") as file2:
#     f2=file2.readlines()
# result=[int(num) for num in f1 if num in f2]
# # Write your code above 👆
#
# print(result)

    # dictionaery_comprehhension
#
# import random
# names=["Alex","Beth","Caroline","Dave","Eleanor","freddie"]
# dict={n:random.randint(1,100) for n in names}
# print (dict)

# passed_students={student:"passed" for student in dict if dict[student]>40}
# print(passed_students)
#
# passed_students={student:score for (student,score) in dict.items() if score>=60}
# print(passed_students)

# sentence=input()
# data=sentence.split()
# list1={word:len(word) for word in data }
# print(list1)


          # pandas Dataframe
#
# student_dict={"student":["Angela","James","Lily"],
#               "score":[56,76,98]
#               }
# # for (key,value) in student_dict.items():
#     print(student_dict[key])
#
#
# import pandas
# data=pandas.DataFrame(student_dict)
# print(data)
#
# for(index,row) in data.iterrows():
#     print(row)
# for(index,row) in  data.iterrows():
#     if row.student=="Angela":
#         print(row.score)
#
# for(index,row) in data.iterrows():
#     if row.score==98:
#         print(row.student)
#
#
# dict={"A": "Alfa","B":"Bravo"}
# data=pandas.DataFrame(dict)
# print(data)

              # Nato project
#
# import pandas
# data=pandas.read_csv("nato_phonetic_alphabet.csv")
# dict={row.letter:row.code for (index,row) in data.iterrows()}
# print(dict)
#
#
# word=input("Enter the word: ").upper()
# list=[dict[letter] for letter in word]
# print(list)
