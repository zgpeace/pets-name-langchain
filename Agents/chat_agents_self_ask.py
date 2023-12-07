# 导入与 OpenAI 语言模型交互的模块。
from langchain.llms import OpenAI  

# 导入创建和管理提示模板的模块。
from langchain.prompts import PromptTemplate  

# 导入用于初始化代理和定义代理类型的模块。
from langchain.agents import initialize_agent, AgentType

# 导入创建和管理 OpenAI 聊天模型实例的类。
from langchain.chat_models import ChatOpenAI

# 导入用于定义和初始化工具的模块。
from langchain.agents import Tool

# 导入用于包装 SERP API 的实用工具。
from langchain.utilities import SerpAPIWrapper

# 导入 Langchain 的 hub 模块用于拉取预设的提示。
from langchain import hub

# 导入用于格式化代理日志的工具。
from langchain.agents.format_scratchpad import format_log_to_str

# 导入用于解析自问自答（Self-Ask）输出的解析器。
from langchain.agents.output_parsers import SelfAskOutputParser

# 导入用于执行代理的执行器。
from langchain.agents import AgentExecutor

# 从 .env 文件加载环境变量，常用于管理 API 密钥等敏感数据。
from dotenv import load_dotenv  
load_dotenv()  

# 设置 SERPAPI 的 API 密钥环境变量。
import os
os.environ["SERPAPI_API_KEY"] = 'xxx'

# 初始化 OpenAI 模型。
llm = OpenAI(temperature=0)

# 初始化 SERPAPI 包装器。
search = SerpAPIWrapper()

# 定义工具列表，包括一个中间回答工具，使用搜索功能。
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

# 从 Langchain hub 拉取预设的提示。
prompt = hub.pull("hwchase17/self-ask-with-search")

# 将 OpenAI 模型与停止标记绑定。
llm_with_stop = llm.bind(stop=["\nIntermediate answer:"])

# 定义一个智能代理，包括输入处理、格式化和输出解析。
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_log_to_str(
            x["intermediate_steps"],
            observation_prefix="\nIntermediate answer: ",
            llm_prefix="",
        ),
    }
    | prompt
    | llm_with_stop
    | SelfAskOutputParser()
)

# 初始化代理执行器，并设置为详细模式。
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 使用代理执行器处理特定查询。
agent_executor.invoke(
    {"input": "最近一届奥运会男子100米赛跑冠军的家乡是哪里？"}
)
