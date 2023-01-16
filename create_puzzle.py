import openai
import streamlit as st

def main():
    key = st.text_input("Enter your Open AI token")
    openai.api_key = key
    if key >"":
        obj_name = st.text_input("Enter the name of the object to create a puzzle")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="A puzzle with the word {object} without using the word, no answer".format(object=obj_name),
            max_tokens=100,
            temperature=1
        )
        puzzle_desc = response["choices"][0]["text"]

        puzzle_placeholder = st.empty()

        if puzzle_placeholder.button("Create Puzzle"):
            st.info(puzzle_desc)
            puzzle_placeholder.empty()

if __name__=="__main__":
    main()