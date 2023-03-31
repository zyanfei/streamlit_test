import streamlit as st
import pandas as pd
from io import BytesIO

# file_path = r"G:\test\a.xlsx"
# df = pd.read_excel(file_path, dtype="object")
# df = {"name": ["张三", "王五", "李四", "赵六"],
#       "age": [15, 16, 17, 18],
#       "county": ["china", "china", "china", "china"]}
st.title("文件拼接")
st.text("操作说明：使两个需要拼接的excel文件，"
        "(或一个excel文件的两个不同sheet)"
        "按字段实现拼接")
st.text("")
file_get = st.file_uploader("选择:第一个要数据拼接的文件")
if file_get is None:
    # 防止未选择文件时报错
    st.stop()
df = pd.read_excel(file_get, None)
sheet_name = list(df.keys())
st.text("")
sheet_select = st.selectbox("选择:第一个要数据拼接的工作表", sheet_name)
if sheet_select is None:
    st.stop()
st.dataframe(df[sheet_select])
sheet_data = df[sheet_select]
column_name = list(df[sheet_select])
column_select = st.selectbox("选择:第一个要拼接的列", column_name)
column_data = sheet_data[column_select]
st.dataframe(column_data)


file_get_2 = st.file_uploader("选择:第二个要数据拼接的文件")
if file_get_2 is None:
    # 防止未选择文件时报错
    st.stop()
df2 = pd.read_excel(file_get, None)
sheet_name2 = list(df2.keys())
sheet_select2 = st.selectbox("选择:第二个要数据拼接的工作表", sheet_name2)
if sheet_select2 is None:
    st.stop()
st.dataframe(df[sheet_select2])
sheet_data2 = df[sheet_select2]
column_name2 = list(df[sheet_select2])
column_select2 = st.selectbox("选择:第二个要拼接的列", column_name2)
column_data2 = sheet_data[column_select2]
st.dataframe(column_data2)

# 执行拼接
click_button = st.button("用力点击，执行拼接")
if click_button is False:
    st.stop()

final_data = pd.merge(sheet_data, sheet_data2, left_on=column_select, right_on=column_select2, how="outer")
st.dataframe(final_data)

# 数据保存 用例保存csv文件
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')
#
#
# csv = convert_df(final_data)
#
# st.download_button(
#     label="拼接结果导出为csv文件",
#     data=csv,
#     file_name='拼接后数据.csv'
# )
# 数据保存 用例保存xlsx文件

output = BytesIO()
final_data.to_excel(output)

st.download_button(
    label="生成并下载结果",
    data=output,
    file_name="merge_file.xlsx"
)
