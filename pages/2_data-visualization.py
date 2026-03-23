import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import seaborn as sns

# 한글 폰트 설정
font_path = 'fonts/NotoSansKR-Bold.ttf'
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 표시

st.title("📊 간단한 데이터 시각화 예시 (한글 폰트)")

st.write("matplotlib과 seaborn을 사용하여 한글 폰트로 그래프를 그립니다.")

# 샘플 데이터
data = pd.DataFrame({
    '카테고리': ['사과', '바나나', '오렌지', '포도'],
    '판매량': [23, 17, 35, 29],
    '가격': [1000, 800, 1200, 1500]
})

st.header("1. 막대 그래프 (Matplotlib)")
fig, ax = plt.subplots()
ax.bar(data['카테고리'], data['판매량'], color='skyblue')
ax.set_title('과일별 판매량', fontproperties=font_prop)
ax.set_xlabel('과일', fontproperties=font_prop)
ax.set_ylabel('판매량', fontproperties=font_prop)
st.pyplot(fig)

st.header("2. 선 그래프 (Matplotlib)")
fig2, ax2 = plt.subplots()
ax2.plot(data['카테고리'], data['가격'], marker='o', color='green')
ax2.set_title('과일별 가격', fontproperties=font_prop)
ax2.set_xlabel('과일', fontproperties=font_prop)
ax2.set_ylabel('가격 (원)', fontproperties=font_prop)
st.pyplot(fig2)

st.header("3. 산점도 (Seaborn)")
fig3 = plt.figure()
sns.scatterplot(data=data, x='판매량', y='가격', hue='카테고리', s=100)
plt.title('판매량 vs 가격 산점도', fontproperties=font_prop)
plt.xlabel('판매량', fontproperties=font_prop)
plt.ylabel('가격 (원)', fontproperties=font_prop)
st.pyplot(fig3)

st.header("4. 박스 플롯 (Seaborn)")
fig4 = plt.figure()
sns.boxplot(data=data[['판매량', '가격']])
plt.title('판매량과 가격의 분포', fontproperties=font_prop)
plt.xticks([0, 1], ['판매량', '가격'], fontproperties=font_prop)
st.pyplot(fig4)
