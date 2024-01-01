from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import time
from calc_time import measure_execution_time
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_core.runnables import RunnableParallel

# print(os.environ["OPENAI_API_KEY"])
# print(os.environ["WANDOU_OPENAI_API_KEY"])

# model = ChatOpenAI()
model = ChatOpenAI(model="gpt-3.5-turbo")

chain1 = ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
chain2 = (
    ChatPromptTemplate.from_template("write a short (2 line) poem about {topic}")
    | model
)
combined = RunnableParallel(joke=chain1, poem=chain2)

# result, exec_time = measure_execution_time(chain1.invoke, {"topic": "bears"})
# print(f"执行结果: {result}")
# print(f"函数执行耗时: {exec_time} 秒")


# result, exec_time = measure_execution_time(chain2.invoke, {"topic": "bears"})
# print(f"执行结果: {result}")
# print(f"函数执行耗时: {exec_time} 秒")


# result, exec_time = measure_execution_time(combined.invoke, {"topic": "bears"})
# print(f"执行结果: {result}")
# print(f"函数执行耗时: {exec_time} 秒")

# result, exec_time = measure_execution_time(chain1.batch, [{"topic": "bears"}, {"topic": "cats"}])
# print(f"执行结果: {result}")
# print(f"函数执行耗时: {exec_time} 秒")

# result, exec_time = measure_execution_time(chain2.batch, [{"topic": "bears"}, {"topic": "cats"}])
# print(f"执行结果: {result}")
# print(f"函数执行耗时: {exec_time} 秒")

result, exec_time = measure_execution_time(combined.batch, [{"topic": "bears"}, {"topic": "cats"}, {"topic": "dogs"}])
print(f"执行结果: {result}")
print(f"函数执行耗时: {exec_time} 秒")
