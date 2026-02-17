def temperature_converter():
    choice = input("""
1. celsius to fahrenheit
2. fahrenheit to celsius
:""")
    match choice:
        case '1':
            celcious = int(input("enter celcious:  "))
            print(celcious*9/5+32)

        case '2':
            fahrenheit = int(input("enter fahrenheit:  "))
