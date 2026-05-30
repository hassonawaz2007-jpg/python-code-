def main():
    try:
        a= int(input("hey,enter a number :"))
        print(a)
        return

    except Exception as e:
        print(e)
        return
    
    finally:
        print("hey i am inside of finally")
        
main()