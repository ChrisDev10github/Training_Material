class Person:
    """Person class"""
    def __init__(self, name):
        print('Initializing name')
        self.__name = name

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    def move(self):
        print('Moving')

class Employee(Person):
    """Employee class, inheriting from Person"""
    def __init__(self,name,id):
        super().__init__(name)
        self.__empid = id

    @property
    def EmployeeID(self):
        return self.__empid

    @EmployeeID.setter
    def name(self, new_id):
        self.__empid = new_id

    @property
    def Manager(self):
        return self.__mgr

    @Manager.setter
    def Manager(self,manager):
        self.__mgr = manager


Employee1 = Employee('Chris',1)
print(Employee1)            #doesn't word
print(Employee1.name)
print(Employee1.EmployeeID)
#Employee1.EmployeeID = 51               #doesn't word because its hidden info [cant see attribute]
#print(Employee1.EmployeeID)
Employee2 = Employee('Sam',2)
Employee2.Manager = Employee1
print(Employee2.Manager)