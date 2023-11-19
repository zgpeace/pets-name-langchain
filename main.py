import streamlit as st  # 导入Streamlit库，用于创建Web应用程序
import langchain_helper as lch  # 导入自定义模块'langchain_helper'，用于处理langchain操作
import textwrap  # 导入textwrap模块，用于格式化文本

st.title("YouTube Assistant")  # 设置Streamlit网页应用的标题

# 使用Streamlit的侧边栏功能来创建输入表单
with st.sidebar:
    # 在侧边栏中创建一个表单
    with st.form(key='my_form'):
        # 创建一个文本区域用于输入YouTube视频URL
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
        )
        # 创建一个文本区域用于输入关于YouTube视频的查询
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )
        
        # 创建一个提交表单的按钮
        submit_button = st.form_submit_button(label='Submit')

# 检查是否同时提供了查询和YouTube URL
if query and youtube_url:
    # 从YouTube视频URL创建向量数据库
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    # 根据向量数据库获取查询的响应
    response, docs = lch.get_response_from_query(db, query)
    # 在应用程序中显示一个副标题“回答：”
    st.subheader("Answer：")
    # 显示响应，格式化为每行85个字符
    st.text(textwrap.fill(response, width=85))
