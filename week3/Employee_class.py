class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return (self.salary*12)
    
emp=Employee("reyan",12000)
print(f"the annual salary of reyan is{emp.annual_salary()}")
