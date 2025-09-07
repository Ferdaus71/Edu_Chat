from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from pymongo import MongoClient

app = FastAPI()

# MongoDB Atlas connection (replace with your URI)
client = MongoClient("your_mongodb_atlas_uri")
db = client["edu_chatbot"]

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

class Question(BaseModel):
    question: str
    context: str

@app.post("/ask")
async def ask_qn(q: Question):
    answer = qa_pipeline(question=q.question, context=q.context)
    db.questions.insert_one({"question": q.question, "answer": answer["answer"]})
    return {"answer": answer["answer"]}

@app.get("/")
async def root():
    return {"message": "Education Chatbot API Running 🚀"}
