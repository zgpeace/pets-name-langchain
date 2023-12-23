from typing import Optional

from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain_experimental.autonomous_agents import BabyAGI
from langchain.docstore import InMemoryDocstore
from langchain.vectorstores import FAISS
import faiss

from dotenv import load_dotenv  
load_dotenv()  

# Define your embedding model
embeddings_model = OpenAIEmbeddings()

embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

OBJECTIVE = "Write a weather report for SF today"
llm = OpenAI(temperature=0)
# Logging of LLMChains
verbose = False
# If None, will keep on going forever
max_iterations: Optional[int] = 3
baby_agi = BabyAGI.from_llm(
    llm=llm, vectorstore=vectorstore, verbose=verbose, max_iterations=max_iterations
)
baby_agi({"objective": OBJECTIVE})

