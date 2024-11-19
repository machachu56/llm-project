Programa per fer consultes as documents, de moment es poden fer servir documents .xlsx i .pdf

# Com utilitzar

Instal·lar requisits:
`pip install -r requirements.txt`

Cal baixar PostgreSQL + una extensió si es vol utilitzar una BBDD local. Es pot fer amb docker molt fàcilment.

**Hi ha un script a la carpeta scripts/ que permet instal·lar un postgresql molt ràpidament amb la extensió necessaria.**
**Després es pot gestionar fàcilment amb pgAdmin https://www.pgadmin.org/**
**Canviar la contrasenya del postgres editant el script per més seguretat.**

Crear un usuari a postgres amb contrasenya i una nova base de dades amb un nom com cal.

Modificar l'arxiu `settings.json` per establir diferents configuracions del programa:
- `ollama-base` IP i PORT on OLLAMA està fent-se servir
- `postgres-table` taula de la BD on es guardarà la informació, canviar al nom que vulguis, la taula tindrà aquest nom.
- `data-dir` carpeta on posar les dades, de moment només soporta .xlsx i .pdf
- `tmp-base-folder` opcional: carpeta base dels arxius temporals quan es processin.
- `db-connection`  connexió postgres en format `postgresql://USUARI:CONTRASENYA@IP:PORT/NOM_BASE_DADES` 

# Ollama

Utilitzar les comandes `ollama pull llama3.1` i `ollama pull nomic-embed-text` assegurar-se que després de fer això ollama s'executa amb `ollama serve`.

Programa WIP: Es millorarà en els pròxims dies.