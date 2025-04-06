import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender")
st.title("SHL Assessment Recommender")
query = st.text_area("Enter job description or query")

if st.button("Recommend") and query:
    response = requests.get("http://localhost:8000/api/recommend", params={"q": query})
    results = response.json()["results"]

    for res in results:
        st.markdown(f"### [{res['name']}]({res['url']})")
        st.write(f"**Remote Testing:** {res['remote']} | **Adaptive:** {res['adaptive']}")
        st.write(f"**Duration:** {res['duration']} | **Type:** {res['type']}")
