# 导入 Langchain 库中的 OpenAI 模块，用于与 OpenAI 语言模型进行交互。
from langchain.llms import OpenAI  

# 导入 Langchain 库中的 PromptTemplate 模块，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate  

# 导入 Langchain 库中的 LLMChain 模块，它允许构建基于大型语言模型的处理链。
from langchain.chains import LLMChain  

# 导入 dotenv 库，用于从 .env 文件加载环境变量，这对于管理敏感数据如 API 密钥很有用。
from dotenv import load_dotenv  

# 导入 Langchain 库中的 ChatOpenAI 类，用于创建和管理 OpenAI 聊天模型的实例。
from langchain.chat_models import ChatOpenAI

# 调用 dotenv 库的 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

# 设置一些环境变量，包括唯一的项目 ID 和 Langchain API 的相关设置。
import os
from uuid import uuid4
unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "ls__xxxx" 

# 初始化 LangSmith 客户端。
from langsmith import Client
client = Client()

# 导入 Langchain 的其他必要模块和工具。
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.tools import DuckDuckGoSearchResults
from langchain.tools.render import format_tool_to_openai_function

# # 创建 ChatOpenAI 实例。
llm = ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0)

# # 定义工具列表，这里使用了 DuckDuckGo 作为搜索工具。
tools = [DuckDuckGoSearchResults(name="duck_duck_go")]

# 定义一系列输入问题。
inputs = [
    "What is LangChain?",
    "What's LangSmith?",
    "When was Llama-v2 released?",
    "What is the langsmith cookbook?",
    "When did langchain first announce the hub?",
]

# 批量执行输入问题，并返回结果。
# results = agent_executor.batch([{"input": x} for x in inputs], return_exceptions=True)
# print(results)

outputs = [
    "LangChain is an open-source framework for building applications using large language models. It is also the name of the company building LangSmith.",
    "LangSmith is a unified platform for debugging, testing, and monitoring language model applications and agents powered by LangChain",
    "July 18, 2023",
    "The langsmith cookbook is a github repository containing detailed examples of how to use LangSmith to debug, evaluate, and monitor large language model-powered applications.",
    "September 5, 2023",
]

dataset_name = f"agent-qa-{unique_id}"

dataset = client.create_dataset(
    dataset_name,
    description="An example dataset of questions over the LangSmith documentation.",
)

for query, answer in zip(inputs, outputs):
    client.create_example(
        inputs={"input": query}, outputs={"output": answer}, dataset_id=dataset.id
    )

from langchain import hub
from langchain.agents import AgentExecutor, AgentType, initialize_agent, load_tools
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.tools.render import format_tool_to_openai_function


# Since chains can be stateful (e.g. they can have memory), we provide
# a way to initialize a new chain for each row in the dataset. This is done
# by passing in a factory function that returns a new chain for each row.
def agent_factory(prompt):
    llm_with_tools = llm.bind(
        functions=[format_tool_to_openai_function(t) for t in tools]
    )
    runnable_agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )
    return AgentExecutor(agent=runnable_agent, tools=tools, handle_parsing_errors=True)

from langchain.evaluation import EvaluatorType
from langchain.smith import RunEvalConfig

evaluation_config = RunEvalConfig(
    # Evaluators can either be an evaluator type (e.g., "qa", "criteria", "embedding_distance", etc.) or a configuration for that evaluator
    evaluators=[
        # Measures whether a QA response is "Correct", based on a reference answer
        # You can also select via the raw string "qa"
        EvaluatorType.QA,
        # Measure the embedding distance between the output and the reference answer
        # Equivalent to: EvalConfig.EmbeddingDistance(embeddings=OpenAIEmbeddings())
        EvaluatorType.EMBEDDING_DISTANCE,
        # Grade whether the output satisfies the stated criteria.
        # You can select a default one such as "helpfulness" or provide your own.
        RunEvalConfig.LabeledCriteria("helpfulness"),
        # The LabeledScoreString evaluator outputs a score on a scale from 1-10.
        # You can use default criteria or write our own rubric
        RunEvalConfig.LabeledScoreString(
            {
                "accuracy": """
Score 1: The answer is completely unrelated to the reference.
Score 3: The answer has minor relevance but does not align with the reference.
Score 5: The answer has moderate relevance but contains inaccuracies.
Score 7: The answer aligns with the reference but has minor errors or omissions.
Score 10: The answer is completely accurate and aligns perfectly with the reference."""
            },
            normalize_by=10,
        ),
    ],
    # You can add custom StringEvaluator or RunEvaluator objects here as well, which will automatically be
    # applied to each prediction. Check out the docs for examples.
    custom_evaluators=[],
)

from langchain import hub

# We will test this version of the prompt
prompt = hub.pull("wfh/langsmith-agent-prompt:798e7324")
print(prompt)

import functools

from langchain.smith import (
    arun_on_dataset,
    run_on_dataset,
)

chain_results = run_on_dataset(
    dataset_name=dataset_name,
    llm_or_chain_factory=functools.partial(agent_factory, prompt=prompt),
    evaluation=evaluation_config,
    verbose=True,
    client=client,
    project_name=f"runnable-agent-test-5d466cbc-{unique_id}",
    tags=[
        "testing-notebook",
        "prompt:5d466cbc",
    ],  # Optional, adds a tag to the resulting chain runs
)

# Sometimes, the agent will error due to parsing issues, incompatible tool inputs, etc.
# These are logged as warnings here and captured as errors in the tracing UI.
print(chain_results)