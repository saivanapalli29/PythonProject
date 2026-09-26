import math

def paint_req(height,width,cover):
    area = height*width
    cans_require=math.ceil(area/cover)
    return cans_require
ht=int(input("enter the wall height in mtrs:"))
wt=int(input("enter the wall width in mtrs:"))
coverage=9

result=paint_req(height=ht,width=wt,cover=coverage)
print(f"required cans to paint a wall is {result} cans ")
