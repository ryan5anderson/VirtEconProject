import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [hasInteracted, setHasInteracted] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const chatEndRef = useRef(null);

  const handleAsk = async () => {
      if (!question.trim()) return;

      setHasInteracted(true);
      const newMessage = { type: "user", text: question, timestamp: new Date() };
      setMessages(prev => [...prev, newMessage]);

      setIsLoading(true);
      try {
          const res = await axios.post("http://localhost:5001/ask", { question });
          const botMessage = { 
              type: "bot", 
              text: res.data.generated_text || "No response text.", 
              timestamp: new Date() 
          };
          setMessages(prev => [...prev, botMessage]);
      } catch {
          setMessages(prev => [...prev, { type: "bot", text: "Error fetching response.", timestamp: new Date() }]);
      }
      setIsLoading(false);
      setQuestion("");
  };

  useEffect(() => {
      chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  return (
    <div className={`app-background ${darkMode ? 'dark-mode' : ''}`}>
        <div className="top-bar">
          <div className="left-section">
              <span className="app-title">VirtualEconomist</span>
              <button 
                  className="new-chat-btn" 
                  onClick={() => {
                      setMessages([]);
                      setHasInteracted(false);
                      setQuestion("");
                  }}
              >
                  + New Chat
              </button>
              <button className="dark-toggle" onClick={() => setDarkMode(!darkMode)}>
                  {darkMode ? '☀️' : '🌙'}
              </button>
          </div>

          <div className="right-section">
              <img 
                  src="https://pilbox.themuse.com/image.png?url=https%3A%2F%2Fassets.themuse.com%2Fuploaded%2Fcompanies%2F15000185%2Fsmall_logo.png%3Fv%3DNone&h=630&mode=fill&prog=1&w=1200" 
                  alt="Federal Reserve" 
                  className="fed-logo"
              />
          </div>
        </div>

        <div className={`chat-container ${hasInteracted ? 'active' : 'centered'}`}>
            {!hasInteracted && (
                <div className="welcome-message">
                    Welcome! Ask me about the economy.
                </div>
            )}

            {hasInteracted && (
                <div className="chat-box">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.type}`}>
                            <div>{msg.text}</div>
                        </div>
                    ))}
                    {isLoading && <div className="typing-indicator">VirtualEconomist is typing...</div>}
                    <div ref={chatEndRef}></div>
                </div>
            )}

            <div className="input-container">
                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="Ask about inflation, interest rates, markets..."
                    onKeyDown={(e) => e.key === "Enter" && handleAsk()}
                />
                <button onClick={handleAsk}>➤</button>
            </div>

            <div className="disclaimer">
                VirtualEconomist can provide general insights. Always verify critical financial information.
            </div>
        </div>
    </div>
  );
}

export default App;
