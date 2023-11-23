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
template = """您是一位专业的水果店文案撰写员。\n
对于售价为 {price} 元的 {fruit_name} ，您能提供一个吸引人的简短描述吗？
"""

# 使用PromptTemplate类的from_template方法创建一个基于上述模板的prompt对象。
# 这个对象可以用来格式化具体的水果名称和价格。
prompt = PromptTemplate.from_template(template)
print(prompt)

# 使用OpenAI类创建一个名为llm的实例。
# 这个实例配置了用于生成文本的模型参数："text-davinci-003"是一个高级的GPT-3模型。
# temperature设置为0.5，用于控制生成文本的随机性和创造性。
# max_tokens设置为60，用于限制生成文本的最大长度。
llm = OpenAI(
    model="text-davinci-003",
    temperature=0.5,
    max_tokens=60
)

# 定义两个列表：fruits包含不同的水果名称，prices包含相应的价格。
fruits = ["葡萄", "草莓", "樱桃"]
prices = ["10", "20", "30"]

# 使用zip函数将fruits和prices中的元素配对，并在每一对元素上迭代。
for fruit, price in zip(fruits, prices):
    # 使用format方法和prompt模板生成具体的输入文本。
    # 这里将占位符替换为具体的水果名称和价格。
    input_prompt = prompt.format(price=price, fruit_name=fruit)
    # 使用llm实例生成文案描述。
    response = llm(input_prompt)
    # 打印生成的文案描述。
    print(response)

