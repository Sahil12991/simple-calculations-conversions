from calculator import calculator
from currency_converter import currency_converter

def main():
    choice = input(""" 
1.calculator
2.currency_converter
:""")
    
    match choice:
          case '1':
                calculator(2,4)

          case '2':
                currency_converter()
                
    
    


if __name__ == "__main__":
        main()