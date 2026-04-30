class employee:
    language="py" #this is a class attribute
    salary=1200000
    
    def __init__(self,name,salary,language):#dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")
    
    def getinfo(self): #dunder method which is automatically called
        print(f"the language is {self.language}. the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")
        
        
hassan=employee("hassan",1300000,"javascript")
#hassan.name="hassan"
print(hassan.name,hassan.salary,hassan.language)