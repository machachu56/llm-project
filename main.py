from phi.model.ollama import Ollama
from phi.agent import Agent
import parser.utils.utils as utils
import parser.utils.utilsLlm as utilsLLM
import shutil


#Directori de dades (modificar settings.json)
DATA = utils.readJson("data-dir") + "/"

AFEGIR = False

#Directori temporal (modificar settings.json)
tmpDir = utils.readJson("tmp-base-folder")

#Connexió base de dades (modificar settings.json)
OLLAMABASE = utils.readJson("ollama-base")

# Llegir taula de la base de dades
taula = utils.readJson("postgres-table")

taula = taula + "-docs"

llistar = utils.llistar_directori(DATA)

knowledge_base = None

table_exists = utilsLLM.table_exists(utilsLLM.cur, taula)

if not table_exists:
    AFEGIR = True

if(utils.es_dir(DATA) == False):
    print("No s'ha trobat el directori de dades, es crea ara...")
    utils.crear_dir(DATA)
    

original_tmpDir = tmpDir
for i in llistar:
    extensio = utils.llegirExtensio(i)
    tmpDir = original_tmpDir + "-" + extensio.replace(".", "")  + "/"
    # Segons la extensió fer una cosa o una altre
    if extensio == ".xlsx":
        utils.crear_dir(tmpDir)
        knowledge_base = utilsLLM.excelMemoria(DATA + i, tmpDir, OLLAMABASE, taula=taula, afegir=AFEGIR)
        
    elif extensio == ".pdf":
        utils.crear_dir(tmpDir)
        shutil.copy(DATA + i, tmpDir + "-" + extensio)
        knowledge_base = utilsLLM.pdfMemoria(tmpDir, OLLAMABASE, taula=taula, afegir=AFEGIR)
    else:
        print("No s'ha pogut llegir l'extensió o no és compatible.")

    shutil.rmtree(tmpDir, ignore_errors=False, onerror=None)
if(llistar == []):
    print("No s'ha trobat cap arxiu a llegir, posa els fitxer a la carpeta de dades.\nEs proceedeix a la lectura de les dades guardades a la taula especificada de la base de dades")
    knowledge_base = utilsLLM.agentBase(OLLAMABASE, taula)

agent = Agent(
    model=Ollama(host=OLLAMABASE, id="llama3.1"),
    show_tool_calls=True,
    markdown=True,
    knowledge_base=knowledge_base,
    search_knowledge=True,
    add_references_to_prompt=True,
)

agent.print_response(input("Introdueix el que es vol preguntar a l'IA: "), stream=True)