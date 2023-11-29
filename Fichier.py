# Liste des noms de fichiers à créer
noms_de_fichiers = [
    "000_GTK_000/src/00_Connexion.c",
    "000_GTK_000/src/00_Inscription.c",
    "000_GTK_000/src/00_Accueil.c",
    "000_GTK_000/src/00_Eleves.c",
    "000_GTK_000/src/00_Enseignants.c",
    "000_GTK_000/src/00_Matiere.c",
    "000_GTK_000/src/00_Notes.c",
    "000_GTK_000/src/00_Deconnexion.c",
    "000_GTK_000/include/00_Connexion.h",
    "000_GTK_000/include/00_Inscription.h",
    "000_GTK_000/include/00_Accueil.h",
    "000_GTK_000/include/00_Eleves.h",
    "000_GTK_000/include/00_Enseignants.h",
    "000_GTK_000/include/00_Matiere.h",
    "000_GTK_000/include/00_Notes.h",
    "000_GTK_000/include/00_Deconnexion.h",
    "000_GTK_000/main.c",
    "000_GTK_000/Makefile"
]

# Boucle pour créer les fichiers
for nom_fichier in noms_de_fichiers:
    # Création du fichier
    with open(nom_fichier, 'w') as fichier:
        pass  # Fichier vide, vous pouvez ajouter du contenu si nécessaire

print(f"{len(noms_de_fichiers)} fichiers ont été créés.")