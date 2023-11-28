# 导入 Langchain 库的 OpenAI 模块，用于与 OpenAI 的 GPT-3 模型进行交互。
from langchain.llms import OpenAI  

# 导入 PromptTemplate 模块，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate  

# 导入输出解析器，用于解析生成文本的格式。
from langchain.output_parsers import CommaSeparatedListOutputParser  

# 导入 dotenv 库，用于从 .env 文件加载环境变量，管理敏感数据，如 API 密钥。
from dotenv import load_dotenv  

# 调用 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

# 创建一个 OpenAI 类的实例，用于生成文本。
# 指定使用的模型是 "text-davinci-003"，这是一个高级的 GPT-3 模型。
# 设置 temperature 参数，影响文本生成的随机性和创造性。
# 设置 max_tokens，限制生成文本的最大长度。
llm = OpenAI(
    model="text-davinci-003",
    temperature=0.7,
    max_tokens=600
)

# 创建一个输出解析器实例，专门用于解析逗号分隔的列表。
output_parser = CommaSeparatedListOutputParser()

# 获取格式化指令，用于在提示模板中指定输出格式。
format_instructions = output_parser.get_format_instructions()

# 创建一个提示模板实例。
# 模板包含了生成特定主题列表的指令，例如列出5种水果。
prompt = PromptTemplate(
    template="List 5 {subject}.\n{format_instructions}",
    input_variables=['subject'],
    partial_variables={'format_instructions': format_instructions}
)

# 格式化提示，将主题设置为“fruits”。
_input = prompt.format(subject="fruits")

# 使用 llm 实例生成回应。
output = llm(_input)

# 使用输出解析器解析生成的回应。
response = output_parser.parse(output)

# 打印解析后的回应。
print(response)
