import streamlit as st
import plotly.express as px
import pandas as pd

# 데이터 준비
data = {
    'name': ['lee', 'pakr', 'kim'],
    'grade': [2, 2, 2],
    'number': [1, 2, 3],
    'kor': [90, 88, 99],
    'eng': [91, 89, 99],
    'math': [81, 77, 99],
    'info': [100, 100, 100]
}
df = pd.DataFrame(data)

# Streamlit 웹앱 제목
st.title("학생 성적 시각화 대시보드")

# 원본 데이터 표시
st.subheader("원본 데이터")
st.dataframe(df)

# 평균 점수 계산 및 표시
df['average'] = df[['kor', 'eng', 'math', 'info']].mean(axis=1)
st.subheader("학생별 평균 점수")
st.dataframe(df[['name', 'average']])

# 학생 선택 드롭다운
st.subheader("학생별 과목 점수 시각화")
selected_student = st.selectbox("학생 선택", df['name'])

# 선택한 학생의 데이터 필터링
student_data = df[df['name'] == selected_student][['kor', 'eng', 'math', 'info']].melt(var_name='subject', value_name='score')

# 막대그래프 생성
fig_bar = px.bar(
    student_data,
    x='subject',
    y='score',
    title=f"{selected_student} 학생의 과목별 점수",
    labels={'subject': '과목', 'score': '점수'},
    color='subject',
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig_bar.update_layout(showlegend=False)
st.plotly_chart(fig_bar)

# 모든 학생의 산점도 시각화
st.subheader("모든 학생의 과목별 점수 비교 (산점도)")
subjects = ['kor', 'eng', 'math', 'info']
for subject in subjects:
    fig_scatter = px.scatter(
        df,
        x='name',
        y=subject,
        size=subject,
        color=subject,
        title=f"{subject.upper()} 점수 비교",
        labels={'name': '학생', subject: '점수'},
        color_continuous_scale=px.colors.sequential.Viridis
    )
    st.plotly_chart(fig_scatter)