# 导入 Langchain 库中的 OpenAI 模块，用于与 OpenAI 语言模型进行交互。
from langchain.llms import OpenAI  

# 导入 Langchain 库中的 PromptTemplate 模块，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate  

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

# 导入 dotenv 库，用于从 .env 文件加载环境变量，这对于管理敏感数据如 API 密钥很有用。
from dotenv import load_dotenv  

# 导入 Langchain 库中的 ChatOpenAI 类，用于创建和管理 OpenAI 聊天模型的实例。
from langchain.chat_models import ChatOpenAI

# 调用 dotenv 库的 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  
import os
os.environ["SERPAPI_API_KEY"] = 'xxxxx'


llm = OpenAI(temperature=0)
tools = load_tools(['serpapi', 'llm-math'], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
respose = agent.run("目前市场上草莓的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？")
print(respose)

