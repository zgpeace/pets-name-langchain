# 导入OpenAI模块，用于与OpenAI语言模型交互
from langchain.llms import OpenAI  

# 导入PromptTemplate模块，用于创建和管理提示模板
from langchain.prompts import PromptTemplate  

# 导入ChatOpenAI类，用于创建和管理OpenAI聊天模型的实例
from langchain.chat_models import ChatOpenAI

# 导入TextLoader类，用于从文本文件加载数据
from langchain.document_loaders import TextLoader

# 导入VectorstoreIndexCreator类，用于创建和管理向量存储索引
from langchain.indexes import VectorstoreIndexCreator

# 导入dotenv库，用于加载.env文件中的环境变量
from dotenv import load_dotenv  

# 加载.env文件中的环境变量
load_dotenv()  

# 使用TextLoader加载文本文件，指定文件路径和编码格式
loader = TextLoader('./RAG/fruit.txt', encoding='utf8')

# 使用VectorstoreIndexCreator从加载的数据创建向量存储索引
index = VectorstoreIndexCreator().from_loaders([loader])

# 定义要查询的字符串
query = "草莓的好处是啥"

# 使用创建的索引执行查询
result = index.query(query)

# 打印查询结果
print(result)
