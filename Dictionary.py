mydict = {}

range_input=int(input("how many value you want to enter: "))
for i in range(range_input):
    key = input("Enter the key value: ")
    value = input("Enter the value: ")

    mydict[key] = value


print(mydict)
change_input = input("Do you want to change something? y/n: ")

def update():
    print (mydict)
    index_number = input("Enter key value to Update: ")
    value_input = input("Enter the new value here: ")
    mydict.update({ index_number: value_input})
    print(mydict)
   


def add():
    print (mydict)
    index_number = input("Enter the new key value : ")
    value_input = input("Enter the new value here: ")
    mydict[index_number] = value_input
    print(mydict)
   

def remove():
    print("how you want to remove the key and value\nusing \n1. specific key \n2. remove last one")
    remove_input = int(input("Enter which method you want"))
    if remove_input == 1:
        print (mydict)
        index_number = input("Enter the key to remove: ")
        mydict.pop(index_number)
        print(mydict)

    elif remove_input == 2:

        print (mydict)
        mydict.popitem()
        print(mydict)
        

    else:
        print("enter valid method: ")
        
        
def delete():
    global mydict
    print("Do you want to \n1.delete hole dictionary \n2.delete key")
    remove_input = int(input("Enter which method you want"))
    if remove_input == 1:
        print(mydict)
        del mydict
        print(mydict)
        

    elif remove_input == 2:

        print (mydict)
        index_number = input("Enter key value to delete: ")
        del mydict[index_number]
        print(mydict)

    else:
        print("enter valid method: ")



if change_input == 'y' or 'Y':
    print("what you want to change in dictionary")
    print("1. Update data \n2. Add new key and value \n3. pop\popitem \n4. Delete \n5. Check Length of dictionary ")

    take_input = int(input("Enter the number what you want to change: "))

    if take_input == 1:
        update()
    elif take_input == 2:
        add()
    elif take_input == 3:
        remove()
    elif take_input == 4:
        delete()
    elif take_input == 5:
        print(len(mydict))

    else :
        print("enter the valid number")

elif change_input == 'N' or 'n':
    print("thank have a good day")
    exit()
else:
    print("enter the valid input")
    exit()