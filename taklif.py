class Product:
    def __init__(self, name, price, group,brand,voltage):
        self.name = name
        self.price = price
        self.group = group
        self.brand = brand
        self.voltage = voltage

    def __repr__(self):
        return f"{self.__dict__}"

    #def save(self):
        #print(f"{self.name} {self.price} {self.group} {self.brand} saved")


class User:
    def a(self):
        print("User a")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged in.")



class Electronic(Product):
    def __init__(self, name, price,brand,voltage):
        super().__init__(name,brand,price,brand,voltage)
        self.group+="-Electronic"
        self.voltage=voltage

class Laptop(Electronic):
    def __init__(self, name,brand,price,voltage,ram,cpu):
        super().__init__(name,brand,voltage,price)
        self.ram=ram
        self.cpu=cpu
        self.group+="-Laptop"


class Asus(Laptop):
    def __init__(self, name,brand,price,voltage,ram,cpu):
        super().__init__(name,brand,price,voltage,ram,cpu)
        self.group+="-Asus"

class Acer(Laptop):
    def __init__(self, name, brand, price, voltage, ram, cpu):
        super().__init__(name, brand, price, voltage, ram, cpu)
        self.group += "-Acer"

class Mobile(Electronic):
    def __init__(self, name, price, group,brand,inch):
        super().__init__(name,brand,price,group)
        self.group+="-Mobile"
        self.inch=inch
class Iphone(Mobile):
    def __init__(self, name, price, group,brand,inch):
        super().__init__(name, price, group,brand,inch)
        self.group+="-Iphone"
class Samsung(Mobile):
    pass
    def __init__(self, name, price, group,brand,inch):
        super().__init__(name, price, group,brand,inch)
        self.group+="-samsung"

class Cloth(Product):
    pass

class Food(Product):
    pass

class Health(Product):
    pass
#test asus

#asus_laptop=Asus("as123","asus",2000,234,8,"core i5")
#print(asus_laptop)

#test iphone

#iphone_mobile=Iphone("13 pro max",2000,"mobile","iphone",12)
#print(iphone_mobile)

















