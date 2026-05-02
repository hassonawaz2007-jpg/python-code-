class employee:
    company = "ITC"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")
        

class porogrammer(employee):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")
            

a = employee()
b = porogrammer()

print(a.company, b.company)
        