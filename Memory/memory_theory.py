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

# 导入 Langchain 库的 ChatOpenAI 类，用于与 OpenAI 聊天模型进行交互。
from langchain.chat_models import ChatOpenAI

# 导入 Langchain 库的不同提示模板类，用于构建会话提示。
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 导入 Langchain 的 LLMChain 类，用于创建语言模型链。
from langchain.chains import LLMChain

# 导入 Langchain 的 ConversationBufferMemory 类，用于存储和管理会话记忆。
from langchain.memory import ConversationBufferMemory

# 导入 dotenv 库，用于从 .env 文件加载环境变量，管理敏感数据，如 API 密钥。
from dotenv import load_dotenv  

# 调用 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

# 创建 ChatOpenAI 的实例。
llm = ChatOpenAI()

# 创建聊天提示模板，包含一个系统消息、一个聊天历史占位符和一个人类消息模板。
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with a human."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

# 创建一个会话记忆，用于存储和返回会话中的消息。
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 创建一个 LLMChain 实例，包括语言模型、提示、详细模式和会话记忆。
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)

# 使用会话链处理第一个问题，并打印回应。
response = conversation({"question": "hi"})
print(response)

# 使用相同的会话链处理第二个问题，并打印回应。
response = conversation({"question": "how are you?"})
print(response)

