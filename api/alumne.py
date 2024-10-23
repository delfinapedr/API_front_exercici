def alumne_schema(fetchAlumnes):
    return {
        
        "NomAlumne": str(fetchAlumnes[0]),  
        "Cicle": str(fetchAlumnes[1]),
        "Curs": str(fetchAlumnes[2]),
        "Grup": str(fetchAlumnes[3]),
        "DescAula": str(fetchAlumnes[4])
    }
def alumnes_schema(alumnes) -> list:
    return [alumne_schema(alumne) for alumne in alumnes]