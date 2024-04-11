#slide 6
class MyClass():
    a = 10
    b = 20
    x = a + b
    
inst3 = MyClass()
inst3.a
inst3.b
inst3.x

#slide 8
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a + b

def __init__(self, a, b):
    x = a + b
    return x
        
inst1 = MyClass(10, 20)
inst1.x
#>> 30

inst2 = MyClass(1, 2)
inst2.x
#>> 3

inst3 = MyClass(5, 5)
inst3.x
#>> 10

#slide 12
type(inst1)
#>> __main__.MyClass

type(inst2)
#>> __main__.MyClass

type(inst3)
#>> __main__.MyClass

x = {'a':0}
type(x)
#>> dict

x = 'Hello world!'
type(x)
#>> str

x = [1, 2]
type(x)
#>> list

#slide 15
class HouseValues():
    def __init__(self):
        # needs three values: num bedrooms, num bathrooms, sqft
        pass
    
    def estimate_value(self):
        # use an equation of questionable accuracy that I found on a random
        # website to estimate the value based on those three parameters
        pass

    def pick_a_neighborhood(self):
        # randomly pick a modifier to multiply the value estimate by
        pass
        
#slide 18
class HouseValues():
    def __init__(self, num_bedrooms, num_baths, sqft):
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.sqft = sqft

house = HouseValues(3, 2, 1100)
house.num_bedrooms
>> 3

#slide 22
class HouseValues():
    def __init__(self, num_bedrooms, num_baths, sqft):
        num_bedrooms = num_bedrooms
        num_baths = num_baths
        sqft = sqft

house = HouseValues(3, 2, 1100)
house.num_bedrooms
#>> AttributeError: 'HouseValues' object has no attribute 'num_bedrooms'


class HouseValues():
    def __init__(self, num_bedrooms, num_baths, sqft):
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.sqft = sqft
    
    def estimate_value(self):
        #add 10% per num of bedrooms over 1
        bedroom_mod = ((self.num_bedrooms - 1) * 0.1) + 1
        
        #add 5% per num of baths over 1
        bath_mod = ((self.num_baths - 1) * 0.05) + 1
        
        self.value = (self.sqft * 400) * bedroom_mod * bath_mod
        print(f'I estimate this house will be worth ${round(self.value, 2)}')
        
house1 = HouseValues(2, 2, 950)
house1.estimate_value()

#slide 27
from numpy import random

class HouseValues():
    def __init__(self, num_bedrooms, num_baths, sqft):
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.sqft = sqft
        
    def estimate_value(self):
        #add 10% per num of bedrooms over 1
        bedroom_mod = ((self.num_bedrooms - 1) * 0.1) + 1
        
        #add 5% per num of baths over 1
        bath_mod = ((self.num_baths - 1) * 0.05) + 1
        
        n_mod = self.pick_a_neighborhood()
        
        self.value = (self.sqft * 400) * bedroom_mod * bath_mod * n_mod
        print(f'I estimate this house will be worth ${round(self.value, 2)}')
        
    def pick_a_neighborhood(self):
        value = random.normal(1, 0.1)
        if value > 1.2:
            print('Whoa, you got an expensive neighborhood!')
        elif value > 1:
            print('Fairly pricy neighborhood.')
        elif value < 1:
            print('Maybe not the nicest neighborhood.')
        return value
    
house1 = HouseValues(2, 2, 950)
house2 = HouseValues(1, 1, 700)

house1.estimate_value()
>> Fairly pricy neighborhood.
>> I estimate this house will be worth $516607.27

house2.estimate_value()
>> Maybe not the nicest neighborhood.
>> I estimate this house will be worth $273543.39
