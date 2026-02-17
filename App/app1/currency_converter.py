def currency_converter():
   choice = input(""" 
1. inr to usd:
2. usd to inr:
:""") 
   
   
   match choice:
      case '1':
        inr = int(input("enter inr:"))
        print(inr/90)

      case '2':
        usd = int(input("enter usd:"))
        print(usd*90)   
