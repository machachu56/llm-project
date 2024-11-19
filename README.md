Crear carpeta 'data' i posar els documents .xlsx (Excel).


# Com utilitzar

Instal·lar requisits:
`pip install -r requirements.txt`

Cal baixar postgresql si es vol utilitzar una BBDD local.
`https://www.postgresql.org/download/`

Caldrà canviar la `db_url` per la que utilitzi postgresql a l'arxiu main.py (Cal canviar el host, l'usuari, contrasenya, port, etc).

Ollama: Utilitzar les comandes `ollama pull llama3.1` i `ollama pull nomic-embed-text` assegurar-se que després de fer això ollama s'executa `ollama serve`.

Per afegir noves dades a la BBDD, cal descomentar la línia: `knowledge_base.load(upsert=True)`

Programa WIP: Es millorarà en els pròxims dies.