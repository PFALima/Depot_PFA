class Personne:
    #definição de uma classe
    ## " def "  declarar um método.
    ## para um método especial usar dois underline __
    def __init__(self,nom, prenom, age) : 
        self.nom    = nom
        self.prenom = prenom
        self.age    = age
    #définition de la méthode se_présente
    def se_presente(self):
        print(f"je m'appelle {self.nom}, {self.prenom} et j'ai {self.age} ans.")

 # Criação de uma instancia da Classe Personne
personne1=Personne("Lima", "Priscila", 34)

personne1.se_presente()