# import json
#
# data = {"Spain": "Madrid"}
#
# with open("Spain.json", "w") as f:
#     json.dump(data, f)
#
# json_string = json.dumps(data)
# print("^", json_string)


#-------------------------------------------------
#
# import json
# from random import choice
#
# def gen_person():
#     name = ''
#     tel = ''
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
#     while len(name) != 7:
#         name += choice(letters)
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = { 'name': name, 'tel': tel  }
#     return person
#
# def write_json(person_dict):
#
#     dict_key = " "
#     letters = "1234567890"
#
#     while len(dict_key) != 4:  # --------generator of dict keys
#         dict_key += choice(letters)
#     try:
#         data = json.load(open("persons.json"))
#         # print("DATA", data)
#     except FileNotFoundError:
#         data = {}
#
#     data[dict_key] = person_dict
#     print("Final_data", data)
#
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#     # json_string = json.dumps(data)
#     # print("---", json_string)
#
#
# for i in range(1):
#     write_json(gen_person())
#

#
# a = {'a': "aaa", 'b': "bbb", 'c': "ccc"}
# # b=(*a.values())


# -------------------------------------------
# dict_article = {
#     'Name ': "First",
#     "Author ": "Vasya",
#     "Quantity of letters ": "345345",
#     "Description ": "something..."
# }
# # for key in dict_article:
# #     dict_article[key] = input(f'Input {key} articles: ')
# #
# # print(dict_article, "---")
#
#
# class Article:
#     def __init__(self, title, author, pages, description):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.descriptions = description
#
#
#     def __str__(self):
#         print(" ***  working __str__  *** ")
#         return f"{self.title} ({self.author})"
#
# diction={}
# g=dict_article.values()
# print(g)
# print(*dict_article.values())
# l=Article(*dict_article.values())
# print(l, "---")
# diction[l] = l
# print("DICT: ", diction)
# print("DICT2: ", *diction)

#------------------------------------------------


# dict_sample = {
#   "Company": "Toyota",
#   "model": "Premio",
#   "year": 2012
# }
#
#
# # g= "jjj kkk nnn mmm"
# # # dict_sample["Capacity"] = "1800CC"
# # dict_sample[g.title] = g
# # print(dict_sample)
#
#
# a = {}
# b ='aaa vvv bbb'
# a[b] = b
# print(a)



# a= 1
# b = 5
# while a<b:
#   print(a**2)
#   a+=1



# a= 45.3
# b=1
# while b <11:
#   print(b*a)
#   b+=1


# a=6
# b=1
# c=0
# while b<a:
#   c+=1/b
#   b+=1
# print(c)

# b=0
# a=""
# while a!="0":
#   a=input(":")
#   b+=int(a)
# print(b)

# a="qwe---fgh---tyu"
# while "--" in a:
#   a=a.replace("--", "-")
# print(a)



# a= "12345"
# b = 1
# for i in a:
#   b=b*int(i)
#   print(b)


# a=100
# b=1
# while b<a:
#   if b%4==0:
#     print(b)
#   b+=1



# print("kjhkjh")

# a=20
# for i in range(1,21):
#   if a%i==0:
#     print(i)
