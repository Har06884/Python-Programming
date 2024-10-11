print("This is a dictionary, the uses {} brackets")
print()

#declare the dictionary with key-values
student = {
    "name": "Chris",
    "age": 41,
    "course": "MSc Computing and Information Systems"
    }

#print the dictionary
print("This is the dictionary",student)

#print a element of the dictionary
print("Lets access a Value in the dictionary:", student["name"])

#update part of the dictionary
student["age"] = 38
print(student)

#access the keys in the dictionary
x = student.keys()
print(x)

#add to the dictioanary
student["email"] = "christopher.harrison@coleggwent.ac.uk"
print(student)

#update the dictionary
student.update({"tel": "01495333666"})
print(student)

#pop to remove
student.pop("tel")
print(student)
#del to remove
del student["email"]
print(student)
#clear
student.clear()
print(student)

#nested dictionary
student = {
    "Cyber Y2.1":{
        "id": 11002,
        "name": "Timmy",
        "Group": "A"
        },
    "Cyber Y2.2" :{
        "id": 11003,
        "name": "Sally",
        "Group": "B"
        },
    "Cyber Y2.3" :{
        "id": 11004,
        "name": "Jack",
        "Group": "A"
        },
    }

print(student)      
print(student["Cyber Y2.2"]["id"])
