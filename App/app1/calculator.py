def calculator(a,b):
    choice = input("""enter an opertion:
                       +,-,/,*
                       """)
    match choice:
        case '+':
            print(a+b)

        case '-':
            print(a-b)

        case '/':
            print(a/b)

        case '*':
            print(a*b)

