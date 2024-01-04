import streamlit as st
from wordcloud import WordCloud
from summa import summarizer  # summa 패키지 설치 필요
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='NanumGothic')

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path='/usr/share/fonts/truetype/nanum/NanumGothic.ttf').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def main():
    st.title("문서 시각화")

    uploaded_file = st.file_uploader("텍스트 파일 업로드", type=["txt"])

    if uploaded_file is not None:
        st.info("파일이 성공적으로 업로드되었습니다!")

        # 파일 내용 읽기 및 디코딩
        file_contents = uploaded_file.read().decode('utf-8')

        st.subheader("파일 요약:")
        summarized_text = summarizer.summarize(file_contents)
        st.text(summarized_text)

        if st.button("WordCloud 생성 (원본)"):
            generate_wordcloud(file_contents)

if __name__ == "__main__":
    main()
