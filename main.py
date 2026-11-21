from pathlib import Path
from gestion import (save_student, display_students, search_student, edit_student, delete_student)


def make_directory():
    directory = Path(__file__).parent / "university"
    directory.mkdir(exist_ok=True)
    return directory


def create_file(directory):
    file = directory / "student.txt"
    file.touch(exist_ok=True)
    return file


def menu(file):
    actions = {
        "1": save_student,
        "2": display_students,
        "3": search_student,
        "4": edit_student,
        "5": delete_student,
    }
    while True:
        print("""
        ╔══════════════════════════════════════════════════════╗
        ║                                                    ║
        ║           🎓 GESTION DES ÉTUDIANTS ISI             ║
        ║                                                    ║
        ╚══════════════════════════════════════════════════════╝
        """)
        print("Welcome into our small students management console application !")
        print("To get started, pick up an option to see the magic happen !")
        print("====================================")
        print("1. Enregistrer un nouvel étudiant")
        print("2. Afficher la liste des étudiants")
        print("3. Search un étudiant")
        print("4. Edit un étudiant")
        print("5. Supprimer un étudiant")
        print("0. Quitter l'application")
        choix = input("Votre choix : ").strip()
        if choix == "0":
            print("C'est triste de vous voir partir, A bientôt !")
            break
        elif choix in actions:
            actions[choix](file)
        else:
            print("Choix invalide. Saisissez un nombre correspondant à une des options")


if __name__ == "__main__":
    directory = make_directory()
    file = create_file(directory)
    menu(file)