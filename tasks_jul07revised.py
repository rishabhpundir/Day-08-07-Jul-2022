# 1) swap two variable value without third variable

# a = 2
# b = 4
# a,b = b,a 

# print('a = ', a)
# print('b = ', b)


# -----------------------------------------------------------------------------------------


# 2)function arguments

# # Example #1
# student_data = {'name':0, 'class_grade':0, 'Age':0, 'Marks':0}

# def report_card(student_data_dict):
#     print('-------------------STUDENT REPORT CARD-------------------')
#     for i in student_data_dict:
#         print(f'Student {i} : {student_data_dict[i]}')

# for i in student_data:
#     data = str(input(f'Enter student {i} : '))
#     student_data[i] = data

# report_card(student_data)


# # Example #2 Positional Arguements

# def morning_wish(msg, name):
#     print(f'{msg} {name}, Suprabhat.')

# morning_wish('Hello!', 'Rishabh')


# # Example #3 keyword arguements

# def jar(item, count):
#     print(f'The number of {item} in the jar are {count}.')

# jar(item='cookies', count=17)
# jar(count=293, item='marbles')


# -----------------------------------------------------------------------------------------


# 3) Decorators 

# # example #1 simple decorator

# def decorator_func(func_name):
#     def inner_func():
#         print(f'Executing {func_name.__name__} function!')
#         func_name()
#         print('Finished execution!')

#     return inner_func

# @decorator_func
# def printer():
#     print('Hello! There.')

# printer()


# # example #2 decorator func with arguements

# def smart_divide(func):
#     def inner(a, b):
#         print(f'Dividing {a} by {b}')
#         if b == 0:
#             print(f'Cannot divide {a} by 0!')
#             return
#         return func(a, b)
    
#     return inner

# @smart_divide
# def divide(a, b):
#     return a/b

# # print(divide(5, 2))
# print(divide(2, 0))


# # example #3 multiple decorators

# def star(func):
#     def inner(arg):
#         print('*'*43)
#         func(arg)
#         print('*'*43)
#     return inner

# def pound(func):
#     def inner(arg):
#         print('#'*43)
#         func(arg)
#         print('#'*43)
#     return inner

# @star
# @pound
# def printer(msg):
#     print(msg)

# printer("Hello! There. Its a beautiful day isn't it?")


# -----------------------------------------------------------------------------------------


# 4) Abstraction

# # # example #1
# from abc import ABC, abstractmethod

# class Abstrct(ABC):
#     @abstractmethod
#     def printer(self):
#         pass

#     def greet(self):
#         print('Hello')

# class NormalClass1(Abstrct):
#     def printer(self):
#         print("Normal Class 1 printer running...")

# class NormalClass2(Abstrct):
#     def printer(self):
#         print("Normal Class 2 printer running...")

# class NormalClass3(Abstrct):
#     def printer(self):
#         print("Normal Class 3 printer running...")

# normal1_obj = NormalClass1()
# normal2_obj = NormalClass2()
# normal3_obj = NormalClass3()
# normal1_obj.printer()
# normal2_obj.printer()
# normal3_obj.printer()
# normal3_obj.greet()


# # example #2
# class parent(ABC):
#     @abstractmethod
#     def printer(self):
#         print('Abstract Class printer function ran...')

# class child(parent):
#     def printer(self):
#         super().printer()
#         print('Child Class printer function ran...')

# child_obj = child()
# child_obj.printer()
# print(issubclass(child, parent))
# print(isinstance(child(), parent))
# # c = parent() # throws error


# -----------------------------------------------------------------------------------------


# 5) Encapsulation

# ACCESSING PUBLIC MEMBERS

# class pub_mod:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def Age(self):
#         print('Age is : ', self.age)

# obj = pub_mod('Rishabh', 25)
# obj.Age()
# print(obj.name)


# # PRIVATE MEMBERS

# class Measurements:
#     __length = 0
#     __breadth = 0

#     def __init__(self):
#         self.__length = 5
#         self.__breadth = 3

#     def area(self):
#         print(self.__length * self.__breadth)


# obj = Measurements()
# # print(obj.__length) #Throws error
# obj.area() #accessible within the class itself only


# PROTECTED MEMBERS

# class Measurements:
#     _length = 0
#     _breadth = 0

# class Area(Measurements):
#     def __init__(self):
#         print(self._length)
#         print(self._breadth)
    
#     def area(self):
#         self._length = 4
#         self._breadth = 6
#         print(self._length * self._breadth)

# obj = Area()
# print(obj._length) #Throws error
# obj.area()
# print(obj._breadth)


# -----------------------------------------------------------------------------------------


# # 6) static method

# class Dates:
#     def __init__(self, date):
#         self.date = date

#     def getDate(self):
#         return self.date

#     @staticmethod
#     def toDashDate(date):
#         return date.replace('/', '-')

# date = Dates('08-07-2022')
# dateFromDB = '08/07/2022'
# dateWithDash = Dates.toDashDate(dateFromDB)

# if(date.getDate() == dateWithDash):
#     print('Dates are Equal.')
# else:
#     print('Dates are Unequal.')


# -----------------------------------------------------------------------------------------



    
