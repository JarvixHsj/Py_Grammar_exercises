class Super:

    def __init__(self, name , age):
        self.name = name
        self.age = age
        print('initialzed Super : {}'.format(self.name))

    def tell(self):
        """告诉我有关我的细节"""
        print('Name : {}, Age : {}'.format(self.name, self.age),end=' ')


class Teacher(Super):
    """代表一位教师。"""
    def __init__(self,name , age, salary):
        Super.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        Super.tell(self)
        print('Salary: {:d}'.format(self.salary))


class Student(Super):
    """代表以为学生。"""
    def __init__(self,name , age, marks):
        Super.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        Super.tell(self)
        print('Marks: {:d}'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Jarvix', 25, 75)
print()

members = [t,s]
for member in members:
    member.tell()



