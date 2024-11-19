Crear carpeta 'data' i posar els documents .xlsx (Excel).


# Com utilitzar

Instal·lar requisits:
`pip install -r requirements.txt`

Cal baixar postgresql si es vol utilitzar una BBDD local.
`https://www.postgresql.org/download/`

Caldrà canviar la `db_url` per la que utilitzi postgresql a l'arxiu main.py.

Per afegir noves dades a la BBDD, cal descomentar la línia: `knowledge_base.load(upsert=True)`

Programa WIP: Es millorarà en els pròxims dies.


