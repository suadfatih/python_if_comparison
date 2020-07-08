age = input("Are you a cigarette addict older than 75 years old?(Yes or No) : ")
age = age.capitalize()
chronic = input("Do you have a severe chronic disease?(Yes or No) : ")
chronic = chronic.capitalize()
immune = input("Is your immune system too weak?(Yes or No) : ")
immune = immune.capitalize()
if age == "Yes" :
    age = True
else :
    age = False
if chronic == "Yes" :
    chronic = True
else :
    chronic = False
if immune == "Yes" :
    immune = True
else:
    immune = False

risk_bool = age and chronic and immune
if risk_bool == True :
    print("You are in risky group. ")
else :
    print("You are not in risky group. ")