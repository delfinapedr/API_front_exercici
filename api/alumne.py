def alumne_schema(student) -> dict:
    return {
        "IdAlumne": student[0],
        "IdAula": student[1],
        "NomAlumne": student[2],
        "Cicle": student[3],
        "Curs": student[4],
        "Grup": student[5],
        "DescAula": student[6]
    }

def alumnes_schema(alumnes) -> list:
    return [alumne_schema(alumne) for alumne in alumnes]