from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.runnables import ConfigurableField
# We add in a string output parser here so the outputs between the two are the same type
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
# Now lets create a chain with the normal OpenAI model
from langchain_community.llms import OpenAI
from operator import itemgetter

from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_community.chat_models import ChatOpenAI

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
set_debug(True)  # 启用 langchain 的调试模式

from langchain_core.runnables import RunnablePassthrough

model = ChatOpenAI()
planner = (
    ChatPromptTemplate.from_template("生成一个关于{input}的论点。")
    | ChatOpenAI()
    | StrOutputParser()
    | {"base_response": RunnablePassthrough()}
)

arguments_for = (
    ChatPromptTemplate.from_template(
        "列出关于{base_response}的优点或积极方面"
    )
    | ChatOpenAI()
    | StrOutputParser()
)
arguments_against = (
    ChatPromptTemplate.from_template(
        "列出关于{base_response}的缺点或负面方面"
    )
    | ChatOpenAI()
    | StrOutputParser()
)

final_responder = (
    ChatPromptTemplate.from_messages(
        [
            ("ai", "{original_response}"),
            ("human", "优点:\n{results_1}\n\n缺点:\n{results_2}"),
            ("system", "根据批评生成最终回应"),
        ]
    )
    | ChatOpenAI()
    | StrOutputParser()
)

chain = (
    planner
    | {
        "results_1": arguments_for,
        "results_2": arguments_against,
        "original_response": itemgetter("base_response"),
    }
    | final_responder
)
response = chain.invoke({"input": "敏捷开发"})
print('response >> ', response)