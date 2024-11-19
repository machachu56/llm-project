Versió en català del README aqui.
[a CATALÀ](https://github.com/machachu56/llm-project/README_CAT.md)

Program to do queries to documents using a LLM, only .PDFs and .XLSX are supported at the moment.

# Usage

Install requirements:
`pip install -r requirements.txt`

PostgreSQL + an extension is required. This can be easily done with Docker.

**There's a script in the scripts/ folder that allows installing a postgresql server with the extension very easily.**
**Afterwards, it can be managed with pgAdmin https://www.pgadmin.org/**
**Changing the password of the postgresql script is recommended for more security.**

Create a username in postgres with a password and a new database, you can use pgAdmin to do so.

Modify the `settings.json` file to set different program settings:
- `ollama-base` IP and PORT where OLLAMA is running.
- `postgres-table` DB table where the information will be saved, change to the name you want, the table will have this name.
- `data-dir` Folder to put the data in, at the moment it only supports .xlsx and .pdf
- `tmp-base-folder` (optional) base folder for temporary files when processed.
- `db-connection` postgres connection in the format `postgresql://USER:PASSWORD@IP:PORT/NAME_DATABASE`

# Ollama

Use the commands `ollama pull llama3.1` and `ollama pull nomic-embed-text` and make sure that after doing this ollama is running with `ollama serve`.

WIP program: It will be improved in the coming days.