from statistics import mean
from random import randint


PROMOTIONS = [
    {
        "nom": "SG-1",
        "responsable": {"prenom": "George", "nom": "Hammond"},
        "eleves":[
            {"prenom": "Jack", "nom": "O'Neill", "notes": []},
            {"prenom": "Daniel", "nom": "Jackson", "notes": []},
            {"prenom": "Samantha", "nom": "Carter", "notes": []},
            {"prenom": "Teal", "nom": "C", "notes": []},
        ]
    },
    {
        "nom": "SG-C",
        "responsable": {"prenom": "Elizabeth", "nom": "Weir"},
        "eleves":[
            {"prenom": "Janet", "nom": "Fraiser", "notes": []},
            {"prenom": "Walter", "nom": "Harriman", "notes": []},
            {"prenom": "Carolyn", "nom": "Lam", "notes": []},
            {"prenom": "Bill", "nom": "Lee", "notes": []},
        ]
    }
]


def eleves_to_str(eleve):
    """
    Retourne une chaîne de caractère à partir d'un élève
    """
    return "{} {}".format(eleve['prenom'],
                          eleve['nom'])

def responsable_to_str(responsable):
    """
    Retourne une chaîne de caractère à partir d'un responsable de 
    promotion
    """
    return "Pr. {} {}".format(responsable['prenom'],
                              responsable['nom'])

def eleve_ajouter_note(eleve, note):
    """
    Ajoute une note à un élève. Un élève ne pas avoir
    que 3 notes dans l'année.
    """
    if len(eleve['notes']) > 3:
        raise ValueError("{} a déjà 3 trimestres enregistrés".format(eleves_to_str(eleve)))
    eleve['notes'].append(note)


def eleve_moyenne(eleve):
    """
    Retourne la moyenne des notes d'un élève.
    """
    return mean(eleve['notes'])


def promotion_moyenne(promotion):
    """
    Retourne la moyenne générale de toutes les notes
    de tous les élève de la promotion
    """
    notes = []
    for eleve in promotion['eleves']:
        notes.extend(eleve['notes'])
    return mean(notes)


def promotion_passer_controle(promotion):
    """
    Faire passer un controle aux élèves de la promotion,
    une note est ajoutée à chaque élève.
    """
    for eleve in promotion['eleves']:
        eleve_ajouter_note(eleve, randint(0, 20))  



def main():
    """
    Faire passer des controles à chaque promotion et affiche 
    les bulletins de notes
    """
    for promotion in PROMOTIONS:
        promotion_passer_controle(promotion)
        promotion_passer_controle(promotion)
        promotion_passer_controle(promotion)


        lignes = '\nPromotion {}\n'.format(promotion['nom'])
        lignes += 'Responsable {}\n'.format(responsable_to_str(promotion['responsable']))
        lignes += '+--------------------+--+--+--+--------+\n'
        lignes += '|Élève               |T1|T2|T3| Moyenne|\n'
        lignes += '+--------------------+--+--+--+--------+\n'

        template = '|{eleve!s:<20}|{notes[0]:>2}|{notes[1]:>2}|{notes[2]:>2}|{moyenne:>8.2f}|\n'
        for eleve in promotion['eleves']:
            lignes += template.format(eleve=eleves_to_str(eleve),
                                      notes=eleve['notes'],
                                      moyenne=eleve_moyenne(eleve))

        lignes += '|Moyenne générale:{:>21.2f}|'.format(promotion_moyenne(promotion))

        print(lignes)


if __name__ == '__main__':
    main()
