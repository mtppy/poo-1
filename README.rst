Initiatition POO
================

En **programmation orienté objet** (POO) on manipule des **objets** mais qu'est-ce qu'un objet ?

Un objet peu représenter quelque chose de la vie réelle, exemple Une bouteille d'eau. On distingue deux choses:

- Comment est l'objet (son état) 
- Ce que l'on peut faire avec l'objet

Comment est la bouteille: C'est une bouteille de 1L remplie de 20cl d'eau avec un bouchon fermé.
Ce que l'on peut faire avec une bouteille: L'ouvrir ou la fermer, la vider ou la remplir.


Les objets sont fabriqués par des **classes** que l'on a définies dans notre programme. La fabrication d'un objet 
s'appelle **l'instanciation**.  En python, on utilise le **mot clef class** pour définir une classe.

::

    class Bouteille:
         """
         Cette classe fabrique des bouteilles
         """


Et on fabrique des objets comme ceci.

::

    une_bouteille = Bouteille()
    une_autre_bouteille = Bouteille()

    print(une_bouteille)
    print(une_autre_bouteille)

       
Pour le moment notre classe Bouteille fabrique un objet sans état avec lequel on ne peut rien faire.
On va commencer par ajouter la méthode **__init_\_** à notre classe bouteille pour pouvoir initialiser 
l'état des objets créés.

::

    class Bouteille:
        """
        Cette classe fabrique des bouteilles
        """
        
        def __init__(self, contenance, contenu, ouverte):
            self.contenance = contenance
            self.contenu = contenu
            self.ouverte = ouverte


La méthode **__init_\_**, comme toutes les méthodes en python prend comme premier paramètre **self** 
qui contient l'objet. Elle va ajouter les paramètres à notre méthod.


Cette fois je peux instancier des bouteilles avec un état.

::

    une_bouteille = Bouteille(1, 0.5, True)
    print(une_bouteille)

Je peux afficher les attributs de mon objet 

::

    print(une_bouteille.contenance)
    print(une_bouteille.contenu)
    print(une_bouteille.ouverte)


Pour afficher joliment nos objets, ou peut définir la méthode **__str_\_**.

::

    class Bouteille:
        """
        Cette classe fabrique des bouteilles
        """

        def __init__(self, contenance, contenu, ouverte):
            self.contenance = contenance
            self.contenu = contenu
            self.ouverte = ouverte

        def __str__(self):
            if self.ouverte:
                string = "<Bouteille {}/{}L ouverte >"
            else:
                string = "<Bouteille {}/{}L fermée>"
            return string.format(self.contenu, self.contenance)

    une_bouteille = Bouteille(1, 0.5, True)
    print(une_bouteille)


On peut modifier l'état d'un objet en modifiant directement sont attribut mais on va
voir pourquoi ça peut poser problème:

::

    une_bouteille = Bouteille(1, 0.5, True)
    print(une_bouteille)    
    une_bouteille.contenu = 0.7 
    print(une_bouteille)
    une_bouteille.contenu = 3
    print(une_bouteille)

Que peut on dire de l'état de la bouteille ? 

Comme on peut le voir, si l'on laisse l'accès libre au attribut, l'objet peut 
se retrouver dans un état incoherent. Ce qui est source de bugs.

On va donc mettre un _ devant les noms de nos attributs, c'est une convention en Python qui signifie je ne veux pas que
l'on touche directement a ces attributs. 

Puis on va ajouter des méthodes pour modifier les attributs et faire en sorte que notre bouteille reste toujours
dans un état coherent. 

::

    class Bouteille:
        """
        Cette classe fabrique des bouteilles
        """

        def __init__(self, contenance, contenu, ouverte):
            self._contenance = contenance
            self._contenu = contenu
            self.ouverte = ouverte

        def remplir(self, quantite):
            if self._contenu + quantite > self._contenance:
                raise ValueError('La bouteille va déborder !')

            self._contenu += quantite

        def __str__(self):
            if self.ouverte:
                string = "<Bouteille {}/{}L ouverte >"
            else:
                string = "<Bouteille {}/{}L fermée>"
            return string.format(self._contenance, self._contenu)


    une_bouteille = Bouteille(1, 0.5, True)
    print(une_bouteille)    
    une_bouteille.remplir(0.3) 
    print(une_bouteille)
    une_bouteille.remplir(0.4)
    print(une_bouteille)

C'est un des principes de la POO appelé encapsulation faire en sorte que la
complexité d'un objet soit encapsulé à l'intérieur. L'objet expose des méthode
pour que l'on manipule son l'état de manière à ce qu'il reste cohérent.  


Ajouter une méthode **vider** qui met le contenue de la bouteille à 0.
cette méthode doit retourner le contenue qui a été enlevé.


Ajouter une méthode **transferer(self, autre_bouteille)** Cette méthod prendra en paramètre 
un autre objet bouteille et la videra dans l'objet courant.

