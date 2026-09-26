global_var="sai"
def var():
    #global loca_var
    loca_var="sai_loc"
    print(f"loca is {loca_var}")
    print(global_var)
    def nested():
        print(loca_var)
    nested()
var()
#print(loca_var)