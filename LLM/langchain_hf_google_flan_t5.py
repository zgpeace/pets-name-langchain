# 导入dotenv库，用于从.env文件加载环境变量。
# 这对于管理敏感数据，如API密钥，非常有用。
from dotenv import load_dotenv  

# 调用load_dotenv函数来加载.env文件中的环境变量。
load_dotenv()

# 从langchain库导入所需的类。
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain

# 初始化Hugging Face Hub中的语言模型。
# 这里使用的是"google/flan-t5-small"作为repo_id来指定模型。
# repo_id="meta-llama/Llama-2-7b-chat-hf"是另一个可选的模型。
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small"
)

# 创建一个简单的问答模板。
# 模板包含了问题(question)和回答(Answer)的格式。
template = """Question: {question}
              Answer: """

# 创建一个PromptTemplate对象，基于上面定义的模板和输入变量。
prompt = PromptTemplate(template=template, input_variables=["question"])

# 使用LLMChain，它是一种将提示和语言模型结合起来的方法。
# 这里将前面创建的prompt和llm（语言模型）结合起来。
llm_chain = LLMChain(
    prompt=prompt,
    llm=llm
)

# 定义一个问题.
question = "Please tell a lovely story."

# 使用llm_chain运行模型，传入问题，并打印结果。
# 这将根据提供的问题生成回答。
print(llm_chain.run({"question": question}))
