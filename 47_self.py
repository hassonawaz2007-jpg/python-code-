class employee:
    language="py" #this is a class attribute
    salary=1200000
    
    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")
        
        
hassan=employee()
hassan.language="javascript" #this is an instance(onbject) aattribute
print(hassan.language,hassan.salary)
hassan.greet()
hassan.getinfo()
#employee.getinfo(hassan)