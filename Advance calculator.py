x = 'y' 
while (x == 'y' or x == 'Y'):

    print("1. Normal calculator\n2. Area Calculator\n3. Perimeter Calculator")
    calculator_input = int(input("Enter here: "))

    if calculator_input == 1:

        first_input = int(input("enter the number: "))
        print("Select operator + - * /")
        operator_input = input("Enter here: ")
        second_input = int(input("enter the number: "))

        def add():

            final_output = first_input+second_input
            print("Addition of " ,first_input, "and" ,second_input, "is", final_output)

        def subtraction():
            final_output = first_input-second_input
            print("Subtraction  of " ,first_input, "and" ,second_input, "is", final_output)

        def multiple():
            final_output = first_input*second_input
            print("Multiply of " ,first_input, "and" ,second_input, "is", final_output)
        
        def division():
            final_output = first_input/second_input
            print("Division  of " ,first_input, "and" ,second_input, "is", final_output)
            

        if operator_input == '+':
            add()
        elif operator_input == '-':
            subtraction()
        elif operator_input == '*':
            multiple()
        elif operator_input == '/':
            division()
        else:
            print("Enter the valid operator ")

    elif calculator_input == 2:
        print ("1. Area of Triangle\n2. Area of Square\n3. Area of circle\n4. Area of Rectangle\n5. Area of Sector\n6. Area of Parallelogram")
        Area_input = int(input("Enter here: "))
        def triangle():

            side1 = float(input("Enter first Side: "))
            side2 = float(input("Enter Second Side: "))
            side3 = float(input("Enter Third Side: "))

            s = (side1+side2+side3) /2
           
            area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5

            print("\nThe Area of the Triangle is", area)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Side = a+b+c/2")
                print("Side =",side1,"+",side2,"+",side3,"/2")
                print("Side =",s)
                print("")
                print("Area = √s*(s-a)*(s-b)*(s-c)")
                print("Area = √",s,"*(",s,"-",side1,")*(",s,"-",side2,")*(",s,"-",side3,")\n")

                print("The Area of the Triangle is", area)
            
            else:
                print("ok")

        def square():
            side = int(input("Enter the side of Square: "))
            area = side*side
            print("The Area of the Square is", area)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Area = Side * Side")
                print("Area = ",side,"*",side)

                print("The Area of the Square is", area)
            
            else:
                print("ok")

        def circle():
            radius = float(input("Enter the radius of Circle: "))
            area = 3.1415926536 * (radius*radius)
            print("The Area of the Circle is", area)
            radius1 = radius*radius

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Area = πr2")
                print("Area = π",radius,"*",radius)
                print("Area = ",radius1,"π")


                print("The Area of the Circle is", area)
            
            else:
                print("ok")

        def rectangle():
            length = int(input("Enter the length of Rectangle: "))
            width = int(input("Enter the width of Rectangle: "))
            area = length*width
            print("The Area of the Rectangle is", area)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Area = Lenght * Width")
                print("Area = ",length,"*",width)

                print("The Area of the Rectangle is", area)
            
            else:
                print("ok")

        def sector():
            radius = float(input("Enter the radius of Sector: "))
            angle = float(input("Enter the angle of Sector: "))

            area = angle/360 * 3.1415926536 * (radius*radius)
            radius1 = angle/360 * (radius*radius)
            print("The Area of the Sector is", area)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Area = A/360 * π * r2")
                print("Area = ",angle,"/360 π",radius,"*",radius)
                print("Area = ",radius1,"π")


                print("The Area of the Sector is", area)
            
            else:
                print("ok")

        def parallelogram():
            base = int(input("Enter the base of Parallelogram: "))
            height = int(input("Enter the height of Parallelogram: "))
            area = base*height
            print("The Area of the Parallelogram is", area)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Area = Base * Height")
                print("Area = ",base,"*",height)

                print("The Area of the Parallelogram is", area)
            
            else:
                print("ok")

        if Area_input == 1:
            triangle()

        elif Area_input == 2:
            square()

        elif Area_input == 3:
            circle()

        elif Area_input == 4:
            rectangle()

        elif Area_input == 5:
            sector()
        elif Area_input == 6:
            parallelogram()

    elif calculator_input == 3:
        print ("1. Perimeter of Square\n2. Perimeter of Rectangle\n3. Perimeter of Triangle\n4. Perimeter of Circle\n5. Perimeter of Sector\n6. Perimeter of Parallelogram")
        perimeter_input = int(input("Enter here: "))

        def square():
            side = int(input("Enter the side of Square: "))
            perimeter = 4 * side
            print("The Perimeter of the Square is", perimeter)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Perimeter = 4 * Side")
                print("Perimeter = 4 *",side)

                print("The Perimeter of the Square is", perimeter)
            
            else:
                print("ok")

        def rectangle():
            length = int(input("Enter the length of Rectangle: "))
            width = int(input("Enter the width of Rectangle: "))
            perimeter = 2*(length+width)
            print("The Perimeter of the Rectangle is", perimeter)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Perimeter = 2(Lenght + Width)")
                print("Perimeter = 2 *",length,"*",width)


                print("The Perimeter of the Rectangle is", perimeter)
            
            else:
                print("ok")

        def triangle():
            side = int(input("Enter the Side of Triangle: "))
            base = int(input("Enter the Base of Triangle: "))
            side2 = int(input("Enter the Side of Triangle: "))

            perimeter = side+base+side2
            print("The Perimeter of the Triangle is", perimeter)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Perimeter = Side + Base + Side")
                print("Perimeter = ",side,"+",base,"+",side2)


                print("The Perimeter of the Triangle is", perimeter)
            
            else:
                print("ok")            

        def circle():
            radius = float(input("Enter the radius of Circle: "))
            perimeter = 2 * 3.1415926536 * radius
            print("The Perimeter of the Circle is", perimeter)
            radius1 = radius*2

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Perimeter = 2πr")
                print("Perimeter = 2π *",radius)
                print("Perimeter = ",radius1,"π")


                print("The Perimeter of the Circle is", perimeter)
            
            else:
                print("ok")

        def sector():
            radius = float(input("Enter the radius of Sector: "))
            angle = float(input("Enter the angle of Sector: "))

            perimeter = 2*radius+angle/360*(2*3.1415926536*radius)
            print("The Perimeter of the Sector is", perimeter)
            radius1 = 2*radius
            radius2 = angle/360

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Perimeter = 2*r+(a/360)*2πr")
                print("Perimeter =",radius1,"+",radius2,"*",radius1,"π")
                print("Perimeter = ",radius1+radius2*radius1,"π")



                print("The Perimeter of the Sector is", perimeter)
            
            else:
                print("ok")

        def parallelogram():
            width = int(input("Enter the base of Parallelogram: "))
            height = int(input("Enter the height of Parallelogram: "))
            perimeter = (width+height)*2
            print("The Perimeter of the Parallelogram is", perimeter)

            step = input("Want to see Formula and Step? y/n: ")
            if step == 'y' or step == 'Y':


                print("Formula and Steps:\n")
                print("Perimeter = 2(Height + Width)")
                print("Perimeter = 2 *",height,"+",width)


                print("The Perimeter of the Parallelogram is", perimeter)
            
            else:
                print("ok")

        
        if perimeter_input == 1:
            square()

        elif perimeter_input == 2:
            rectangle()
        
        elif perimeter_input == 3:
            triangle()
        
        elif perimeter_input == 4:
            circle()

        elif perimeter_input == 5:
            sector()
        
        elif perimeter_input == 6:
            parallelogram()


    x = input("you want to continue y/n: ")

    if x == 'n' or x == 'N':
        print("Thanks for using")
        break

    else: 
        print("Enter valid input ")
        
