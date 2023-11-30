# from langchain.memory import ConversationBufferMemory

# memory = ConversationBufferMemory()
# memory.chat_memory.add_user_message("hi!")
# memory.chat_memory.add_ai_message("what's up?")

# print(memory.load_memory_variables({}))

# from langchain.memory import ConversationBufferMemory

# memory = ConversationBufferMemory(memory_key="chat_history")
# memory.chat_memory.add_user_message("hi!")
# memory.chat_memory.add_ai_message("what's up?")

# print(memory.load_memory_variables({}))

# from langchain.memory import ConversationBufferMemory

# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# memory.chat_memory.add_user_message("hi!")
# memory.chat_memory.add_ai_message("what's up?")

# print(memory.load_memory_variables({}))

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
# 导入 dotenv 库，用于从 .env 文件加载环境变量，管理敏感数据，如 API 密钥。
from dotenv import load_dotenv  

# 调用 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

llm = ChatOpenAI()
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with a human."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)
respone = conversation({"question": "hi"})
print(respone)
respone = conversation({"question": "how are you?"})
print(respone)
