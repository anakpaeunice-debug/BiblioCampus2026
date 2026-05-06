def afficher_stats(donnees):
    livres = donnees["livres"]
    emprunts = donnees["emprunts"]

    total = len(livres)
    disponibles = len([l for l in livres if l["disponible"]])
    empruntes = total - disponibles
    total_emprunts = len(emprunts)
    rendus = len([e for e in emprunts if e["statut"] == "rendu"])

    print("\n======= 📊 Statistiques BiblioCampus =======")
    print(f"  📚 Total livres enregistrés : {total}")
    print(f"  ✅ Livres disponibles        : {disponibles}")
    print(f"  ❌ Livres empruntés          : {empruntes}")
    print(f"  🔄 Total emprunts effectués  : {total_emprunts}")
    print(f"  🔁 Livres rendus             : {rendus}")
    print("============================================\n")