# 导入与 OpenAI 语言模型交互的模块。
from langchain.llms import OpenAI  

# 导入用于创建和管理提示模板的模块。
from langchain.prompts import PromptTemplate  

# 导入用于构建基于大型语言模型的处理链的模块。
from langchain.chains import LLMChain  

# 导入从 .env 文件加载环境变量的库。
from dotenv import load_dotenv  

# 导入创建和管理 OpenAI 聊天模型实例的类。
from langchain.chat_models import ChatOpenAI

# 加载 .env 文件中的环境变量。
load_dotenv()  

# 设置环境变量，包括项目 ID 和 Langchain API 的相关设置。
import os
from uuid import uuid4
unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_PROJECT"] = f"Tracing word length - {unique_id}"

# 初始化 LangSmith 客户端。
from langsmith import Client
client = Client()

# 创建 ChatOpenAI 实例。
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, verbose=True)

# 定义一个自定义工具，用于获取单词的长度。
from langchain.agents import tool

@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

tools = [get_word_length]

# 创建聊天提示模板。
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are very powerful assistant, but bad at calculating lengths of words."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# 将 ChatOpenAI 实例与工具绑定。
from langchain.tools.render import format_tool_to_openai_function

llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

# 定义代理。
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_function_messages(x["intermediate_steps"]),
    }
    | prompt
    | llm_with_tools
    | OpenAIFunctionsAgentOutputParser()
)

# 处理用户输入，使用代理执行循环，直到获取最终结果。
from langchain.schema.agent import AgentFinish

user_input = "how many letters in the word educa?"
intermediate_steps = []
while True:
    output = agent.invoke(
        {
            "input": user_input,
            "intermediate_steps": intermediate_steps,
        }
    )
    if isinstance(output, AgentFinish):
        final_result = output.return_values["output"]
        break
    else:
        print(f"TOOL NAME: {output.tool}")
        print(f"TOOL INPUT: {output.tool_input}")
        tool = {"get_word_length": get_word_length}[output.tool]
        observation = tool.run(output.tool_input)
        intermediate_steps.append((output, observation))
print(final_result)
