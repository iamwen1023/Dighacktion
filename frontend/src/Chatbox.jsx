
import React, { useState } from "react";
import History from "./History";
import Conversation from "./Conversation";
import logo from "./CrossDoc-logo.svg";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [currentMessageIndex, setCurrentMessageIndex] = useState(null);

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setMessages([...messages, { text: input, isUser: true }]);
    simulateBotResponse(input);
    setInput("");
  };

  const simulateBotResponse = (userMessage) => {
    const botMessage = `Hi there! You said: "${userMessage}"`;
    setMessages([...messages, { text: botMessage, isUser: false }]);
  };

  return (
    <div className="chatbot-container">
      <History
        messages={messages}
        setCurrentMessageIndex={setCurrentMessageIndex}
      />
      <Conversation
        messages={currentMessageIndex !== null ? messages.slice(0, currentMessageIndex + 1) : messages}
      />
       <img src={logo} alt="Logo" className="logo" />
      <form onSubmit={handleSubmit} className="input-form">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          placeholder="Type a message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default Chatbot;
