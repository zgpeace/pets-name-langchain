# 从langchain包和其他库中导入必要的模块
from langchain.document_loaders import YoutubeLoader  # 导入YoutubeLoader，用于从YouTube视频加载数据
from langchain.text_splitter import RecursiveCharacterTextSplitter  # 导入用于处理长文档的文本分割器
from langchain.embeddings.openai import OpenAIEmbeddings  # 导入OpenAIEmbeddings，用于生成文档嵌入向量
from langchain.vectorstores import FAISS  # 导入FAISS，用于大数据集中高效的相似性搜索
from langchain.llms import OpenAI  # 导入OpenAI，用于访问语言模型功能
from langchain import PromptTemplate  # 导入PromptTemplate，用于创建结构化的语言模型提示
from langchain.chains import LLMChain  # 导入LLMChain，用于构建使用语言模型的操作链
from dotenv import load_dotenv  # 导入load_dotenv，用于从.env文件加载环境变量

load_dotenv()  # 从.env文件加载环境变量

embedding = OpenAIEmbeddings()  # 初始化OpenAI嵌入向量的实例，用于生成文档嵌入向量

# YouTube视频的URL
video_url = "https://youtu.be/-Osca2Zax4Y?si=iy0iePxzUy_bUayO"

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    # 加载YouTube视频字幕
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    # 将字幕分割成较小的片段
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    # 从文档片段创建FAISS数据库
    db = FAISS.from_documents(docs, embedding)
    return db

def get_response_from_query(db, query, k=4):
    # 对给定查询执行数据库的相似性搜索
    docs = db.similarity_search(query, k=k)

    # 连接前几个文档的内容
    docs_page_content = " ".join([d.page_content for d in docs])
    
    # 初始化一个OpenAI语言模型
    llm = OpenAI(model="text-davinci-003")

    # 定义语言模型的提示模板
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template = """
        You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
    """,
    )

    # 使用定义的提示创建一个语言模型链
    chain = LLMChain(llm=llm, prompt=prompt)

    # 使用查询和连接的文档运行链
    response = chain.run(question=query, docs=docs_page_content)

    # 通过替换换行符来格式化响应
    response = response.replace("\n", " ")
    return response, docs

# 示例用法：从YouTube视频URL创建向量数据库
# print(create_vector_db_from_youtube_url(video_url))
