from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.runnables import ConfigurableField
# We add in a string output parser here so the outputs between the two are the same type
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
# Now lets create a chain with the normal OpenAI model
from langchain_community.llms import OpenAI
from operator import itemgetter

from langchain import hub
from langchain.agents import AgentExecutor, tool
from langchain.agents.output_parsers import XMLAgentOutputParser
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
set_debug(True)  # 启用 langchain 的调试模式

model = ChatOpenAI()
@tool
def search(query: str) -> str:
    """Search things about current events."""
    return "32 degrees"

tool_list = [search]
# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/xml-agent-convo")
# Logic for going from intermediate steps to a string to pass into model
# This is pretty tied to the prompt
def convert_intermediate_steps(intermediate_steps):
    log = ""
    for action, observation in intermediate_steps:
        log += (
            f"<tool>{action.tool}</tool><tool_input>{action.tool_input}"
            f"</tool_input><observation>{observation}</observation>"
        )
    return log

# Logic for converting tools to string to go in prompt
def convert_tools(tools):
    return "\n".join([f"{tool.name}: {tool.description}" for tool in tools])

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: convert_intermediate_steps(
            x["intermediate_steps"]
        ),
    }
    | prompt.partial(tools=convert_tools(tool_list))
    | model.bind(stop=["</tool_input>", "</final_answer>"])
    | XMLAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tool_list, verbose=True)
response = agent_executor.invoke({"input": "whats the weather in New york?"})

print('response >> ', response)