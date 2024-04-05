# Exercice sur les classes et l'heritage

'''Création de l'objet Personne'''

class Personne:
    '''Création de l'objet personne'''
    nombre = 0 # Variable de classe globale, valeurs de départ à 0
    def __init__(self, nom, age, taille, mdp):
        '''Définition des attributs de la personne
        (string) nom : nom de la personne
        (int) age : age de la personne
        (float) taille : taille de la personne
        (string) mot_de_passe : mot de passe pour proteger les données
        '''
        self.__nom=nom
        self.__age=age
        self.__taille=taille
        self.__mot_de_passe=mdp

        Personne.nombre+=1

    def saluer(self):
        print(f'Bonjour, je m\'appelle {self.__nom}, agée de {self.__age}')
    
    def getAge(self):
        '''Renvoie l'âge'''
        return self.__age
    
    def setAge(self, age_nouveau):
        '''Définit l'âge'''
        self.__age=age_nouveau

    def __del__(self):
        print(f"l'objet {self.__nom} a été supprimé avec succés")
        Personne.nombre-=1

    def checkmdp(self, motdepasse):
        '''check du mdp saisi. s'il est correct, renvoi les données.
        S'il est incorrect, affiche un message d'erreur.'''
        
        while True:
            if motdepasse == self.__mot_de_passe:
                print('Le mot de passe est correct')
                print(f'Le nom est {self.__nom}, l\'âge est {self.__age} et la taille est {self.__taille}')
                break
            else:
                print('Mot de passe incorrect !')
                motdepasse = input("Veuillez saisir à nouveau le mot de passe : \n")
            
        
            

personne1 = Personne("Marine", 21, 1.74, 'tur')
personne = {'nom':'Marine', 'age':'21', 'taille':'1.74', 'mdp':'tur'}
print(Personne.nombre)
personne1.saluer()
print(f'Âge :{personne1.getAge()}')
personne1.setAge('22')
print(f'Nouvel âge :{personne1.getAge()}')
pass_in = str(input("Entrez le mot de passe : \n"))
personne1.checkmdp(pass_in)
# del personne1

