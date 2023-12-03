# 导入 Langchain 库中的 OpenAI 模块，用于与 OpenAI 语言模型进行交互。
from langchain.llms import OpenAI  

# 导入 Langchain 库中的 PromptTemplate 模块，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate  

# 导入 Langchain 库中的 LLMChain 模块，它允许构建基于大型语言模型的处理链。
from langchain.chains import LLMChain  

# 导入 dotenv 库，用于从 .env 文件加载环境变量，这对于管理敏感数据如 API 密钥很有用。
from dotenv import load_dotenv  

# 导入 Langchain 库中的 ChatOpenAI 类，用于创建和管理 OpenAI 聊天模型的实例。
from langchain.chat_models import ChatOpenAI

# 调用 dotenv 库的 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

# 设置一些环境变量，包括唯一的项目 ID 和 Langchain API 的相关设置。
import os
from uuid import uuid4
unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_PROJECT"] = f"Tracing word length - {unique_id}"

# 初始化 LangSmith 客户端。
from langsmith import Client
client = Client()

# 创建 ChatOpenAI 实例。
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, verbose=True)

# educaLen = llm.invoke("how many letters in the word educa?")
# print("educa count > ")
# print(educaLen)

from langchain.agents import tool

@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

tools = [get_word_length]

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very powerful assistant, but bad at calculating lengths of words.",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

from langchain.tools.render import format_tool_to_openai_function

llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIFunctionsAgentOutputParser()
)

response = agent.invoke({"input": "how many letters in the word educa?", "intermediate_steps": []})
print(response)
