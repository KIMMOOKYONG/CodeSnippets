import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json


@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer("jhgan/ko-sroberta-multitask")
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv("https://raw.githubusercontent.com/kairess/mental-health-chatbot/master/wellness_dataset.csv")
    df["embedding"] = df["embedding"].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header("심리상담 챗봇")
st.markdown("[❤️빵형의 개발도상국](https://www.youtube.com/c/빵형의개발도상국)")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

with st.form("form", clear_on_submit=True):
    user_input = st.text_input("당신: ", "")
    submitted = st.form_submit_button("전송")

if submitted and user_input:
    embedding = model.encode(user_input)

    df["distance"] = df["embedding"].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[df["distance"].idxmax()]

    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer["챗봇"])

# message = st.container()
# for i in range(len(st.session_state["past"])):
#     message.text("사용자: " + st.session_state["past"][i])
#     if len(st.session_state["generated"]) > i:
#         message.text("상담사: " + st.session_state["generated"][i])

message = st.empty()
for i in range(len(st.session_state["past"])):
    message.text("사용자: " + st.session_state["past"][i])
    if len(st.session_state["generated"]) > i:
        message.text("상담사: " + st.session_state["generated"][i])

