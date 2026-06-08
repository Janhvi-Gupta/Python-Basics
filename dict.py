# info = {
#     "key": "value",
#     "emotion": "happy",
#     "hobby": "dancing"
# }
# print(info["emotion"])

# null_dict = {}
# print(null_dict)

# student = {
#     "name": "Janhvi Gupta",
#     "subjects": {
#         "phy": 97,
#         "chem": 98,
#         "math": 99
#     }
# }
# # print(student["name1"]) #shows error
# # print(student.get("name1")) #gives none
# new_dict = {"place": "Gurgaon"}
# student.update(new_dict)
# print(student)

# word_meaning = {
#     "table": {
#         "a piece of furniture",
#         "list of facts & figures",
#     },
#     "cat": "a small animal"
# }

# print(word_meaning)

#WAP to enter marks of 3 subjects from the user and store them in a dictonary. start with an empty dict and add one by one.
marks = {}

x = int(input("Enter marks of Physics: "))
marks.update({"phy": x})
x = int(input("Enter marks of Maths: "))
marks.update({"math": x})
x = int(input("Enter marks of Chemistry: "))
marks.update({"chem": x})

print(marks)