# 导入Langchain库中的OpenAI模块，该模块提供了与OpenAI语言模型交互的功能
from langchain.llms import OpenAI  

# 导入Langchain库中的PromptTemplate模块，用于创建和管理提示模板
from langchain.prompts import PromptTemplate  

# 导入Langchain库中的LLMChain模块，它允许构建基于大型语言模型的处理链
from langchain.chains import LLMChain  

# 导入dotenv库，用于从.env文件加载环境变量，这对于管理敏感数据如API密钥很有用
from dotenv import load_dotenv  

# 调用load_dotenv函数来加载.env文件中的环境变量
load_dotenv()  


# 使用OpenAI类创建一个名为llm的实例。这个实例配置了用于生成文本的模型参数。
# 模型使用的是"text-davinci-003"，这是一个高级的GPT-3模型。
# temperature设置为0.8，这决定了生成文本的随机性和创造性。
# max_tokens设置为60，限制生成文本的最大长度。
llm = OpenAI(
    model="text-davinci-003",
    temperature=0.6,
    max_tokens=120
)

samples = [
  {
    "fruit_type": "玫瑰葡萄",
    "occasion": "爱情",
    "ad_copy": "玫瑰，浪漫的象征，是你向心爱的人表达爱意的最佳选择。"
  },
  {
    "fruit_type": "金钻菠萝",
    "occasion": "庆祝",
    "ad_copy": "金钻菠萝，庆祝的完美伴侣，为您的特别时刻增添甜蜜与奢华。"
  },
  {
    "fruit_type": "蜜瓜",
    "occasion": "休闲",
    "ad_copy": "蜜瓜，休闲时光的甜蜜伴侣，让您的闲暇时光更加美好。"
  },
  {
    "fruit_type": "富士苹果",
    "occasion": "健康",
    "ad_copy": "富士苹果，健康生活的选择，丰富您的营养，活力每一天。"
  }
]

# 导入PromptTemplate类，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate

# 定义一个提示模板，包括水果类型、场景和广告文案。
# {fruit_type}, {occasion}, 和 {ad_copy} 是占位符，稍后将被替换。
template = "水果类型：{fruit_type}\n场景：{occasion}\n广告文案：{ad_copy}\n"

# 创建一个PromptTemplate实例，传入输入变量和模板。
prompt_sample = PromptTemplate(input_variables=["fruit_type", "occasion", "ad_copy"], template=template)

# 使用format方法格式化提示，使用samples列表中的第一个样本数据。
# 假设samples是一个预先定义的包含多个样本的列表。
print(prompt_sample.format(**samples[0]))

# 导入FewShotPromptTemplate类，用于创建包含多个示例的提示模板。
from langchain.prompts.few_shot import FewShotPromptTemplate

# 创建一个FewShotPromptTemplate实例。
# 使用samples作为示例，prompt_sample作为每个示例的格式，定义输入变量和后缀。
prompt = FewShotPromptTemplate(
    examples=samples,
    example_prompt=prompt_sample,
    suffix="水果类型：{fruit_type}\n场景：{occasion}",
    input_variables=["fruit_type", "occasion"],
)
# 格式化提示，用于生成特定水果类型和场景的广告文案。
print(prompt.format(fruit_type="玫瑰葡萄", occasion="爱情"))

# 使用语言模型（如GPT-3）生成文案。
result = llm(prompt.format(fruit_type="火龙果", occasion="爱情"))
print(result)

# # 导入SemanticSimilarityExampleSelector和Qdrant，用于选择与输入最相关的示例。
# from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
# from langchain.vectorstores import Qdrant
# from langchain.embeddings import OpenAIEmbeddings

# # 初始化一个示例选择器，使用语义相似度选择与输入最相关的示例。
# example_selector = SemanticSimilarityExampleSelector.from_examples(
#     samples,
#     OpenAIEmbeddings(),
#     Qdrant,
#     k=1
# )

# # 创建一个新的FewShotPromptTemplate实例，这次使用示例选择器来选择最佳示例。
# prompt = FewShotPromptTemplate(
#     example_selector=example_selector, 
#     example_prompt=prompt_sample, 
#     suffix="水果类型：{fruit_type}\n场景：{occasion}",
#     input_variables=["fruit_type", "occasion"],
# )
# # 格式化提示，用于生成特定水果类型和场景的广告文案。
# print(prompt.format(fruit_type="钻石石榴", occasion="爱情"))


