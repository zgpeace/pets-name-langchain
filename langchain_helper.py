# 从langchain库中导入模块
from langchain.llms import OpenAI  # 从langchain.llms导入OpenAI模块
from langchain.prompts import PromptTemplate  # 从langchain.prompts导入PromptTemplate模块
from langchain.chains import LLMChain  # 从langchain.chains导入LLMChain模块
from dotenv import load_dotenv  # 从dotenv导入load_dotenv，用于加载环境变量
from langchain.agents import load_tools  # 从langchain.agents导入load_tools函数
from langchain.agents import initialize_agent  # 从langchain.agents导入initialize_agent函数
from langchain.agents import AgentType  # 从langchain.agents导入AgentType枚举类
from langchain.tools import WikipediaQueryRun  # 从langchain.tools导入WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper  # 从langchain.utilities导入WikipediaAPIWrapper

load_dotenv()  # 加载.env文件中的环境变量

def langchain_agent():
    llm = OpenAI(temperature=0.5)  # 创建OpenAI模型实例，设置temperature参数为0.5以调整响应的多样性
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)  # 加载wikipedia和llm-math工具，与OpenAI模型实例一起使用
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True  # 使用指定的工具、模型、agent类型和详细模式初始化agent
    )
    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"  # 使用一个提示语来运行agent进行处理
    )
    print(result)  # 打印agent的输出

# 主执行检查
if __name__ == "__main__":
    langchain_agent()  # 如果脚本是主程序，则运行langchain_agent函数
