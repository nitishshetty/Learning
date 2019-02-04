class Person:

    def __init__(self, fname, lname):
        self.fname = fname

        self.lname = lname


class EmployeesList(list):

    def search(self, name):

        matching_employees = []

        for employee in self:

            if name in employee.fname:
                matching_employees.append(employee.fname)
                print('Matched employee')
        return matching_employees


class Employee(Person):
    all_employees = EmployeesList()

    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)

        self.empid = empid

        Employee.all_employees.append(self)

    def getSalary(self):
        return 'You get Monthly salary.'

    def getBonus(self):
        return 'You are eligible for Bonus.'


class ContractEmployee(Employee):

    def getSalary(self):
        return 'You will not get Salary from Organization.'

    def getBonus(self):
        return 'You are not eligible for Bonus.'


e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('Jack1', 'simmons1', 4563421)
print(Employee.all_employees.count('jack'))

e2 = ContractEmployee('John', 'williams', 123656)

print(e1.getBonus())

print(e2.getBonus())


#########

class Employee(Person):
    all_employees = EmployeesList()

    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)

        self.__empid = empid

        Employee.all_employees.append(self)

    def getEmpid(self):
        return self.__empid


e1 = Employee('Jack', 'simmons', 456342)

print(e1.fname, e1.lname)

print(e1.getEmpid())


class A:
    def __init__(self, a=5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b=0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10


x = B()
x.f1()
print(x.a, '-', x.b)


class class1:
    a = 2

    def f1(self):
        a = 3
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')


class1().f1()
class1().f1()
class1().f1()


##########

class A:
    def __init__(self, x=5, y=4):
        self.x = x
        self.y = y

    def __str__(self):
        return 'A(x: {}, y: {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y


def f1():
    a = A(12, 3)
    b = A(3, 12)
    if (a == b):
        print(b != a)
        print(a)


a = A(12, 3)
print(a)
f1()


#######

class grandpa(object):
    pass


class father(grandpa):
    pass


class mother(object):
    pass


class child(mother, father):
    pass


print(child.__mro__)
