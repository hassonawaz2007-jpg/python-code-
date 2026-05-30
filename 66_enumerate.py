l=[1,23,2334,344]

#index=0
#for item in l:
#   index+=1
#    print(f"the item number at index{index} is {item}")

#this can be simplified using enumerate function

for index,item in enumerate(l):
    print(f"the item number at index {index} is {item}")