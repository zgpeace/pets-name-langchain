# 导入dotenv库，用于从.env文件加载环境变量
import dotenv

# 加载.env文件中的环境变量
dotenv.load_dotenv()

# 导入OpenAI模块，用于与OpenAI语言模型交互
from langchain.llms import OpenAI

# 导入SQLDatabase工具，用于与SQL数据库进行交互
from langchain.utilities import SQLDatabase

# 导入SQLDatabaseChain，用于创建一个结合了语言模型和数据库的处理链
from langchain_experimental.sql import SQLDatabaseChain

# 从指定的数据库URI创建SQL数据库实例，此处使用的是SQLite数据库
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# 创建OpenAI模型实例，设置temperature为0（完全确定性输出），并启用详细日志记录
llm = OpenAI(temperature=0, verbose=True)

# 创建SQL数据库链，结合了语言模型和数据库，用于处理基于数据库的查询
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# 使用数据库链运行查询，此处查询“有多少员工？”
db_chain.run("How many employees are there?")