De la structure de donnée à l'objet
===================================


On va transformer un script d'affichage de bulletins de notes en utilisant la POO.

Récupérer le fichier tp.py https://raw.githubusercontent.com/mtppy/poo-1/master/tp.py


1) Création de la classe Eleve
------------------------------


Actuellement, les élèves sont représentés par des dictionnaires.::

    {"prenom": "Jack", "nom": "O'Neill", "notes": []}


Créer la class *Eleve* et transformer les fonctions suivantes en méthodes

* eleves_to_str(eleve)
* eleve_ajouter_note(eleve, note)
* eleve_moyenne(eleve)

La méthode *__init_\_* de la classe *Eleve* prendra en paramètre *self*, *prenom*, *nom*.

Remplace les dictionnaires utilisés pour représenter les élèves en objet Eleve.

Avant::

    {"prenom": "Jack", "nom": "O'Neill", "notes": []},

Après::

     Eleve("Jack", "O'Neill"),


Penser à changer dans les code les endroit ou `eleve` est utilisé comme dictionnaire
`eleve['notes']` deviendra `eleve.notes`

Les appels de fonction deviendront des appels de methods:

Avant::

    eleve_ajouter_note(eleve, randint(0, 20))

Après::

    eleve.eleve_ajouter_note(randint(0, 20))


2) Création la classe responsable
---------------------------------

Actuellement, les responsables sont représentés par des dictionnaires.

::

    {"prenom": "George", "nom": "Hammond"},



Créer la classe *Responsable* et transformer les fonction suivante en méthode

* responsable_to_str(responsable)

La méthode *__init_\_* de la classe *Responsable* prendra en paramètre *self*, *prenom*, *nom*.

Remplace les dictionnaires utilisés pour représenter les responsables en objet Responsable.

Avant::

    {"prenom": "George", "nom": "Hammond"},

Après::

     Responsable("George", "Hammond"),


3) Création de la classe promotion
----------------------------------

Actuellement, les promotions sont représentés par des dictionnaires.::

    {
        "nom": "SG-1",
        "responsable": Responsable('George', 'Hammond'),
        "eleves":[
            Eleve("Jack", "O'Neill"),
            Eleve("Daniel", "Jackson"),
            Eleve("Samantha", "Carter"),
            Eleve("Teal", "C")
        ]
    }

Créer la class *Promotion* et transformer les fonctions suivantes en méthodes.

* promotion_moyenne(promotion):
* promotion_passer_controle(promotion)

La méthode *__init_\_* de la classe *Promotion* prendra en paramètre *self*, *nom*, *responsable*, *eleves*
Ne pas oublier que si promotion devient un objet, l'accès à ses attributs se feront comme ceci ``promotion.eleves``
au lieu de ``promotion['eleves']``

A la place des dictionnaires définis dans la liste **PROMOTIONS**, instacier des objets *Promotion*.

Avant::

    {
        "nom": "SG-1",
        "responsable": Responsable('George', 'Hammond'),
        "eleves":[
            Eleve("Jack", "O'Neill"),
            Eleve("Daniel", "Jackson"),
            Eleve("Samantha", "Carter"),
            Eleve("Teal", "C")
        ]
    },
    ...

Après::

    Promotion(
        "SG-1",
        Responsable('George', 'Hammond'),
        [
            Eleve("Jack", "O'Neill"),
            Eleve("Daniel", "Jackson"),
            Eleve("Samantha", "Carter"),
            Eleve("Teal", "C")
        ]
    ),
    ...

Noublier pas de changer les appels de fonction pas des appels de méthods:

* ``promotion_passer_controle(promotion)`` devient ``promotion.promotion_passer_controle()``
* ``promotion_moyenne(promotion)`` devient ``promotion.promotion_moyenne()``



4) (Bonus) Créer la classe Personne
-----------------------------------

La classe Personne sera la classe parente aux classes *Responsable* et *Eleve*

Enlever la méthod *__init_\_* dans la classes *Responsable* et copiez la dans
la class *Personne*. Transformez la méthod *__init_\_* de la class *Eleve*
comme ci-dessous::

    class Personne:
        def __init__(self, nom, prenom):
            self.nom = nom
            self.prenom = prenom


    class Eleve(Personne):
        def __init__(self, nom, prenom):
            super().__init__(nom, prenom)
            self.notes = []
    
    class Responsable(Personne):
        # ...


A votre avis, à quoi sert super() ?


5) Mega bonnus:
---------------

::

    class Eleve(Personne):
        def __init__(self, nom, prenom):
            super().__init__(nom, prenom)
            self._notes = []

        @property
        def notes:
            return list(self._notes)

Quelle est l'avantage de faire une copie de la liste des notes avant de la retourner ?

Comment s'appele ce principe qui consiste à ce qu'un objet soit toujours dans un état cohérent ?
