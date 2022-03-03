#***************************************************** Calling an API ?


# import json ,requests
# url="http://saral.navgurukul.org/api/courses"
# a=requests.get(url)
# print(a.text)
# # print(a.json())

# a=requests.get("http://saral.navgurukul.org/api/courses")
# # print(a.text)
# print(a.json())

#..................................... Assignment ?

# import json, requests

# a="http://saral.navgurukul.org/api/courses"
# a=requests.get(a)
# print(a.json())
# b=open("courses.json","w")
# # json.dump(a.text,b, indent=4)     #.................data text form 
# json.dump(a.json(),b, indent=4)
# b.close()

# with open("aa.json","w") as f:
#     json.dump(a.json(),f, indent=4)
#************************************************************* using-json ?

# import json

# def courses():
#     b=open("courses.json","r")
#     c=json.load(b)
#     for i in c["availableCourses"]:
#         print(i['name'])
# courses()

#........................................................... 

# import json, requests,os
# def courses():
#     b=open("courses.json","r")
#     c=json.load(b)
#     for i in c["availableCourses"]:
#         print(i['name'])

# if (os.path.exists("courses.json")):
#     courses()
# else:
#     a="http://saral.navgurukul.org/api/courses"
#     a=requests.get(a)
#     print(a.json())
#     b=open("courses.json","w")
#     # json.dump(a.text,b, indent=4)     #.................data text form 
#     json.dump(a.json(),b, indent=4)
#     b.close()

#.....................................................

# import json ,requests,os
# def courses():
#     d=1
#     b=open("courses.json","r")
#     c=json.load(b)
#     for i in c["availableCourses"]:
#         print(f"{d}. {i['name']}")
#         # print(d,".",i['name'])
#         d+=1
# if (os.path.exists("courses.json")):
#     courses()
# else:
#     a="http://saral.navgurukul.org/api/courses"
#     a=requests.get(a)
#     print(a.json())
#     b=open("courses.json","w")
#     # json.dump(a.text,b, indent=4)     #.................data text form 
#     json.dump(a.json(),b, indent=4)
#     b.close()

#................................................... complite 

# import json ,requests,os
# def courses():
#     d=1
#     b=open("courses.json","r")
#     c=json.load(b)
#     for i in c["availableCourses"]:
#         print(f"{d}. {i['name']}")
#         # print(d,".",i['name'])
#         d+=1
# if (os.path.exists("courses.json")):
#     courses()
# else:
#     a="http://saral.navgurukul.org/api/courses"
#     a=requests.get(a)
#     print(a.json())
#     b=open("courses.json","w")
#     # json.dump(a.text,b, indent=4)     #.................data text form 
#     json.dump(a.json(),b, indent=4)
#     b.close()
#     d=1
#     b=open("courses.json","r")
#     c=json.load(b)
#     for i in c["availableCourses"]:
#         print(f"{d}. {i['name']}")
#         # print(d,".",i['name'])
#         d+=1


    

#**************************************************** Thodi si Programming ?

# import json ,requests,os
# def courses():
#     d=1
#     b=open("courses.json","r")
#     c=json.load(b)
#     for i in c["availableCourses"]:
#         print(f"{d}. {i['name']}")
#         d+=1
#     if (os.path.exists("courses.json")):
#         num=int(input("Enter the number :"))
#         e=c["availableCourses"][num-1]
#         print(e)

#     else:
#         a="http://saral.navgurukul.org/api/courses"
#         a=requests.get(a)
#         print(a.json())
#         b=open("courses.json","w")
#         json.dump(a.json(),b, indent=4)
#         b.close()
#         num=int(input("Enter the number :"))
#         e=c["availableCourses"][num-1]
#         print(e)
# courses()

#************************************************************************************ api-again ?

# import json ,requests
# url="http://saral.navgurukul.org/api/courses/74/exercises"
# a=requests.get(url)
# # print(a.text)
# print(a.json())

#.......................................  

# import json, requests

# a="http://saral.navgurukul.org/api/courses/74/exercises"
# a=requests.get(a)
# print(a.json())
# b=open("courses1.json","w")
# json.dump(a.json(),b, indent=4)
# b.close()

#............................................. Step - 1

# import json ,requests,os
# def courses():
#     d=1
#     b=open("courses1.json","r")
#     c=json.load(b)
#     for i in c["data"]:
#         print(f"{d}. {i['childExercises']}")
#         d+=1
#     if (os.path.exists("courses1.json")):
#         num=int(input("Enter the number :"))
#         e=c["data"][num-1]
#         print(e)

#     else:
#         a="http://saral.navgurukul.org/api/courses/74/exercises"
#         a=requests.get(a)
#         print(a.json())
#         b=open("courses1.json","w")
#         json.dump(a.json(),b, indent=4)
#         b.close()
#         num=int(input("Enter the number :"))
#         e=c["data"][num-1]
#         print(e)
# courses()

#.................................................. Step - 2

# import json ,requests,os
# def courses():
#     d=1
#     b=open("courses1.json","r")
#     c=json.load(b)
#     for i in c["data"]:
#         print(f"{d}. {i['slug']}")
#         d+=1
#     if (os.path.exists("courses1.json")):
#         num=int(input("Enter the number :"))
#         e=c["data"][num-1]
#         print(e)

#     else:
#         a="http://saral.navgurukul.org/api/courses/74/exercises"
#         a=requests.get(a)
#         print(a.json())
#         b=open("courses1.json","w")
#         json.dump(a.json(),b, indent=4)
#         b.close()
#         num=int(input("Enter the number :"))
#         e=c["data"][num-1]
#         print(e)
    
# courses()

#**************************************************************** Bonus Task ?

# import json ,requests,os
# def courses():
#     if (os.path.exists("courses1.json")):   
#         b=open("courses1.json","r")
#         c=json.load(b)
#         print(c)
#     else:
#         print("fetching data")
#         a="http://saral.navgurukul.org/api/courses/74/exercises"
#         a=requests.get(a)
#         print(a.json())
#         b=open("courses1.json","w")
#         json.dump(a.json(),b, indent=4)
#         b.close()
#         print(b)
# courses()

#****************************************************************** slug-aaya-hai ?

# import json , requests

# def slug():
#     url="http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json"

#     a=requests.get(url)
#     print(a.json())
#     b=open("slug-aaya-hai.json","w")
#     json.dump(a.json(),b, indent=4)
#     b.close()
#     # b=input("Enter your input :")
#     # print(b[1])
# slug()