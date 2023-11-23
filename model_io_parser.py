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

# 定义一个文案模板，用于生成关于水果的描述。
# {price} 和 {fruit_name} 是占位符，稍后将被具体的价格和水果名称替换。
# {format_instructions} 是用于结构化输出的指令。
template = """您是一位专业的水果店文案撰写员。
对于售价为 {price} 元的 {fruit_name} ，您能提供一个吸引人的简短描述吗？
{format_instructions}
"""

# 使用PromptTemplate类的from_template方法创建一个基于上述模板的prompt对象。
# 这个对象可以用来格式化具体的水果名称和价格。
prompt = PromptTemplate.from_template(template)
print(prompt)

# 使用OpenAI类创建一个名为llm的实例。
# 配置使用"text-davinci-003"模型，设置温度为0.5，最大令牌数为120。
llm = OpenAI(
    model="text-davinci-003",
    temperature=0.5,
    max_tokens=120
)

# 定义水果名称和对应价格的列表。
fruits = ["葡萄", "草莓", "樱桃"]
prices = ["10", "20", "30"]

# 导入Langchain库中的StructuredOutputParser和ResponseSchema，
# 用于解析和结构化AI模型的输出。
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
response_schemas = [
    ResponseSchema(name="description", description="水果的描述文案"),
    ResponseSchema(name="reason", description="为什么要这样写这个文案")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate.from_template(template, partial_variables={"format_instructions": format_instructions})

# 创建一个Pandas DataFrame来存储结果。
import pandas as pd
df = pd.DataFrame(columns=["fruit", "price", "description", "reason"])

# 使用zip函数将水果名称和价格配对，并迭代每一对元素。
for fruit, price in zip(fruits, prices):
    # 使用format方法和prompt模板生成输入文本，替换占位符。
    input_prompt = prompt.format(price=price, fruit_name=fruit)
    # 使用llm实例生成文案描述。
    response = llm(input_prompt)
    # 解析输出并添加到DataFrame。
    parsed_output = output_parser.parse(response)
    parsed_output['fruit'] = fruit
    parsed_output['price'] = price
    df.loc[len(df)] = parsed_output

# 打印DataFrame的内容。
print(df.to_dict(orient="records"))

# 将DataFrame保存到CSV文件。
df.to_csv("fruits.csv", index=False)
