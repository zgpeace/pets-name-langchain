# 导入 Langchain 库中的 OpenAI 模块，用于与 OpenAI 语言模型进行交互。
from langchain.llms import OpenAI  
# 导入 Langchain 库中的 PromptTemplate 模块，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate  
from langchain.agents import initialize_agent
from langchain.agents import AgentType
# 导入 Langchain 库中的 ChatOpenAI 类，用于创建和管理 OpenAI 聊天模型的实例。
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain import hub
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import SelfAskOutputParser
from langchain.agents import AgentExecutor

# 导入 dotenv 库，用于从 .env 文件加载环境变量，这对于管理敏感数据如 API 密钥很有用。
from dotenv import load_dotenv  

# 调用 dotenv 库的 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  
import os
os.environ["SERPAPI_API_KEY"] = 'xxx'

llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

prompt = hub.pull("hwchase17/self-ask-with-search")
llm_with_stop = llm.bind(stop=["\nIntermediate answer:"])
agent = (
    {
        "input": lambda x: x["input"],
        # Use some custom observation_prefix/llm_prefix for formatting
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
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke(
    {"input": "最近一届奥运会男子100米赛跑冠军的家乡是哪里？"}
)
