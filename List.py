print ("What you want \n1. String Element \n2. Number Element")
select_input = int(input("write down the number so that we move on to the next list step: "))
if select_input == 1:
    user_input = (input("enter the value: ").split())

elif select_input == 2:
    user_input = list(map(int,input("\nEnter the numbers : ").strip().split()))
else:
    print("Enter correct number")

mylist = user_input


print(mylist)
print(type(mylist))
change_input = input("Do you want to change something? y/n: ")

def update():
    print (mylist)
    if select_input == 1:
        index_number = int(input("Enter index number to Update: "))
        value_input = input("enter the new value here: ")
        mylist[index_number] = value_input
        print(mylist)
    elif select_input ==2:
        index_number = int(input("Enter index number to Update: "))
        value_input = int(input("enter the new value here: "))
        mylist[index_number] = value_input
        print(mylist)

def append():
    if select_input == 1:
        print (mylist)
        value_input = input("enter the string to add in last: ")
        mylist.append(value_input)
        print (mylist)
    elif select_input ==2:
        print (mylist)
        value_input = int(input("enter the number to add in last: "))
        mylist.append(value_input)
        print (mylist)

def extend():
    if select_input == 1:
        print (mylist)
        value_input = input("enter the string to add : ")
        x = [value_input]
        mylist.extend(x)
        print (mylist)
    elif select_input ==2:
        print (mylist)
        value_input = int(input("enter the number to add : "))
        x = [value_input]
        mylist.extend(x)
        print (mylist)

def insert():
    if select_input == 1:
        print (mylist)
        index_number = int(input("Enter index number to insert the new value: "))
        value_input = input("enter the new string here: ")
        mylist.insert(index_number,value_input)
        print(mylist)
    elif select_input ==2:
        print (mylist)
        index_number = int(input("Enter index number to insert the new value: "))
        value_input = int(input("enter the new number here: "))
        mylist.insert(index_number,value_input)
        print(mylist)

def remove():
    print("how you want to remove the element\nusing \n1. pop method\n2. remove method")
    remove_input = int(input("Enter which method you want"))
    if remove_input == 1:
        print (mylist)
        index_number = int(input("Enter index number to remove: "))
        mylist.pop(index_number)
        print(mylist)

    elif remove_input == 2:
        if select_input == 1:
            print (mylist)
            value_input = input("enter the value to remove: ")
            mylist.remove(value_input)
            print(mylist)
        elif select_input ==2:
            print (mylist)
            value_input = int(input("enter the value to remove: "))
            mylist.remove(value_input)
            print(mylist)

    else:
        print("enter valid method: ")
        
        
def delete():
    global mylist
    print("Do you want to \n1.delete hole list \n2.delete element")
    remove_input = int(input("Enter which method you want"))
    if remove_input == 1:
        print(mylist)
        del mylist
        print(mylist)
        

    elif remove_input == 2:

        print (mylist)
        index_number = int(input("Enter index number to delete: "))
        del mylist[index_number]
        print(mylist)

    else:
        print("enter valid method: ")



if change_input == 'y':
    print("what you want to change in list")
    print("1. Update data \n2. Append the data \n3. Extend the data \n4. Insert the new value \n5. Remove\pop value \n6.Delete \n7 Check Length of dictionary ")

    take_input = int(input("Enter the number what you want to change: "))

    if take_input == 1:
        update()
    elif take_input == 2:
        append()
    elif take_input == 3:
        extend()
    elif take_input == 4:
        insert()
    elif take_input == 5:
        remove()
    elif take_input == 6:
        delete()
    elif take_input == 7:
        print(len(mylist))



    else :
        print("enter the valid number")

elif change_input == 'N' or 'n':
    print("thank have a good day")
    exit()
else:
    print("enter the valid input")
    exit()
