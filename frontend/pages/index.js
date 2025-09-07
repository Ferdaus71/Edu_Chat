import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askBot = async () => {
    const res = await axios.post("https://your-backend-service.onrender.com/ask", {
      question: question,
      context: "Gravity was discovered by Isaac Newton."
    });
    setAnswer(res.data.answer);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">🎓 Education Chatbot</h1>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask me anything..."
        className="border p-2 rounded w-80"
      />
      <button
        onClick={askBot}
        className="mt-2 bg-blue-500 text-white px-4 py-2 rounded"
      >
        Ask
      </button>
      {answer && (
        <div className="mt-4 p-4 bg-white shadow rounded w-80">
          <strong>Answer:</strong> {answer}
        </div>
      )}
    </div>
  );
}