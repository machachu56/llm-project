from phi.vectordb.pgvector import PgVector
from phi.knowledge.json import JSONKnowledgeBase
from phi.knowledge.agent import AgentKnowledge
from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
import parser.utils.utils as utils
from phi.embedder.ollama import OllamaEmbedder
import psycopg2

#Canviar a la teva base de dades.
DB_URL = utils.readJson("db-connection")

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

# Check if the table exists
def table_exists(cur, table_name):
    query = f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = '{table_name}'
        );
    """
    cur.execute(query)
    return cur.fetchone()[0]

def excelMemoria(dadesExcel, tmpDir, OLLAMABASE, taula, afegir=False):
    utils.convertirExcelAJson(dadesExcel, tmpDir)
    knowledge_base= JSONKnowledgeBase(
        path=tmpDir,    
        vector_db=PgVector(
            db_url=DB_URL,
            table_name=f"{taula}",

            embedder=OllamaEmbedder(host=OLLAMABASE, model="nomic-embed-text", dimensions=768),
        ),
    )
    if afegir:
        knowledge_base.load(upsert=True)
    return knowledge_base

def pdfMemoria(tmpDir, OLLAMABASE, taula, afegir=False):
    knowledge_base= PDFKnowledgeBase(
        path=tmpDir,    
        vector_db=PgVector(
            db_url=DB_URL,
            table_name=f"{taula}",

            embedder=OllamaEmbedder(host=OLLAMABASE, model="nomic-embed-text", dimensions=768),
        ),
        reader=PDFReader(chunk=True)
    )
    if afegir:
        knowledge_base.load(upsert=True)
    return knowledge_base

def agentBase(OLLAMABASE, taula):
    knowledge_base= AgentKnowledge(  
        vector_db=PgVector(
            db_url=DB_URL,
            table_name=f"{taula}",

            embedder=OllamaEmbedder(host=OLLAMABASE, model="nomic-embed-text", dimensions=768),
        ),
    )
    return knowledge_base