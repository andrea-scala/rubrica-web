from db import get_connection
from models import Persona
"""
Questo modulo fornisce le funzioni che lavorano direttamente sul db. Nasce dalla necessità di dividere le funzionalità.
"""

def get_all(config=None):
    conn = get_connection(config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lista_contatti ORDER BY cognome, nome")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Persona(**row) for row in rows]

def get_by_id(id, config=None):
    conn = get_connection(config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lista_contatti WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return Persona(**row) if row else None

def insert(persona, config=None):
    conn = get_connection(config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO lista_contatti (nome, cognome, indirizzo, telefono, eta) VALUES (%s, %s, %s, %s, %s)",
        (persona.nome, persona.cognome, persona.indirizzo, persona.telefono, persona.eta)
    )
    conn.commit()
    cursor.close()
    conn.close()

def update(persona, config=None):
    conn = get_connection(config)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE lista_contatti SET nome=%s, cognome=%s, indirizzo=%s, telefono=%s, eta=%s WHERE id=%s",
        (persona.nome, persona.cognome, persona.indirizzo, persona.telefono, persona.eta, persona.id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete(id, config=None):
    conn = get_connection(config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lista_contatti WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
