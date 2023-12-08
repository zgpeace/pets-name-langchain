from langchain.llms import OpenAI  # 导入Langchain库的OpenAI模块，提供与OpenAI模型的交互功能
from langchain.prompts import PromptTemplate  # 导入用于创建和管理提示模板的模块
from langchain.chains import LLMChain  # 导入用于构建基于大型语言模型的处理链的模块
from dotenv import load_dotenv  # 导入dotenv库，用于从.env文件加载环境变量，管理敏感数据如API密钥
from langchain.chat_models import ChatOpenAI  # 导入用于创建和管理OpenAI聊天模型的类
from langchain.agents import AgentType, initialize_agent, load_tools  # 导入用于初始化智能代理和加载工具的函数
from langchain.utilities import ArxivAPIWrapper  # 导入Arxiv API的包装器，用于与Arxiv数据库交互

load_dotenv()  # 调用dotenv函数加载.env文件中的环境变量

llm = ChatOpenAI(temperature=0.0)  # 创建一个温度参数为0.0的OpenAI聊天模型实例，温度0意味着输出更确定性
tools = load_tools(["arxiv"])  # 加载Arxiv工具，以便代理可以访问Arxiv数据库信息

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,  # 初始化一个智能代理，使用零次学习的方式来根据描述做出反应
)

paper = "2307.05782"
response = agent_chain.run("请描述论文的主要内容 " + paper)  # 运行代理链，获取指定论文ID的内容描述
print(response)  # 打印论文描述的响应

arxiv = ArxivAPIWrapper()
docs = arxiv.run(paper)  # 使用Arxiv API获取特定论文的详细信息
print(docs)  # 打印论文的详细信息

author = arxiv.run("Michael R. Douglas")  # 使用Arxiv API获取指定作者的信息
print(author)  # 打印作者信息

nondocs = arxiv.run("1605.08386WWW")  # 尝试使用一个非标准格式的ID来获取信息，可能无法正确检索
print(nondocs)  # 打印这次非标准检索的结果
