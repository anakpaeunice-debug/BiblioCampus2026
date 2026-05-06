from books import ajouter_livre, lister_livres, rechercher_livre
from loans import emprunter_livre, rendre_livre
from stats import afficher_stats
from storage import charger_donnees, sauvegarder_donnees

def afficher_menu():
    donnees = charger_donnees()

    while True:
        print("\n========== BiblioCampus ==========")
        print("1. Ajouter un livre")
        print("2. Lister les livres")
        print("3. Rechercher un livre")
        print("4. Emprunter un livre")
        print("5. Rendre un livre")
        print("6. Voir les statistiques")
        print("0. Quitter")
        print("==================================")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            ajouter_livre(donnees, titre, auteur)
            sauvegarder_donnees(donnees)
            print(f"✅ Livre '{titre}' ajouté.")

        elif choix == "2":
            livres = lister_livres(donnees)
            if not livres:
                print("Aucun livre enregistré.")
            else:
                print("\n--- Liste des livres ---")
                for i, livre in enumerate(livres):
                    dispo = "✅ Disponible" if livre["disponible"] else "❌ Emprunté"
                    print(f"{i+1}. {livre['titre']} — {livre['auteur']} [{dispo}]")

        elif choix == "3":
            mot = input("Rechercher (titre ou auteur) : ").strip()
            resultats = rechercher_livre(donnees, mot)
            if not resultats:
                print("Aucun résultat trouvé.")
            else:
                for livre in resultats:
                    dispo = "✅ Disponible" if livre["disponible"] else "❌ Emprunté"
                    print(f"- {livre['titre']} — {livre['auteur']} [{dispo}]")

        elif choix == "4":
            titre = input("Titre du livre à emprunter : ").strip()
            resultat = emprunter_livre(donnees, titre)
            sauvegarder_donnees(donnees)
            print(resultat)

        elif choix == "5":
            titre = input("Titre du livre à rendre : ").strip()
            resultat = rendre_livre(donnees, titre)
            sauvegarder_donnees(donnees)
            print(resultat)

        elif choix == "6":
            afficher_stats(donnees)

        elif choix == "0":
            print("Au revoir !")
            sauvegarder_donnees(donnees)
            break

        else:
            print("Choix invalide. Réessayez.")