def alumne_schema(fetchAlumnes):
    return {
        
        "NomAlumne": str(fetchAlumnes[0]),  # Asegúrate de que esto sea un string
        "Cicle": str(fetchAlumnes[1]),
        "Curs": str(fetchAlumnes[2]),
        "Grup": str(fetchAlumnes[3]),
        "DescAula": str(fetchAlumnes[4])  #
    }
 
            

def alumnes_schema(pelis) -> dict:
    return [alumne_schema(alumnes) for alumnes in pelis]