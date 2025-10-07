# variable
#print("variable")
#for i in range(5):
    #print(i)

print("-------------------------")

# boucle

#print("boucle")
#i=0
#while i < 5:
    #print(i)
    #i+=1



print("-------------------------")

print("exercice fizzbuzz")

## recuperer la valeur de l'input
## l'input doit recuperer que des nombres entre 1 et 20
## tant que différennt de Fizzbuzz on continue d'afficher l'input
## si c'est divisible par 3 Fizz
## si c'est divisible par 5 Buzz
## si c'est divisible par les deux FizzBuzz

while True:
    try :
        nombre = int(input(" Entrez un nombre entre 0 et 20 : "))
        if nombre < 0 or nombre > 20 :
            print("Entrez unn nombre entre 0 et 20, Réesayez")
            continue

        if nombre % 3 ==0 and nombre % 5 ==0 :
            print("FizzBuzz 🎉")
            break
        elif nombre % 3 ==0 :
            print("Fizz")
        elif nombre % 5 ==0 :
            print("Buzz")
        else:
            print(nombre)

        print("Essaie encore")

    except :
        print("Ce que vous avez rentré est pas unn chiffre, réessayez")


