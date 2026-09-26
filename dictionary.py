
person_details={"Name":"sai","Age":25,"Desg":"DevOps_Engineer","Phone_no":"8978597741","Email":"saivanapalli29@gmail.com"}
# print(person_dteails)
# print(person_dteails["Name"])
#print(person_details.get("Name"))

person_details.update({"class":"mpc"})
print(person_details.pop("Phone_no"))
person_details.update({"Desg":"python_dev"})
person_details.setdefault("project","uidai")
person_details.setdefault("Name","uidai")
del person_details["class"]
#person_details.clear()
print(person_details.keys())
print(person_details.values())
print(person_details.items())

print(person_details)
d=person_details.copy()
print(d)
# for i, j in person_details.items():
#     print(i,j)


# get() → safe read
# [] → risky read
# pop() → delete + return value
# popitem() → delete + return last pair
# setdefault() → insert only if missing
# update() → bulk insert/overwrite
# keys()/values()/items() → views for looping
# copy() → shallow duplicate
# clear() → empty it out
#