# 导入dotenv库，用于从环境配置文件.env中加载环境变量。
# 这主要用于安全地管理敏感数据，例如API密钥。
from dotenv import load_dotenv  

# 调用load_dotenv函数来从.env文件加载环境变量。
load_dotenv()  

# 从transformers库导入AutoTokenizer和AutoModelForCausalLM。
# 这些用于自动加载和处理预训练的语言模型。
from transformers import AutoTokenizer, AutoModelForCausalLM

# 加载tokenizer，用于将文本转换为模型能理解的格式。
# 这里使用的是预训练模型"meta-llama/Llama-2-7b-chat-hf"。
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# 加载预训练的因果语言模型。
# 指定模型的设备为"auto"，以自动选择运行模型的最佳设备（CPU或GPU）。
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", device="auto")

# 定义一个提示文本，要求生成关于水果的爱情故事。
prompt = "你是一位起水果运营专家，请讲一个动人的关于水果的爱情故事。"

# 使用tokenizer处理输入文本，并将其转移到模型的设备上。
# 这里return_tensors="pt"表示返回的是PyTorch张量。
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# 使用模型生成回应，设置最大长度、采样参数以控制生成的文本多样性。
outputs = model.generate(inputs["input_ids"], max_length=2000, do_sample=True, top_p=0.95, top_k=60)

# 将生成的输出解码为文本，并跳过特殊标记。
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# 打印生成的故事。
print(response)
