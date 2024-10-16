def alumne_schema(alumno) -> dict:
    return {"IdAlumne": alumno[0],
            "IdAula": alumno[1],
            "NomAlumne": alumno[2],
            "Cicle": alumno[3],
            "Curs": alumno[4],
            "Grup": alumno[5],
            "CreatedAt": alumno[6],
            "UpdateAt": alumno[7]  
            }

def alumnes_schema(pelis) -> dict:
    return [alumne_schema(alumnes) for alumnes in pelis]