# 导入Langchain库中的OpenAI模块，该模块提供了与OpenAI语言模型交互的功能
from langchain.llms import OpenAI  

# 导入Langchain库中的PromptTemplate模块，用于创建和管理提示模板
from langchain.prompts import PromptTemplate  

# 导入Langchain库中的LLMChain模块，它允许构建基于大型语言模型的处理链
from langchain.chains import LLMChain  

# 导入dotenv库，用于从.env文件加载环境变量，这对于管理敏感数据如API密钥很有用
from dotenv import load_dotenv  

# 调用load_dotenv函数来加载.env文件中的环境变量
load_dotenv()  


# 使用OpenAI类创建一个名为llm的实例。这个实例配置了用于生成文本的模型参数。
# 模型使用的是"text-davinci-003"，这是一个高级的GPT-3模型。
# temperature设置为0.8，这决定了生成文本的随机性和创造性。
# max_tokens设置为60，限制生成文本的最大长度。
llm = OpenAI(
    model="text-davinci-003",
    temperature=0.8,
    max_tokens=60
)

# 使用llm实例的predict方法生成文本。这里的输入是一个提示，要求生成一个创新的硅谷AI科技公司的名字，
# 并提供了OpenAI、DeepMind、Google、Facebook等公司作为参考。
response = llm.predict("请给我的硅谷AI科技公司起个有创新的名字，可以参考OpenAI，DeepMind，Google，Facebook等等")

# 打印生成的响应文本，去除首尾的空格。
print(response)
