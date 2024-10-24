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

def update_alumne(idAlumne,curs):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "update alumne SET curs = %s WHERE idAlumne = %s;"
        values=(curs,idAlumne)
        cur.execute(query,values)
        updated_recs = cur.rowcount
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_recs


def delete_alumne(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM alumne WHERE idAlumne = %s;"
        cur.execute(query,(id,))
        deleted_recs = cur.rowcount
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
        
    return deleted_recs

def list_all_alumnes(idAlumne: int):
    try:
        conn = db_client()  
        cur = conn.cursor()

        query = """
            SELECT alumne.IdAlumne, alumne.NomAlumne, alumne.Cicle, alumne.Curs, alumne.Grup,
                   aula.DescAula, aula.Edifici, aula.Pis
            FROM alumne
            JOIN aula ON alumne.IdAula = aula.IdAula
            WHERE alumne.IdAlumne = %s;
        """
        cur.execute(query, (idAlumne,))  
        alumnes = cur.fetchall()

        return alumnes

    except Exception as e:
        raise Exception(f"Error retrieving data: {e}")

    finally:
        conn.close()
