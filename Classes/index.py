print("----------------------------------------")

class Student:
    def __init__(self, nom: str, age: int, moyenne: float):
        self.nom: str = nom
        self.age: int = age
        self.moyenne: float = moyenne

    def se_presenter(self) -> None:
        print(f"je m'appelle {self.nom} j'ai {self.age} ans et j'ai une moyenne de {self.moyenne} \n")
      


Student1 = Student("Antoine", 23, 12.4)
Student2 = Student("Miki", 21, 17.4)

Student1.se_presenter()
Student2.se_presenter()



print("----------------------------------------")

# principe d'héritage en PO

class OnlineStudent(Student): # on hérite OnlineStudent de Student par conséquent de ses attributs et méthode 
    def __init__(self, nom: str, age: int, moyenne: float, plateform: str):
        super().__init__(nom, age, moyenne) # on appelle le connstructeur de la classe mère 
        self.plateform: str = plateform
    # def se_presenter(self) -> None:
    #    print("je suis un étudiant en ligne")    ce que je viens de mettre en commentaire c'est de l'override, lire la petite doc que j'ai mit dans le dossier 
    def se_connecter(self) -> None :
        print(f"{self.nom} se connecte sur {self.plateform}\n")
    

Malick = OnlineStudent("Malick", 20, 16.5, "W3C")

Malick.se_presenter()
Malick.se_connecter()