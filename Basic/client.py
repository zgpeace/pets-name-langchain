from langserve import RemoteRunnable
from dotenv import load_dotenv  

load_dotenv()  

remote_chain = RemoteRunnable("http://localhost:8000/category_chain")
response = remote_chain.invoke({"text": "colors"})
print('colors >> ', response)
# >> ['red', 'blue', 'green', 'yellow', 'orange']