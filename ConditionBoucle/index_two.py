print("FizzBuzz avec function")

def Fizz_Buzz(min_value=0, max_value=20, message_fizz="C'est Fizz", message_buzz="C'est un Buzz", message_fizzbuzz=" C'est un FizzBuzz 🎉 "):

    while True :
        try :
            min_value
            max_value
            message_fizz
            message_buzz
            message_fizzbuzz

            nombre= int(input(" Entrez un nombre entre 0 et 20 : "))
            if nombre < min_value or nombre > max_value :
                print("Le nombre non compris Veuillez réesayer.")
                continue
            if nombre % 3 == 0 and nombre % 5 == 0 :
                print(message_fizzbuzz)
                break
            elif nombre % 3 == 0 :
                print(message_fizz)
            elif nombre % 5 == 0 :
                print(message_buzz)
            else :
                print(nombre)
            
            print("tu peux le faire vasy 😏 \n")

        # pour ne capturer que les erreurs de conversion en entier. except ValueError au lieu de except juste 
        except ValueError :
            print("Ce que vous avez rentré est pas un nombre/chiffre")

        
Fizz_Buzz()
