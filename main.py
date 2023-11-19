import langchain_helper as lch  # 导入名为langchain_helper的模块，并使用别名lch
import streamlit as st  # 导入Streamlit库，并使用别名st

st.title("Pets name generator")  # 在Streamlit应用中设置标题

# 通过侧边栏选择宠物类型
animal_type = st.sidebar.selectbox("Select animal type", ["dog", "cat", "cow", "horse", "pig", "sheep"])

# 根据宠物类型设置宠物颜色，使用侧边栏的文本区域输入
if animal_type in ['dog', 'cat', 'cow', 'horse', 'pig', 'sheep']:
    pet_color = st.sidebar.text_area(label=f"What color is your {animal_type}?", max_chars=15)
else:
    pet_color = st.sidebar.text_area(label="What color is your pet?", max_chars=15)

# 如果有输入颜色，调用generate_pet_name函数生成宠物名字并显示
if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response['pet_name'])
