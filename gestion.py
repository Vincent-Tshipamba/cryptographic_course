"""Module de gestion."""

from constants import FIELDS


def read_student(file):
    students = []
    for line in file.read_text(encoding="utf-8").splitlines():
        if line.strip():
            students.append(dict(zip(FIELDS, line.split(";"))))
    return students


def write_students(file, students):
    lines = [";".join(e[c] for c in FIELDS) for e in students]
    file.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def display(e):
    print(
        f"Matricule : {e['matricule']} | {e['nom']} {e['postnom']} {e['prenom']} | "
        f"Genre : {e['genre']} | Né(e) à {e['lieu_naissance']} le {e['date_naissance']} | "
        f"Promotion : {e['promotion']}"
    )


def find(students, matricule):
    for e in students:
        if e["matricule"] == matricule:
            return e
    return None


def save_student(file):
    students = read_student(file)
    matricule = input("Matricule : ").strip()
    if find(students, matricule):
        print("Erreur : ce matricule existe déjà.")
        return
    student = {"matricule": matricule}
    for field in FIELDS[1:]:
        student[field] = input(f"{field.replace('_', ' ').capitalize()} : ").strip()

    with file.open("a", encoding="utf-8") as f:
        f.write(";".join(student[c] for c in FIELDS) + "\n")
    print("Étudiant enregistré avec success !")

def display_students(file):
    students = read_student(file)
    if not students:
        print("Aucun étudiant enregistré.")
    for e in students:
        display(e)

def search_student(file):
    matricule = input("Matricule à rechercher : ").strip()
    existing_student = find(read_student(file), matricule)
    if existing_student:
        display(existing_student)
    else:
        print("Étudiant introuvable.")

def edit_student(file):
    students = read_student(file)
    e = find(students, input("Matricule de l'étudiant à modifier : ").strip())
    if not e:
        print("Étudiant introuvable.")
        return
    print("Laissez vide pour conserver la valeur actuelle.")
    for field in FIELDS[1:]:
        value = input(
            f"{field.replace('_', ' ').capitalize()} [{e[field]}] : "
        ).strip()
        if value:
            e[field] = value
    write_students(file, students)
    print("Étudiant modifié successfully !")

def delete_student(file):
    students = read_student(file)
    e = find(students, input("Matricule de l'étudiant à supprimer : ").strip())
    if not e:
        print("Étudiant introuvable.")
        return
    display(e)
    if input("Confirmer la suppression (o/n) ? ").lower() == "o":
        students.remove(e)
        write_students(file, students)
        print("Étudiant supprimé successfully.")
    else:
        print("Suppression annulée.")
