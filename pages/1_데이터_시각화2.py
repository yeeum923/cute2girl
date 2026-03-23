import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 간단한 데이터 시각화 예제")

st.write("이 페이지에서는 간단한 데이터 시각화 예제를 보여줍니다. 모든 그래프는 한글로 작성되었습니다.")

# 샘플 데이터 생성
data = pd.DataFrame({
    '카테고리': ['A', 'B', 'C', 'D', 'E'],
    '값1': [10, 20, 15, 25, 30],
    '값2': [5, 15, 10, 20, 25]
})

st.header("1. 막대 그래프")
fig_bar = px.bar(data, x='카테고리', y='값1', title='카테고리별 값1 막대 그래프', labels={'값1': '값'})
st.plotly_chart(fig_bar)

st.header("2. 선 그래프")
fig_line = px.line(data, x='카테고리', y='값2', title='카테고리별 값2 선 그래프', labels={'값2': '값'})
st.plotly_chart(fig_line)

st.header("3. 산점도")
fig_scatter = px.scatter(data, x='값1', y='값2', title='값1 vs 값2 산점도', labels={'값1': 'X축 값', '값2': 'Y축 값'})
st.plotly_chart(fig_scatter)

st.header("4. 히스토그램")
values = [1, 2, 2, 3, 3, 3, 4, 4, 5]
fig_hist = px.histogram(values, title='값 분포 히스토그램', labels={'value': '값'})
st.plotly_chart(fig_hist)

st.header("5. 박스 플롯")
fig_box = px.box(data, y='값1', title='값1 박스 플롯')
st.plotly_chart(fig_box)
