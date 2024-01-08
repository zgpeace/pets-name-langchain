# !pip install langchain wikipedia

from operator import itemgetter
from langchain.agents import AgentExecutor, load_tools
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts.chat import ChatPromptValue
from langchain.tools import WikipediaQueryRun
from langchain_community.chat_models import ChatOpenAI
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain_community.utilities import WikipediaAPIWrapper

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
set_debug(True)  # 启用 langchain 的调试模式

wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=10_000)
)
tools = [wiki]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个很有帮助的助手"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
llm = ChatOpenAI()

# agent = (
#     {
#         "input": itemgetter("input"),
#         "agent_scratchpad": lambda x: format_to_openai_function_messages(
#             x["intermediate_steps"]
#         ),
#     }
#     | prompt
#     | llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])
#     | OpenAIFunctionsAgentOutputParser()
# )

def condense_prompt(prompt: ChatPromptValue) -> ChatPromptValue:
    messages = prompt.to_messages()
    num_tokens = llm.get_num_tokens_from_messages(messages)
    ai_function_messages = messages[2:]
    while num_tokens > 4_000:
        ai_function_messages = ai_function_messages[2:]
        num_tokens = llm.get_num_tokens_from_messages(
            messages[:2] + ai_function_messages
        )
    messages = messages[:2] + ai_function_messages
    return ChatPromptValue(messages=messages)


agent = (
    {
        "input": itemgetter("input"),
        "agent_scratchpad": lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | condense_prompt
    | llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])
    | OpenAIFunctionsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke(
    {
        "input": "现任美国总统是谁？他们来自哪个州？他们州的州鸟是什么？那只鸟的学名是什么？"
    }
)
print('response >> ', response)
