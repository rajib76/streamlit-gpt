import ast
import json

import openai
import streamlit as st

desc_per_list=[]
def main():
    print("Entering")
    key = st.text_input("Enter your Open AI token")
    openai.api_key = key
    if st.button("Generate Description", "o1"):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Give a list of 10 famous Hollywood actors or actresses in json format",
            max_tokens=516,
            temperature=0.7
        )
        res = response["choices"][0]["text"]
        res_list = ast.literal_eval(res)
        print(res_list)
        res_list_len = len(res_list)
        for i in range(res_list_len):
            for key in res_list[i].keys():
                print(res_list[i][key])
                name_of_person = res_list[i][key]
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt="Describe " + name_of_person + " in 20 words without using his name in the description",
                    max_tokens=516,
                    temperature=0.7
                )
                desc_res = response["choices"][0]["text"]
                desc_per_list.append(desc_res)
    st.session_state.desc_per_list=desc_per_list
    show_next = st.button("next","nb")
    print("rajib")
    print(desc_per_list)
    # Initialize the current index
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
        # Whenever someone clicks on the button
        if show_next:
            # Show next element in list
            st.info(st.session_state.desc_per_list[st.session_state.current_index])
            # Update and store the index
            st.session_state.current_index += 1
        # for items in res:
        #     print(names)
        # names_json = json.loads(names)
        # print(names)
        # print(names_json["name"])
        # answer_text = st.info(res)


if __name__ == "__main__":
    main()
