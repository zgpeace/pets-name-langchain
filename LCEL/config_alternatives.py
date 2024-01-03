from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatAnthropic, ChatOpenAI
from langchain_core.runnables import ConfigurableField

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

# from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
# set_debug(True)  # 启用 langchain 的调试模式

llm = ChatAnthropic(temperature=0.7).configurable_alternatives(
    # This gives this field an id
    # When configuring the end runnable, we can then use this id to configure this field
    ConfigurableField(id="llm"),
    # This sets a default_key.
    # If we specify this key, the default LLM (ChatOpenAI() initialized above) will be used
    default_key="anthropic",
    # This adds a new option, with name `openai` that is equal to `ChatOpenAI()`
    openai=ChatOpenAI(),
    # This adds a new option, with name `gpt4` that is equal to `ChatOpenAI(model="gpt-4")`
    gpt4=ChatOpenAI(model="gpt-4"),
    # You can add more configuration options here
)
prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
chain = prompt | llm

# We can use `.with_config(configurable={"llm": "openai"})` to specify an llm to use
chat_response = chain.with_config(configurable={"llm": "openai"}).invoke({"topic": "bears"})
print('chat_response >> ', chat_response)

# We can use `.with_config(configurable={"llm": "gpt4"})` to specify an llm to use
gpt4_response = chain.with_config(configurable={"llm": "gpt4"}).invoke({"topic": "bears"})
print('gpt4_response >> ', gpt4_response)
