from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.runnables import ConfigurableField

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

# from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
# set_debug(True)  # 启用 langchain 的调试模式

model = ChatOpenAI(temperature=0).configurable_fields(
    temperature=ConfigurableField(
        id="llm_temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    )
)

resposne_0 = model.invoke("pick a random number")
print('resposne_0 >> ', resposne_0)

response_09 = model.with_config(configurable={"llm_temperature": 0.9}).invoke("pick a random number")
print('response_09 >> ', response_09)

# 我们也可以在它作为链条的一部分时这样做。
prompt = PromptTemplate.from_template("Pick a random number above {x}")
chain = prompt | model
response_0 = chain.invoke({"x": 50})
print('response_0 >> ', response_0)

response_07 = chain.with_config(configurable={"llm_temperature": 0.7}).invoke({"x": 50})
print('response_07 >> ', response_07)