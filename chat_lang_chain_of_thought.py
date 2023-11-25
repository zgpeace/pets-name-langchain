# 导入Langchain库中的OpenAI模块，该模块提供了与OpenAI语言模型交互的功能
from langchain.llms import OpenAI  

# 导入Langchain库中的PromptTemplate模块，用于创建和管理提示模板
from langchain.prompts import PromptTemplate  

# 导入Langchain库中的LLMChain模块，它允许构建基于大型语言模型的处理链
from langchain.chains import LLMChain  

# 导入dotenv库，用于从.env文件加载环境变量，这对于管理敏感数据如API密钥很有用
from dotenv import load_dotenv  

# 导入Langchain库中的ChatOpenAI类，用于创建和管理OpenAI聊天模型的实例。
from langchain.chat_models import ChatOpenAI

# 调用dotenv库的load_dotenv函数来加载.env文件中的环境变量。
# 这通常用于管理敏感数据，如API密钥。
load_dotenv()  

# 创建一个ChatOpenAI实例，配置它使用gpt-3.5-turbo模型，
# 设定温度参数为0.7（控制创造性的随机性）和最大令牌数为60（限制响应长度）。
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=500
)

# 从langchain库导入所需的类。
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# 定义一个固定模板，描述AI作为水果电商公司助手的角色。
# 这是对AI预期功能的直接描述。
rote_template = "你是一个为水果电商公司工作的AI助手, 你的目标是帮助客户根据他们的喜好做出明智的决定"

# 使用固定模板创建一个SystemMessagePromptTemplate对象。
system_prompt_role = SystemMessagePromptTemplate.from_template(rote_template)

# 定义一个思维链（COT）模板。此模板提供了更详细的处理方法，
# 包括AI如何处理和响应请求的示例。
cot_template = """
作为一个为水果电商公司工作的AI助手，我的目标是帮助客户根据他们的喜好做出明智的决定。 

我会按部就班的思考，先理解客户的需求，然后考虑各种水果的涵义，最后根据这个需求，给出我的推荐。
同时，我也会向客户解释我这样推荐的原因。

示例 1:
  人类：我想找一种象征爱情的水果。
  AI：象征爱情的水果之一是草莓。草莓以其鲜艳的红色和心形外观，成为爱情的象征，通常与浪漫和情感联系在一起。因此，考虑到这一点，我会推荐草莓。草莓心形外观：草莓的心形轮廓与爱情的传统符号——心形——相吻合，使其成为爱情的自然象征。鲜艳的红色：草莓的红色在许多文化中与激情和爱情联系在一起，象征着热情和浓烈的感情。甜美的味道：草莓的甜味象征着爱情的甜蜜和愉悦。这是你在寻找的。

示例 2:
  人类：我想要一些独特和奇特的水果。
  AI：从你的需求中，一种独特和奇特的水果是“火龙果”。这种水果以其独特的外观和口感而闻名，通常具有明亮的粉红色皮肤和点缀着黑色种子的白色或红色果肉。因此，我建议你考虑火龙果。火龙果独特性：火龙果的外形和味道与众不同，为寻求新奇体验的水果爱好者提供了完美选择。而且，火龙果视觉吸引力：其鲜艳的颜色和特殊的形状在视觉上吸引人，常常成为餐桌上的焦点。也可能会吸引你。
"""

# 使用COT模板创建一个SystemMessagePromptTemplate对象。
system_prompt_cot = SystemMessagePromptTemplate.from_template(cot_template)

# 定义一个人类输入的模板。
human_template = "{human_input}"
# 使用人类输入模板创建一个HumanMessagePromptTemplate对象。
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 将系统角色、COT和人类输入模板组合成一个聊天提示模板。
chat_prompt = ChatPromptTemplate.from_messages([system_prompt_role, system_prompt_cot, human_prompt])

# 用特定的人类输入格式化聊天提示，关于为喜欢不甜、浪漫水果的女朋友购买水果。
prompt = chat_prompt.format_prompt(human_input="我想要为我的女朋友购买水果。她喜欢不是很甜的，并且浪漫的水果。你有什么建议吗？").to_messages()

# 使用格式化的提示从语言模型（llm）生成响应。
response = llm(prompt)
# 打印语言模型生成的响应。
print(response)
