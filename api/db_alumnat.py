from client import db_client

def read_alumnes():
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "SELECT alumne.nomAlumne, alumne.cicle, alumne.curs, alumne.grup, aula.descAula from alumne JOIN aula ON alumne.IdAula = aula.IdAula ;"
        cur.execute(query)
        alumnes = cur.fetchall()

        return alumnes

    except Exception as e:
        return {"status": -1, "message": f"Error fetching data: {e}"}

    finally:
        conn.close()

def read_alumne_by_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "SELECT * from alumne WHERE IdAlumne = %s;"
        cur.execute(query, (id,))
        alumne = cur.fetchone()  

        return alumne

    except Exception as e:
        return {"status": -1, "message": f"Error fetching data: {e}"}

    finally:
        conn.close()

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
