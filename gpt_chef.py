import openai
import streamlit as st

key = st.text_input("Enter your Open AI token")
openai.api_key = key
if key>"":
    food_answer = st.text_input("Name the food item you want to eat")
    prompt = "markdown, INPUT:{a food item} " \
             "OUPTUT: {recipe}) {recipe} : " \
             "{detailed recipe to make the {food item}}" \
             " INPUT:" + food_answer
    if st.button("Get recipe"):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            temperature=1
        )

        res_recipe = response["choices"][0]["text"]
        img_prompt = "A beautiful image of "+food_answer
        response = openai.Image.create(
            prompt=img_prompt,
            n=1,
            size="256x256"
        )

        image_url = response['data'][0]['url']
        st.info(res_recipe)
        st.image(
            image_url,width=600,  # Manually Adjust the width of the image as per requirement
        )
