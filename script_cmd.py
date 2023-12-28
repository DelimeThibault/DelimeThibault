import argparse
import datetime
import os
import fileinput
import shutil

def backup_file(original_file, backup_suffix=".bak", incremental=False, backup_folder="backups", backup_prefix="backup"):
    """
    Crée une copie de sauvegarde du fichier spécifié.

    PRE: original_file (str): Chemin du fichier original à sauvegarder.
         backup_suffix (str, optional): Suffixe à ajouter au fichier de sauvegarde (par défaut ".bak").
         incremental (bool, optional): Si True, utilise une sauvegarde incrémentielle (par défaut False).
         backup_folder (str, optional): Dossier où stocker les fichiers de sauvegarde (par défaut "backups").
         backup_prefix (str, optional): Préfixe pour les fichiers de sauvegarde (par défaut "backup").
    POST: /
    Raises: Toute exception pouvant survenir lors de la création de la sauvegarde.
    """
    # Détermine le chemin complet du fichier de sauvegarde
    backup_file = os.path.join(backup_folder, os.path.basename(original_file) + backup_suffix) if incremental else os.path.join(backup_folder, f"{backup_prefix}_{os.path.basename(original_file)}{backup_suffix}")

    try:
        # Copie le fichier original vers le fichier de sauvegarde
        shutil.copyfile(original_file, backup_file)
        print(f"Une copie de sauvegarde a été créée : {backup_file}")
    except Exception as e:
        print(f"Erreur lors de la création de la sauvegarde : {e}")

def clean_backup_files(current_folder=".", backup_suffix=".bak"):
    """
    Supprime tous les fichiers de sauvegarde avec le suffixe spécifié dans le répertoire spécifié.

    PRE: current_folder (str, optional): Répertoire où supprimer les fichiers de sauvegarde (par défaut courant).
         backup_suffix (str, optional): Suffixe des fichiers de sauvegarde à supprimer (par défaut ".bak").
    POST: /
    Raises: Toute exception pouvant survenir lors de la suppression des fichiers de sauvegarde.
    """
    # Liste tous les fichiers de sauvegarde dans le répertoire spécifié
    backup_files = [f for f in os.listdir(current_folder) if f.endswith(backup_suffix)]
    
    # Supprime chaque fichier de sauvegarde
    for backup_file in backup_files:
        try:
            os.remove(os.path.join(current_folder, backup_file))
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier de sauvegarde {backup_file}: {e}")

def log_replacement(log_file, fichier, motif_recherche, motifs_remplacement, modified_lines):
    """
    Enregistre un remplacement dans un fichier journal.

    PRE: log_file (str): Chemin du fichier journal.
         fichier (str): Chemin du fichier modifié.
         ligne (int): Numéro de ligne où le remplacement a eu lieu.
         motif_recherche (str): Motif recherché.
         motifs_remplacement (list): Liste de motifs de remplacement.
    POST: /
    Raises: Toute exception pouvant survenir lors de l'écriture dans le fichier journal.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    motifs_str = ", ".join(motifs_remplacement)

    # Ajoute l'entrée de journal pour chaque ligne modifiée
    with open(log_file, 'a') as log:
        for line_number in modified_lines:
            log_entry = f"{timestamp} - Remplacement dans {fichier} (ligne {line_number}): {motif_recherche} par {motifs_str}\n"
            log.write(log_entry)

    print(f"Remplacement enregistré dans le journal des modifications.")

def create_log_folder():
    """
    Crée un dossier de journaux s'il n'existe pas.

    PRE: /
    POST: Chemin du dossier de journaux créé.
    """
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    return log_folder

def create_backup_folder():
    """
    Crée un dossier de sauvegardes s'il n'existe pas.

    PRE: /
    POST: Chemin du dossier de sauvegardes créé.
    """
    backup_folder = "backups"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    return backup_folder

def do_recherche_remplacement():
    """
    Fonction principale pour effectuer la recherche et le remplacement dans les fichiers spécifiés.

    Cette fonction utilise les arguments de ligne de commande pour configurer le comportement du script.
    Les fichiers spécifiés seront sauvegardés, puis les occurrences du motif de recherche seront remplacées
    par les motifs de remplacement dans chaque fichier.

    PRE: /
    POST: /
    Raises: FileNotFoundError: Si l'un des fichiers spécifiés n'est pas trouvé.
            Exception: Toute autre exception qui pourrait se produire pendant l'exécution.
    """
    # Configuration des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Script de recherche et remplacement dans des fichiers.")
    parser.add_argument("--extensions", nargs="+", default=["txt"], help="Extensions de fichier à prendre en compte.")
    parser.add_argument("--ignore-case", action="store_true", help="Ignorer la casse lors de la recherche.")
    parser.add_argument("--replace-all", action="store_true", help="Remplacer toutes les occurrences du motif.")
    parser.add_argument("--incremental-backup", action="store_true", help="Utiliser une sauvegarde incrémentielle")
    parser.add_argument("--backup-prefix", default="backup", help="Préfixe pour les fichiers de sauvegarde.")
    
    args = parser.parse_args()

    motifs = []
    
    # Demande à l'utilisateur de spécifier les fichiers à traiter
    while True:
        fichier = input("Entrez le chemin vers un fichier à modifier (laissez vide pour terminer) : ")
        if not fichier:
            break
        _, extension = os.path.splitext(fichier)
        # Vérifie si l'extension du fichier est prise en charge
        if extension[1:].lower() in args.extensions:
            motifs.append(fichier)
        else:
            print(f"L'extension {extension[1:]} n'est pas prise en charge. Le fichier {fichier} ne sera pas inclus.")

    if not motifs:
        print("Aucun fichier spécifié. Fin du programme.")
        return

    motif_recherche = input("Choisissez le motif à rechercher : ")
    motifs_remplacement = input("Choisissez le mot ou les mots qui remplacent le précédent (séparés par un espace) : ").split()

    log_folder = create_log_folder()
    backup_folder = create_backup_folder()

    for fichier in motifs:
        try:
            # Crée une sauvegarde du fichier
            backup_file(fichier, incremental=args.incremental_backup, backup_folder=backup_folder, backup_prefix=args.backup_prefix)

            # Effectue la recherche et le remplacement dans le fichier
            modified_lines = []
            with fileinput.FileInput(fichier, inplace=True, backup='.bak') as file:
                for i, line in enumerate(file, start=1):
                    if args.ignore_case:
                        # Remplacement insensible à la casse
                        for motif_r, motif_rep in zip([motif_recherche], motifs_remplacement):
                            line = line.replace(motif_r, str(motif_rep), -1 if args.replace_all else 1)
                        modified_lines.append(i)
                        print(line, end='')
                    else:
                        # Remplacement sensible à la casse
                        line = line.replace(motif_recherche, ' '.join(map(str, motifs_remplacement)))
                        modified_lines.append(i)
                        print(line, end='')

            # Enregistre le remplacement dans le journal des modifications
            log_file = os.path.join(log_folder, "log_replacement.txt")
            log_replacement(log_file, fichier, motif_recherche, motifs_remplacement, modified_lines)

            print(f"Opération de recherche et remplacement effectuée avec succès dans {fichier}")

        except FileNotFoundError:
            print(f"Erreur : le fichier {fichier} n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    do_recherche_remplacement()
    clean_backup_files()
