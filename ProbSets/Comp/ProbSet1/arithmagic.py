def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                                           "digits differ by 2 or more: ")
    if len(step_1) != 3: 
    	raise ValueError("Number must have 3-digits")
    if abs(int(step_1[0]) - int(step_1[2])) < 2:
    	raise ValueError("Number's first and last digits must differ by 2 or more")
    step_2 = input("Enter the reverse of the first number, obtained "
                                              "by reading it backwards: ")
    if int(step_2[0]) != int(step_1[2]) or int(step_2[2]) != int(step_1[0]):
    	raise ValueError("Second number is not the reverse of the first number")
    step_3 = input("Enter the positive difference of these numbers: ")
    if abs(int(step_2) - int(step_1)) != int(step_3):
    	raise ValueError("Third number is not the positive difference of the first two numbers")
    step_4 = input("Enter the reverse of the previous result: ")
    if int(step_3[0]) != int(step_4[2]) or int(step_3[2]) != int(step_4[0]):
    	raise ValueError("Fourth number is not the reverse of the third number")
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

arithmagic()