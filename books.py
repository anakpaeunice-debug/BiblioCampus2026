def ajouter_livre(donnees, titre, auteur):
    livre = {
        "titre": titre,
        "auteur": auteur,
        "disponible": True
    }
    donnees["livres"].append(livre)
    return livre


def lister_livres(donnees):
    return donnees["livres"]


def rechercher_livre(donnees, mot):
    mot = mot.lower()
    resultats = []
    for livre in donnees["livres"]:
        if mot in livre["titre"].lower() or mot in livre["auteur"].lower():
            resultats.append(livre)
    return resultats