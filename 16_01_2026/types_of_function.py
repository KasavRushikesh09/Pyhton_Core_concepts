class Employee:
    company = "Apexon"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    #Instance Method
    def show_info(self):
        return f"{self.name} earns {self.salary} at {Employee.company}"

    #class method
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

    #static method
    @staticmethod
    def is_valid_salary(salary):
        return salary > 60000

e1 = Employee("Rushi",50000)
print(e1.show_info())

Employee.change_company("TCS")
print(e1.show_info())

e2 = Employee.is_valid_salary(70000)
print(e2)