# 导入dotenv库，用于从环境配置文件.env中加载环境变量。
# 这通常用于安全地管理敏感数据，例如API密钥。
from dotenv import load_dotenv

# 执行load_dotenv函数，从.env文件加载环境变量到Python的环境变量中。
load_dotenv()

# 从transformers库导入T5Tokenizer和T5ForConditionalGeneration。
# 这些是用于NLP的预训练模型和对应的分词器。
from transformers import T5Tokenizer, T5ForConditionalGeneration

# 从预训练模型"google/flan-t5-small"加载T5分词器。
# 这个模型专门用于文本生成任务，如翻译、摘要等。
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")

# 加载预训练的T5条件生成模型。
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

# 定义输入文本，这里是一个英译德的翻译任务。
input_text = "translate English to German: How old are you?"

# 使用分词器处理输入文本，将文本转换为模型可理解的输入ID。
# return_tensors="pt"表示返回的是PyTorch张量。
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# 使用模型生成响应，即对输入文本进行翻译。
outputs = model.generate(input_ids)

# 解码模型输出，将生成的ID转换回文本格式，并打印出来。
print(tokenizer.decode(outputs[0]))
