# ----->> ASSIGNMENT 02 <<<----- #
##------>>> Function Section <<<<---------##
#Function-01
def userDefault():
    print("Hello user, please select which one you want to convert: \n")
    print(
        "01. Temparature Conversions (For this insert 1)\n"
        "02. Measurement Conversions (For this insert 2)\n"
    )
    givenChoice = str(errorHandle())
    return givenChoice
    
       
#Function-02
def conversionChoiceFunction(conversionChoice):
    if conversionChoice == "1":    
        # For Temparature Conversion
        conversionType(1)         
    elif conversionChoice == "2":  
        # For Measurement Conversion  
        conversionType(2)   

#Function-03
#This function is for : all conversion options
def conversionType(convertType):    
    print("\nPlease choose your choice: ")
    if convertType == 1:        
        print(
            "1. Celsius To Fahrenheit \n"
            "2. Fahrenheit To Celsius \n"
        )
       # tempConversion = int(input("Enter your choice: "))
        tempConversion = int(errorHandle())
        if tempConversion == 1 :
            conversionCalculation(tempConversion, 'Celsius', 'Fahrenheit')
        elif tempConversion == 2 :
            conversionCalculation(tempConversion, 'Fahrenheit', 'Celsius')
        else:
            print("Error !! Please enter proper choice")
    elif convertType == 2:       
        print(
            "1. Foot To Inch\n"
            "2. Inch To Foot\n"
            "3. Inch To Centimeter\n"
            "4. Centimeter To Inch\n"
            "5. Centimeter To Meter\n"
            "6. Meter To Centimeter\n"
        )        

        meaConversion = int(errorHandle())
        
        #Get all the conversion value in one Dictionary
        ConCal_Disc = {
            1 : (3, 'Foot', 'Inch'),
            2 : (4, 'Inch', 'Foot'),
            3 : (5, 'Inch', 'Centimeter'),
            4 : (6, 'Centimeter', 'Inch'),
            5 : (7, 'Centimeter', 'Meter'),
            6 : (8, 'Meter', 'Centimeter')               
        }       

        # If Prefered choice is available than continue otherwise show error massage
        if ConCal_Disc.get(meaConversion):
            conversionCalculation(ConCal_Disc[meaConversion][0], ConCal_Disc[meaConversion][1], ConCal_Disc[meaConversion][2])
        else:
            print("Error !! Please enter proper choice")

    else:
        print("Error !! Please enter proper choice")

    # To Continue Conversion
    toBeContinue(convertType)   

#Function-04
#This function is for : calculate all the conversion
def conversionCalculation(converType, fromVal, toVal):    
    #Error handling by try-except method
    try:
        givenVal = float(input("Enter " + str(fromVal) +" Value: "))        
    except (SyntaxError, ValueError):
        return 0 

    #Store all calculation one dictionary
    formula_Dic = {
        1 : round(float((givenVal * 1.8) + 32), 2),
        2 : round(float((givenVal - 32) / 1.8), 2),
        3 : round(float(givenVal * 12), 2),
        4 : round(float(givenVal / 12), 2),
        5 : round(float(givenVal * 2.54), 2),
        6 : round(float(givenVal / 2.54), 2),
        7 : round(float(givenVal / 100), 2),
        8 : round(float(givenVal * 100), 2)
    }

    # If Prefered choice is available than continue otherwise show error massage
    if formula_Dic.get(converType):
        getVal = formula_Dic.get(converType)
    else:
        print("Error !! Please enter proper choice")

    print("\n Given " + str(givenVal) + " " + fromVal + " is equal to " + str(getVal) + " " + toVal )

#Function-05
#This function is for : If User want to continue conversion
def toBeContinue(convertType):    
    if convertType == 1:
        runningConvertion = "Temparature Conversion"
        otherConType = 2
        otherConversion = "Measurement Conversion"
    else:
        runningConvertion = "Measurement Conversion"
        otherConType = 1
        otherConversion = "Temparature Conversion"
    
    print("\nDo you want to continue? Please press "+ str(convertType) + " for " + str(runningConvertion) + " or " + str(otherConType) + " for " + str(otherConversion + " or 0 for exit"))
    #conChoice = str(int(input("Enter your choice: ")))
    conChoice = str(errorHandle())
    if conChoice == "1":
        conversionType(1)
    elif conChoice == "2":
        conversionType(2)
    else:
        exit()

#Function-06
#This function is for : Error handling by try-except method
def errorHandle():    
    try:
        givenChoice = int(input("Enter your choice : "))
        return givenChoice
    except (SyntaxError, ValueError):
        return 0 

## =====>>> End Function Section <<<=======

#User default function
conversionChoice = userDefault()
if conversionChoice == "1" or conversionChoice == "2" :
    conversionChoiceFunction(conversionChoice)
else:
    print("\n   Sorry, You inserted wrong choice! Please try again\n")
    