from cliente import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from alumne")
    
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