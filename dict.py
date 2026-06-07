# info = {
#     "key": "value",
#     "emotion": "happy",
#     "hobby": "dancing"
# }
# print(info["emotion"])

# null_dict = {}
# print(null_dict)

student = {
    "name": "Janhvi Gupta",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 99
    }
}
# print(student["name1"]) #shows error
# print(student.get("name1")) #gives none

new_dict = {"place": "Gurgaon"}
student.update(new_dict)

print(student)