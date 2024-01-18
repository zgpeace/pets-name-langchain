from langchain.evaluation import load_evaluator
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

# from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
# set_debug(True)  # 启用 langchain 的调试模式

from langchain.evaluation import load_evaluator
from langchain.chat_models import ChatOpenAI

accuracy_criteria = {
    "accuracy": """
Score 1: The answer is completely unrelated to the reference.
Score 3: The answer has minor relevance but does not align with the reference.
Score 5: The answer has moderate relevance but contains inaccuracies.
Score 7: The answer aligns with the reference but has minor errors or omissions.
Score 10: The answer is completely accurate and aligns perfectly with the reference."""
}

evaluator = load_evaluator(
    "labeled_score_string",
    criteria=accuracy_criteria,
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
)
# evaluator = load_evaluator("labeled_score_string", llm=ChatOpenAI(model="gpt-3.5-turbo"))
# Correct
# eval_result = evaluator.evaluate_strings(
#     prediction="You can find them in the dresser's third drawer.",
#     reference="The socks are in the third drawer in the dresser",
#     input="Where are my socks?",
# )
# print("Correct: ", eval_result)

# Correct but lacking information
# eval_result = evaluator.evaluate_strings(
#     prediction="You can find them in the dresser.",
#     reference="The socks are in the third drawer in the dresser",
#     input="Where are my socks?",
# )
# print("Correct but lacking information >>> /n", eval_result)

# Incorrect
# eval_result = evaluator.evaluate_strings(
#     prediction="You can find them in the dog's bed.",
#     reference="The socks are in the third drawer in the dresser",
#     input="Where are my socks?",
# )
# print("Incorrect >>> /n", eval_result)

evaluator = load_evaluator(
    "labeled_score_string",
    criteria=accuracy_criteria,
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    normalize_by=10,
)

# Correct but lacking information
eval_result = evaluator.evaluate_strings(
    prediction="You can find them in the dresser.",
    reference="The socks are in the third drawer in the dresser",
    input="Where are my socks?",
)
print("Correct but lacking information >>>> ", eval_result)