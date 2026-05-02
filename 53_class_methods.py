class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the class value of a is {cls.a}")
        
e=employee()

e.a=34
e.show()