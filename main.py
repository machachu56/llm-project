from pathlib import Path
from shutil import rmtree
from phi.model.ollama import Ollama
import requests
from phi.agent import Agent
from phi.vectordb.pgvector import PgVector
from phi.knowledge.json import JSONKnowledgeBase
from phi.knowledge.text import TextKnowledgeBase
import parser.utils.utils as utils
from phi.embedder.ollama import OllamaEmbedder

dataExcel = "data/"

tmpDir = "tmp/"

ollamaBase = "http://127.0.0.1:11434"

utils.convertirAJson(dataExcel, tmpDir)

# Create a knowledge base from the vector store
knowledge_base= JSONKnowledgeBase(
    path=tmpDir,    
    vector_db=PgVector(
        db_url="postgresql://phidata:xtwe4DHB2ib8dY79NgXF@localhost:5432/phidata-knowledge",
        table_name="json-docs",

        embedder=OllamaEmbedder(host=ollamaBase, model="nomic-embed-text", dimensions=768),
    ),
    # 2 references are added to the prompt
)

#knowledge_base.load(upsert=True)

agent = Agent(
    model=Ollama(host=ollamaBase, id="llama3.1"),
    # Add the knowledge base to the agent
    show_tool_calls=True,
    markdown=True,
    knowledge_base=knowledge_base,
    search_knowledge=True,
    add_references_to_prompt=True,
)

#agent.knowledge.load(recreate=False)

agent.print_response("Retrieve the auto avaluation grades & co-avaluation (if existent) tell me the teacher comments if they did put a comment. Keep in mind that the grades were put by students, there might be a teacher comment, but it's not for certain in all comments.", stream=True)