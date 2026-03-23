import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="wide")

# ============================================================
# 헤더 영역
# ============================================================
st.title("👋 안녕하세요!")
st.write("여기는 김예음의 자기소개 페이지입니다.")

st.divider()

# ============================================================
# 프로필 영역
# ============================================================
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📸 프로필")
    st.image("https://via.placeholder.com/300", caption="프로필 사진")

with col2:
    st.subheader("👤 기본 정보")
    st.write("**이름:** 김예음")
    st.write("**직업:** 학생")
    st.write("**거주지:** 부천, 대한민국")
    st.write("**연락처:** contact@example.com")

st.divider()

# ============================================================
# 자기소개
# ============================================================
st.header("📖 자기소개")
st.write("""
저는 열정적인 개발자로서 새로운 기술을 배우고 문제를 해결하는 것을 즐깁니다.
Streamlit을 사용하여 효율적이고 사용자 친화적인 웹 애플리케이션을 만드는 것에 관심이 있습니다.
지속적인 학습과 성장을 추구하며, 팀과 협력하여 훌륭한 결과를 만들어내는 것을 좋아합니다.
""")

st.divider()

# ============================================================
# 기술 스택
# ============================================================
st.header("💻 기술 스택")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📚 언어")
    st.write("""
    - Python
    - JavaScript
    - Java
    - SQL
    """)

with col2:
    st.subheader("🛠️ 도구 & 프레임워크")
    st.write("""
    - Streamlit
    - React
    - Django
    - FastAPI
    """)

with col3:
    st.subheader("☁️ 기타")
    st.write("""
    - Git & GitHub
    - Docker
    - AWS
    - PostgreSQL
    """)

st.divider()

# ============================================================
# 경력 & 프로젝트
# ============================================================
st.header("🏆 경력 & 프로젝트")

with st.expander("📌 프로젝트 1: 데이터 분석 대시보드"):
    st.write("""
    **설명:** Streamlit을 사용한 실시간 데이터 분석 대시보드
    
    **사용 기술:** Python, Pandas, Plotly, Streamlit
    
    **기여:** 데이터 시각화 및 사용자 인터페이스 개발
    
    **링크:** [Github](https://github.com)
    """)

with st.expander("📌 프로젝트 2: 머신러닝 예측 모델"):
    st.write("""
    **설명:** 주식 가격 예측을 위한 머신러닝 모델
    
    **사용 기술:** Python, Scikit-learn, TensorFlow, Streamlit
    
    **기여:** 모델 개발 및 웹 애플리케이션 배포
    
    **링크:** [Github](https://github.com)
    """)

with st.expander("📌 프로젝트 3: API 서버"):
    st.write("""
    **설명:** RESTful API 기반의 백엔드 서버
    
    **사용 기술:** Python, FastAPI, PostgreSQL, Docker
    
    **기여:** API 설계 및 데이터베이스 구조화
    
    **링크:** [Github](https://github.com)
    """)

st.divider()

# ============================================================
# 교육 & 자격증
# ============================================================
st.header("🎓 교육 & 자격증")

education_data = {
    "학위/과정": ["Bachelor in Computer Science", "Python 심화 과정", "Web Development Bootcamp"],
    "기관": ["OO 대학교", "OO 교육원", "OO Bootcamp"],
    "연도": ["2019 - 2023", "2023", "2024"]
}

st.table(education_data)

st.divider()

# ============================================================
# 연락처
# ============================================================
st.header("📧 연락처")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("📧 **이메일**")
    st.write("contact@example.com")

with col2:
    st.write("🔗 **링크드인**")
    st.write("[LinkedIn](https://linkedin.com)")

with col3:
    st.write("🐙 **깃허브**")
    st.write("[GitHub](https://github.com)")

with col4:
    st.write("🐦 **트위터**")
    st.write("[@username](https://twitter.com)")

st.divider()

st.write("감사합니다! 💜")
