# 从 'operator' 模块导入 'itemgetter' 函数，用于项查找
from operator import itemgetter

# 从 langchain 和 langchain_core 包中导入各种类和函数
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableConfig
import json  # 导入 JSON 库来解析和生成 JSON
from langchain.callbacks import get_openai_callback  # 导入获取 OpenAI 回调的函数

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
set_debug(True)  # 启用 langchain 的调试模式

# 定义一个函数来解析 JSON 或修复它（如果它格式不正确）
def parse_or_fix(text: str, config: RunnableConfig):
    # 使用模板提示和 OpenAI 模型定义一系列操作来修复文本
    fixing_chain = (
        ChatPromptTemplate.from_template(
            "Fix the following text:\n\n```text\n{input}\n```\nError: {error}"
            " Don't narrate, just respond with the fixed data."
        )
        | ChatOpenAI()  # 连接到 ChatOpenAI 模型来处理提示
        | StrOutputParser()  # 解析聊天模型的字符串输出
    )
    
    # 尝试解析 JSON 三次，如果有错误，使用链来修复
    for _ in range(3):
        try:
            return json.loads(text)  # 尝试将文本解析为 JSON
        except Exception as e:  # 捕获解析异常
            # 使用格式错误的文本和错误信息调用修复链
            text = fixing_chain.invoke({"input": text, "error": e}, config)
    return "Failed to parse"  # 如果三次解析都失败，返回失败消息

# 使用上下文管理器从 OpenAI 获取回调，并调用 parse_or_fix 函数
with get_openai_callback() as cb:
    # 创建一个 RunnableLambda 对象，其中包含 parse_or_fix 函数
    # 并使用类似 JSON 的字符串和配置字典调用它
    output = RunnableLambda(parse_or_fix).invoke(
        "{foo: bar}", {"tags": ["my-tag"], "callbacks": [cb]}
    )
    print(output)  # 打印调用结果
    print(cb)  # 打印回调对象
