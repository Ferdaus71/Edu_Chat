from fastapi import FastAPI
from pydantic import BaseModel
import pymongo
from transformers import pipeline

app = FastAPI()

# MongoDB Connection
import os
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
client = pymongo.MongoClient(MONGO_URI)
db = client["chatbot_db"]
conversations = db["conversations"]

# Load NLP model
qa_pipeline = pipeline("question-answering")

class Query(BaseModel):
    question: str
    context: str

@app.post("/ask")
def ask_question(query: Query):
    result = qa_pipeline(question=query.question, context=query.context)
    conversations.insert_one({
        "question": query.question,
        "context": query.context,
        "answer": result["answer"]
    })
    return {"answer": result["answer"]}

@app.get("/")
def root():
    return {"message": "Education Chatbot Backend Running!"}
