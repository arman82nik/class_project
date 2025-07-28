import x


def sum_all(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum_all(21,25,65))
print(sum_all(5))

def student_info(name,age,high,**kwargs):
    print("Name:",name)
    print("Age:",age)
    print("other",**kwargs)


def greet_all2(*args):
    for name in args:
        print("hello",name)
    return True

def power(x=2):
    return x ** 2
    print(power())
    """
    
    
    :param x:amoo 
    :return:daei 
    """




#def greet_all(name,*args):
    #name=input("what is your name?")
    #print("hello",name)
    #print("hello",args)
    #$return args