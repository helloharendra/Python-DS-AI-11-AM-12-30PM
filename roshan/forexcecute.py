try:
    cardnumber=(input('enter your card number'))
    if len(cardnumber)==16:
        print('valid card number')
        cvv=(input('enter your cvv'))
        if len(cvv)==3:
            print('valid cvv')
            otp=(input('enter your otp'))
            if len(otp)==4:
               print('valid otp')
               card_pin=(input('enter your card pin'))
               if len(card_pin)==4:
                 print('valid card_pin transcation successful')
               else:
                  print('wrong pin please enter valid pin')
            else:
                print('wrong otp please enter valid otp')
        else:
            print('wrong cvv please enter valid cvv')
    else:
        print('wrong card number please valid card number')
except ValueError:
    print("please enter valid input")
finally:
     print("excecution completed")
   