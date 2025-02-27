enter_name = input("Enter your name: ")
enter_current_temperature = float(input("Enter current temperature: "))

if enter_current_temperature >= 30:
    print("It's too hot! Stay hydrated") #Advice given to user
elif enter_current_temperature >= 20:
    print("The weather is pleasant") #Advice given to user
elif enter_current_temperature >= 10:
    print("It's a bit chilly. Wear a sweater") #Advice given to user
elif enter_current_temperature < 10:
    print("It's very cold!. Wear a jacket") #Advice given to user



