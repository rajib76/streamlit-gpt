import ast
import json

import openai
import streamlit as st

desc_per_list=[]
def main():
    print("Entering")
    key = st.text_input("Enter your Open AI token")
    openai.api_key = key
    name_placeholder = st.empty()
    if name_placeholder.button("Show Name","o2"):
        st.info(st.session_state.name_pers)
        name_placeholder.empty()

    desc_placeholder = st.empty()
    if desc_placeholder.button("Generate Description", "o1"):
        desc_placeholder.empty()

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Give a random name of a Hollywood actor or actress in json format",
            max_tokens=20,
            temperature=1
        )
        res_name = response["choices"][0]["text"]
        print(res_name)

        st.session_state['name_pers'] = res_name

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Describe " + res_name + " in 20 words without using his name in the description",
            max_tokens=516,
            temperature=0.7
        )
        res_desc = response["choices"][0]["text"]
        print(res_desc)
        st.info(res_desc)


if __name__ == "__main__":
    main()
