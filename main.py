from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return{"message":"CHATBOT is running"}
@app.get("/chat")
def chat(message:str):
    if "hello" in message.lower():
        reply="Hello! how can i help you?"
    elif"name" in message.lower():
        reply="My name is Chatbot."
    elif"bye" in message.lower():
        reply="Goodbye! Have a nice day."
    else:
        reply="I'm sorry, I don't understand. Can you please rephrase?"

    
    return {
        "user_message": message,
        "bot_response": reply
    }