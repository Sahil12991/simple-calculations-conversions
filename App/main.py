from app1.calculator import calculator
from app1.currency_converter import currency_converter
from app1.temperature_converter import temperature_converter


def main():
    ans = 'y'
    while ans == 'y':

        choice = input(""" 
1.calculator
2.currency_converter
3.temperature_converter
            :""")

        match choice:
            case '1':
                calculator(2, 4)

            case '2':
                currency_converter()

            case '3':
                temperature_converter()

            case _:
                print("invalid choice")

        ans = input("do you want to continue? y/n:  ")


if __name__ == "__main__":
    main()
