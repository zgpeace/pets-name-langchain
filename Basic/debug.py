from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_debug

from dotenv import load_dotenv  
load_dotenv()  

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
tools = load_tools(["ddg-search", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
set_debug(True)
agent.run("谁执导了 2023 年电影《奥本海默》，他们的年龄是多少？他们的年龄是多少天（假设每年 365 天）？")
