# **kwargs(keyword arguments)
# **kwargs(double star operator)
# kwargs as parameter is for convention
# kwargs take argument as dictionary datatype
# same as * args if you use normal argument with kwargs 
# then it does not include the normal argument return with it
def func(**kwargs):
    for Key,Value in kwargs.items():
        print(f"{Key} : {Value}")
# Dictionary unpacking
dic = {"Name":"Manjot","Age":21,"Add":"Vasai"}
func(**dic)

# Functions with all Parameter
# def my_function(normal_parameter,*args,Default_Parameter,**kwargs) 
# Please follow the order above to avoid errors 
# PADK

def my_fun(normal,*args,Name="Manjot",**kwargs):
    print(normal)
    print(args)
    print(Name)
    print(kwargs)

my_fun("Singh",1,2,3,4,5,6,a=12,b=31,c=45,d=61)
