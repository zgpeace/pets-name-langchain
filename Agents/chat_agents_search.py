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

# 这部分被注释掉，原本用于创建一个 ChatOpenAI 实例并执行一个简单的查询。
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# response = llm.invoke("how many letters in the word educa?")
# print("educa count > ")
# print(response)

# 设置一些环境变量，包括唯一的项目 ID 和 Langchain API 的相关设置。
import os
from uuid import uuid4
unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"

# 初始化 LangSmith 客户端。
from langsmith import Client
client = Client()

# 导入 Langchain 的其他必要模块和工具。
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.tools import DuckDuckGoSearchResults
from langchain.tools.render import format_tool_to_openai_function

# 从 Langchain Hub 拉取最新版本的提示。
prompt = hub.pull("wfh/langsmith-agent-prompt:latest")
print(prompt)

# 创建 ChatOpenAI 实例。
llm = ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0)

# 定义工具列表，这里使用了 DuckDuckGo 作为搜索工具。
tools = [DuckDuckGoSearchResults(name="duck_duck_go")]

# 将 ChatOpenAI 实例绑定到工具上。
llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

# 创建可运行的代理，它结合了提示、模型、工具和输出解析器。
runnable_agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_function_messages(x["intermediate_steps"]),
    }
    | prompt
    | llm_with_tools
    | OpenAIFunctionsAgentOutputParser()
)

# 创建代理执行器，用于执行代理并管理工具。
agent_executor = AgentExecutor(
    agent=runnable_agent, tools=tools, handle_parsing_errors=True
)

# 定义一系列输入问题。
inputs = [
    "What is LangChain?",
    "What's LangSmith?",
    "When was Llama-v2 released?",
    "What is the langsmith cookbook?",
    "When did langchain first announce the hub?",
]

# 批量执行输入问题，并返回结果。
results = agent_executor.batch([{"input": x} for x in inputs], return_exceptions=True)
print(results)
