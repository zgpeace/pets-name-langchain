from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.runnables import ConfigurableField
from langchain_core.output_parsers import StrOutputParser
from langchain.utils.math import cosine_similarity
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

# from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
# set_debug(True)  # 启用 langchain 的调试模式

physics_template = """你是一个非常聪明的物理教授。
你擅长以简洁易懂的方式回答物理问题。
当你不知道问题的答案时，你会承认自己不知道。 

这是一个问题。:
{query}"""

math_template = """你是一个非常优秀的数学家。你擅长回答数学问题。
你之所以这么厉害，是因为你能够把难题分解成组成部分，回答这些部分，
然后把它们放在一起回答更广泛的问题。

这里有一个问题:
{query}"""

embeddings = OpenAIEmbeddings()
prompt_templates = [physics_template, math_template]
prompt_embeddings = embeddings.embed_documents(prompt_templates)


def prompt_router(input):
    query_embedding = embeddings.embed_query(input["query"])
    similarity = cosine_similarity([query_embedding], prompt_embeddings)[0]
    most_similar = prompt_templates[similarity.argmax()]
    print("用 数学 >>>>>>>>>>" if most_similar == math_template else "用 物理 >>>>>>>>")
    return PromptTemplate.from_template(most_similar)


chain = (
    {"query": RunnablePassthrough()}
    | RunnableLambda(prompt_router)
    | ChatOpenAI()
    | StrOutputParser()
)

print(chain.invoke("黑洞是什么？"))

print(">>>>>>>>>>")

print(chain.invoke("路径积分是什么？"))