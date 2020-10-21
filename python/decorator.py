def upper_case(func):
    def wrapper():
        result = func()
        result = result.upper()
        return result
    return wrapper


def toggle_case(func):
    def wrapper():
        result = func()
        result = result.swapcase()
        return result
    return wrapper


# pass two decorator here!
@toggle_case
@upper_case
def welcome():
    return "Hello World!"

print(welcome())


# Decorator with arguments

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper



class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello, my name is %s!" %self.name)


# inheritate --> single level inheritance

class TenYearOldPerson(Person):
    def __init__(self, name):
        Person.__init__(self, name, 10)
    
    def greet(self):
        print("I don't talk to strangers!")
    


# Multi-level Inheritance --> multi-level inheritance  --> Hierarchy of classes

class Animal():
    def __init__(self, name, food, characteristic):
        self.name = name
        self.characteristic = characteristic
        self.food = food
        print("I am a " + str(self.name) + '.')
    
class Mammal(Animal):
    def __init__(self, name, food):
        Animal.__init__(self, name, food, "warm blooded")
        print("I am warm blooded")
    
class Carnivore(Mamamal):
    def __init__(self, name):
        Mammal.__init__(self, name, "meat")
        print("I eat meat")

lion = Carnivore("lion") # lion is an instance of carnivore


# Override here --> if we implement the same method here
# we will have the override the method from the superclass

class Animal():
    def __init__(self, name, food, characteristic):
        self.name = name
        self.characteristic = characteristic
        self.food = food
    def printer(self):
        print("I am a " + str(self.name) + '.')
    
class Mammal(Animal):
    def __init__(self, name, food):
        Animal.__init__(self, name, food, "warm blooded")
    def printer(self):
        print("I am warm blooded")
    
class Carnivore(Mamamal):
    def __init__(self, name):
        Mammal.__init__(self, name, "meat")
    def printer(self):
        print("I eat meat")


class Animal():
    def __init__(self, name, food, characteristic):
        self.name = name
        self.characteristic = characteristic
        self.food = food
    def printer(self):
        print("I am a " + str(self.name) + '.')
    
class Mammal(Animal):
    def __init__(self, name, food):
        super().__init__(name, food, "warm blooded")
    def printer(self):
        print("I am warm blooded")
    
class Carnivore(Mamamal):
    def __init__(self, name):
        super().__init__(name, "meat")
    def printer(self):
        print("I eat meat")

# Inherite attributes and methods from more than one class

class Person:
    def __init__(self, name):
        self.name = name    

    def greet(self):
        print("Hi, I am " + self.name + '.')

class Student(Person):
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
        Person.__init__(self, name)

    def report(self):
        print("My roll number is " + self.rollNumber + '.')

class Teacher(Person):
    def __init__(self, name, rollNumber):
        self.name = name
        self.course = course 
        Person.__init__(self, name)

    def introduce(self):
        print("I teach" + self.course + '.')

class TA(Student, Teacher):
    def __init__(self, name, rollNumber, course, grade):
        self.name = name
        self.rollNumber = rollNumber
        self.course = course
        self.grade = grade
    
    def details(self):
        if self.grade == 'A*' or self.grade == 'A' or self.grade == "A-":
            Person.greet(self)
            Student.report(self)
            Teacher.introduce(self)
            print("I got an " + self.grade + "in" + self.course + '.')
        
        else:
            print(self.name + ", you can not apply for TAship")


ta = TA('Ali', '13K-1234', 'Data Structures' ,'A') # TA object
ta.details()



class Person(Object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hi, I am " + self.name + '.')

class Student(Person):
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
        super().__init__(name)
    
    def gree(self):
        # avoid override here
        super().greet()
        print ("I am a " + self.degree + " student.")

student = Student("Ali", "PhD")
student.greet()


# Iterator class here

class MyRange:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration

# we can use next or for loop to access the iterator!
    

class MyRange:
    def __init__(self, n):
        self.n = n
        self.stack = []

    def __iter__(self):
        return self
    
    def next(self):
        for i in range(1, self.n+1):
            if i % 2 == 0:
                value = i
                self.stack.append(i)
            else:
                i +=1 
        return self.stack
    

# generator here
def fibonacci(n):
    
    f1 = 0
    f2 = 1

    for i in range(n):
        if i < 2: 
            yield i
        else:
            f1, f2 = f2, f1+f2
            yield f2
    

import asyncio

async def my_function(argument):
    pass

result = await my_function(argument)

loop = asyncio.new_event_loop()
future = loop.create_task(my_coroutine)
loop.run_until_complete(future)
loop.close()

# create an event loop 
loop = asyncio.get_event_loop()

# run async function and wait for completion
result = loop.run_until_complete(functionName())

# close the loop
loop.close()

import asyncio
async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x ** 2
# create event loop
loop = asyncio.get_event_loop()

# run async function ans wait for completion
results = loop.run_until_complete(asyncio.gather(
    square(1),
    square(2),
    square(3))
)

print(resutls)
# close the loop
loop.close()


