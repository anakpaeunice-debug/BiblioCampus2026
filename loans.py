def emprunter_livre(donnees, titre):
    for livre in donnees["livres"]:
        if livre["titre"].lower() == titre.lower():
            if livre["disponible"]:
                livre["disponible"] = False
                donnees["emprunts"].append({"titre": titre, "statut": "emprunté"})
                return f"✅ Livre '{titre}' emprunté avec succès."
            else:
                return f"❌ Le livre '{titre}' est déjà emprunté."
    return f"❌ Livre '{titre}' introuvable."


def rendre_livre(donnees, titre):
    for livre in donnees["livres"]:
        if livre["titre"].lower() == titre.lower():
            if not livre["disponible"]:
                livre["disponible"] = True
                for emprunt in donnees["emprunts"]:
                    if emprunt["titre"].lower() == titre.lower():
                        emprunt["statut"] = "rendu"
                return f"✅ Livre '{titre}' rendu avec succès."
            else:
                return f"⚠️ Ce livre n'était pas emprunté."
    return f"❌ Livre '{titre}' introuvable."