from langchain.evaluation import load_evaluator
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

# from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
# set_debug(True)  # 启用 langchain 的调试模式

# from langchain.evaluation import load_evaluator
# evaluator = load_evaluator("criteria", criteria="conciseness")

# This is equivalent to loading using the enum
from langchain.evaluation import EvaluatorType

question = "What is the capital of the US?"
evaluator = load_evaluator("labeled_criteria", criteria="correctness")

# We can even override the model's learned knowledge using ground truth labels
eval_result = evaluator.evaluate_strings(
    input="What is the capital of the US?",
    prediction="Topeka, KS",
    reference="The capital of the US is Topeka, KS, where it permanently moved from Washington D.C. on May 16, 2023",
)
print(f'With ground truth: {eval_result["score"]}')
print('eval_result >> ', eval_result)

from langchain.evaluation import Criteria
# For a list of other default supported criteria, try calling `supported_default_criteria`
list_criteria = list(Criteria)
print('list_criteria >> ', list_criteria)

prompt = ChatPromptTemplate.from_template(
    "{topic}"
)
output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | model
    | output_parser
)
response = chain.invoke(question)
print('response >> ', response)