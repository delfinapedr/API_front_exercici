def aula_schema(classe) -> dict:
    return {
        "IdAula": classe[0],
        "DescAula": classe[1],
        "Edifici": classe[2],
        "Pis": classe[3]
    }

def aules_schema(aules) -> list:
    return [aula_schema(aula) for aula in aules]
