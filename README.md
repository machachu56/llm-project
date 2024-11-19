Crear carpeta 'data' i posar els documents .xlsx (Excel).


# Com utilitzar

Instal·lar requisits:
`pip install -r requirements.txt`

Cal baixar postgresql si es vol utilitzar una BBDD local.
`https://www.postgresql.org/download/`

Modificar l'arxiu `settings.json` per establir diferents configuracions del programa:
- `ollama-base` IP i PORT on OLLAMA està fent-se servir
- `postgres-table` taula de la BD on es guardarà la informació, canviar al nom que vulguis, la taula tindrà aquest nom.
- `data-dir` carpeta on posar les dades, de moment només soporta .xlsx i .pdf
- `tmp-base-folder` opcional: carpeta base dels arxius temporals quan es processin.
- `db-connection`  connexió postgres en format `postgresql://USUARI:CONTRASENYA@IP:PORT/phidata-knowledge` 

Caldrà canviar la `db-connection` per que utilitzi postgresql a l'arxiu settings.json (Cal canviar el host, l'usuari, contrasenya, port, etc).

Ollama: Utilitzar les comandes `ollama pull llama3.1` i `ollama pull nomic-embed-text` assegurar-se que després de fer això ollama s'executa `ollama serve`.

Programa WIP: Es millorarà en els pròxims dies.