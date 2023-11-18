from langchain.llms import OpenAI  # 导入Langchain库中的OpenAI模块
from langchain.prompts import PromptTemplate  # 导入Langchain库中的PromptTemplate模块
from langchain.chains import LLMChain  # 导入Langchain库中的LLMChain模块
from dotenv import load_dotenv  # 导入dotenv库，用于加载环境变量

load_dotenv()  # 加载.env文件中的环境变量

def generate_pet_name(animal_type):
    llm = OpenAI(temperature=0.7)  # 创建OpenAI模型的实例，设置temperature参数为0.7以调整生成的多样性

    # 创建PromptTemplate实例，用于构造输入提示
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type'],
        template="I have a {animal_type} pet and I want a cool name for it. Suggest me five cool names for my pet."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)  # 创建LLMChain实例，将OpenAI模型和PromptTemplate传入
    response = name_chain({'animal_type': animal_type})  # 使用LLMChain生成宠物名字

    return response  # 返回生成的名字

# 当该脚本作为主程序运行时，执行以下代码
if __name__ == "__main__":
    print(generate_pet_name('cat'))  # 调用generate_pet_name函数，并打印返回的结果
