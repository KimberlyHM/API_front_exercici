def alumne_schema(fetchAlumnes):
    return {
        
        "NomAlumne": str(fetchAlumnes[1]),  # Asegúrate de que esto sea un string
        "Cicle": str(fetchAlumnes[2]),
        "Curs": str(fetchAlumnes[3]),
        "Grup": str(fetchAlumnes[4]),
        "DescAula": str(fetchAlumnes[5])  #
    }
 
            

def alumnes_schema(pelis) -> dict:
    return [alumne_schema(alumnes) for alumnes in pelis]