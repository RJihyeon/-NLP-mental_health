# mental_health

<h3>❤️discriptions❤️</h3>
A Customized Exchange Student Review Service for Well-being : Analyzing Factors Affecting the Mental Health of Exchange Students

![header](https://capsule-render.vercel.app/api?type=wave&color=auto&text=교환학생%20잠재적%20우울요인%20분석&fontSize=40)
<br></br>

<h3>🔨Tools🔨</h3>
<div align="center">
	<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white" />
	<img src="https://img.shields.io/badge/Figma-F24E1E?style=flat&logo=Figma&logoColor=white" />
	<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white" />
	<img src="https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=Selenium&logoColor=white" />
	<img src="https://img.shields.io/badge/Gensim-FFA200?style=flat&logo=로고이름&Color=white" />
</div>
<br></br>
<h3>✔️Tasks✔️</h3>

- [크롤링-학교 국제처 후기](https://github.com/RJihyeon/NLP_mental_health/tree/main/crawling_schoolweb)
- [크롤링-네이버 블로그](/링크필요)
- [전처리-학교 국제처 후기](https://github.com/RJihyeon/NLP_mental_health/blob/main/%ED%85%8D%EC%A0%95%EC%B2%98_%EC%A0%84%EC%B2%98%EB%A6%AC.ipynb)
- [전처리-블로그](/링크필요)
- [토픽 모델링, 시각화](https://github.com/RJihyeon/NLP_mental_health/blob/main/topic-moㅅdeling.ipynb)
- [모델링 결과 HTML](https://github.com/RJihyeon/NLP_mental_health/blob/main/display_topics.html)

<h4>🖥️1. 크롤링</h4>

- 국제처 교환학생 후기 약 10000건 크롤링
- 네이버 블로그 교환학생+우울 검색어의 후기 약 **\_**건 크롤링

<h4>🖥️2. 전처리</h4>

- 불용어 제거 : stopwords.txt 파일의 불용어들 약 707개를 제외
- 문장 필터링 : '우울', '불안', '스트레스' 3가지 정신건강 관련 키워드들을 포함한 문장만 수집
- 결측치 확인 및 보충
- 전처리 : 텍스트를 문장 단위로 분할하고, 각 문장에 대한 주요 키워드 3가지가 포함된 문장의 형태소 분석, 명사 추출
- return : 처리된 모든 문장의 명사 리스트

<h4>🖥️3. 토픽모델링</h4>

[토큰화 및 사전처리]

- 토큰화 : df의 preprocessed열에 전처리된 텍스트를 정규 표현식을 사용해 단어 단위로 토큰화. 모든 토큰을 소문자 변환
- 사전 생성: gensim.corpora 모듈 사용해 사전 생성
- 코퍼스 생성 : 토큰 리스트 사용해 코퍼스 생성/각 문서에서 단어의 빈도 나타내는 doc2bow 변환을 통해 생성

<p>[LDA 모델 설정 및 훈련]</p>

- 모델 설정 : gensim.models.LdaMode을 사용해 LDA 모델을 설정
- 하이퍼파라미터 설정 : alph와 eta auto로 설정 자동 최적화
- 훈련 : 주어진 데이터와 파라미터로 모델 훈련

<p>[시각화]</p>

- pyLDAvis : 시각화 준비
- HTML 파일로 저장 : display_topics.html 생성
- 시각화 내용 : 토픽 수, 토픽 간 거리, 토픽별 주요 단어 확인 가능
