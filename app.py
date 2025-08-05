import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/mydata.csv')
#global variable
url = 'https://youtu.be/XyEOEBsa8I4?si=cM2dxIWbw7033J8M'

#directory
urls = {
    '윤리' : ['1', '2'],
    '코딩' : ['3', '4']
}

st.title('this is my first web app')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('SubContent1...'):
        st.subheader('SubContent1...')
        st.video(url)

    with st.expander('SubContent2...'):
        st.subheader('Image Content...')
        st.image('./images/catdog.jpg')
    
    with st.expander('SubContent3...'):
        st.subheader('HTML Content...')
        import streamlit.components.v1 as htmlviewer
        with open ('./htmls/index2.html', 'r', encoding='utf-8') as f:
            html1 = f.read()
            f.close()
        htmlviewer.html(html1, height=800, scrolling=True)

    with st.expander('SubContent4...'):
        st.subheader('DataFrame Content...')
        st.table(df)
        st.write(df.describe())
        fig, ax = plt.subplots(figsize=(20, 10))
        df.plot(ax=ax)
        plt.savefig('./images/mygraph.png')
        st.image('./images/mygraph.png')


    with st.expander('Tips...'):
        st.info('Tips.......')