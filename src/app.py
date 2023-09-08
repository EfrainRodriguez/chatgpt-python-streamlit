import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# ##############################################################################
# ChatGPT desde la terminal
# ##############################################################################

# messages = []

# while True:
#   user_input = input("You: ")
#   if user_input == "0":
#     break

#   messages.append({"role": "user", "content": user_input})

#   response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=messages
#   )

#   responseMessage = response['choices'][0]['message']['content']

#   messages.append({"role": "assistant", "content": responseMessage})

#   print("Bot: " + responseMessage)


# ##############################################################################
# ChatGPT con Streamlit
# ##############################################################################

st.title("Mi ChatGPT")

if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy ChatGPT, ¿En qué puedo ayudarte?"}]

for msg in st.session_state["messages"]:
  st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
  st.session_state["messages"].append({"role": "user", "content": user_input})
  st.chat_message("user").write(user_input)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=st.session_state["messages"]
  )
  responseMessage = response['choices'][0]['message']['content']
  st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
  st.chat_message("assistant").write(responseMessage)