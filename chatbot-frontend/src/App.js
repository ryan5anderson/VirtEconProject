import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css"; // Ensure styling for chat appearance

function App() {
    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]); // Store chat history
    const chatEndRef = useRef(null); // Auto-scroll ref

    // Function to handle API call and chat update
    const handleAsk = async () => {
        if (!question.trim()) return;

        const newMessage = { type: "user", text: question };
        setMessages((prevMessages) => [...prevMessages, newMessage]); // Show user input

        try {
            const res = await axios.post("http://localhost:5001/ask", { question });
            const botMessage = { type: "bot", text: res.data.generated_text || "No response text." };
            setMessages((prevMessages) => [...prevMessages, botMessage]); // Show bot response
        } catch (error) {
            const errorMessage = { type: "bot", text: "Error fetching response." };
            setMessages((prevMessages) => [...prevMessages, errorMessage]);
        }

        setQuestion(""); // Clear input box
    };

    // Auto-scroll to the latest message
    useEffect(() => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    return (
        <div className="chat-container">
            <h1>VirtualEconomist</h1>
            <div className="chat-box">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.type}`}>
                        {msg.type === "user" ? "You: " : "Bot: "} {msg.text}
                    </div>
                ))}
                <div ref={chatEndRef}></div>
            </div>
            <div className="input-container">
                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="Type your message..."
                    onKeyDown={(e) => e.key === "Enter" && handleAsk()} // Allow enter key submission
                />
                <button onClick={handleAsk}>Submit</button>
            </div>
        </div>
    );
}

export default App;
