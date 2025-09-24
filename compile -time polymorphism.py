class employee1():
    def name(self):
        print("Rashi is my name")
    def salary(self):
        print("3,00,000 is my salary")
    def age(self):
        print("18 is my age")
class employee2():
    def name(self):
        print("\nBird is her name")
    def salary(self):
        print("3,00,000 is her salary")
    def age(self):
        print("19 is her age")
def function(obj):
    obj.name()
    obj.salary()
    obj.age()
obj_emp1=employee1()
obj_emp2=employee2()
function(obj_emp1)
function(obj_emp2)
