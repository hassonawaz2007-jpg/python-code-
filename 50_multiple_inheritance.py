class employee:
    company = "ITC"
    name="default name"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")
        
class coder:
    language="python"
    def printlanguages(self):
        property(f"out of all languages here is your language:{self.language}")

class porogrammer(employee,coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")
            

a = employee()
b = porogrammer()

b.show()
b.printlanguages()
b.showlanguage()