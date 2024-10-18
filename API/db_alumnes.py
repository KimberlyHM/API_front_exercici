from cliente import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                alumne.NomAlumne,
                alumne.Cicle,
                alumne.Curs,
                alumne.Grup,
                aula.DescAula
            FROM 
                alumne
            JOIN 
                aula ON alumne.IdAula = aula.IdAULA
        """)
    
        films = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return films


def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from alumne WHERE IdAlumne = %s"
        value = (id,)
        cur.execute(query,value)
    
        alumno = cur.fetchone()

        if alumno is None:
            return {"status": 0, "message": "Alumne no encontrado"}  # Si no se encuentra el alumno
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumno


def create_alumne(IdAula, NomAlumne, Cicle, Curs, Grup):
    conn = db_client()
    cur = conn.cursor()
    
    query = """
    INSERT INTO alumne (IdAula, NomAlumne, Cicle, Curs, Grup)
    VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(query, (IdAula, NomAlumne, Cicle, Curs, Grup))
    conn.commit()

    cur.execute("SELECT LAST_INSERT_ID();")
    IdAlumne = cur.fetchone()[0]

    cur.execute("SELECT * FROM alumne WHERE IdAlumne = %s", (IdAlumne,))
    new_alumne = cur.fetchone()

    conn.close()
    return new_alumne

def read_aula_by_id(id):
    conn = db_client()
    cur = conn.cursor()

    query = "SELECT * FROM aula WHERE IdAula = %s"
    cur.execute(query, (id,))
    aula = cur.fetchone()

    conn.close()
    return aula

