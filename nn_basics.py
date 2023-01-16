import os

import openai
import streamlit as st
from gtts import gTTS
from googletrans import Translator

try:
    os.mkdir("temp")
except:
    pass
translator = Translator()


def text_to_speech(input_language, output_language, text, tld):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text


def main():
    st.header("Basics of neural network through prompts")
    key = st.text_input("Enter your Open AI token")
    if key > "":
        openai.api_key = key
        option = st.selectbox("Select the prompt to learn about neural network",
                              ("Tell me the history of deep learning",
                               "Explain the architecture of neural network",
                               "What is a perceptron in neural network",
                               "What is a multi-layer perceptron",
                               "What is an activation function",
                               "What are the different types of activation functions",
                               "What is a loss function in neural network",
                               "What are the different types of loss function",
                               "What is a local optimum and saddle point",
                               "What is back propagation",
                               "Explain the concept of gradient descent",
                               "Expalin the concept of stochastic gradient descent",
                               "What is weight initialization and what are the different techniques",
                               "What is regularization",
                               "What are the different types of regularizations",
                               "Explain the concept of dropout",
                               "What is batch normalization in machine learning"))
        temp = st.slider("temperature (allows to control AI creativity)", 0.0, 1.0, 0.7)
        if (option):
            if (st.button("Give me the answer", "o1")):
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=option,
                    max_tokens=516,
                    temperature=temp
                )
                res = response["choices"][0]["text"]
                answer_text = st.info(res)
                # For some reason text to speech worked locally but not on streamlit cloud
                result, output_text = text_to_speech("en", "en", res, "com")
                audio_file = open(f"temp/{result}.mp3", "rb")
                audio_bytes = audio_file.read()
                st.markdown(f"## Listen to your answer:")
                st.audio(audio_bytes, format="audio/mp3", start_time=0)
            else:
                pass
        else:
            pass

    else:
        pass


if __name__ == "__main__":
    # Start from here - This is the main program
    main()
