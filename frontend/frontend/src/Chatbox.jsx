
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
    <div class="container_right">
      <div class="conversation">
    <Conversation
      messages={currentMessageIndex !== null ? messages.slice(0, currentMessageIndex + 1) : messages}
    />
  </div>
  <form onSubmit={handleSubmit} class="input-form">
    <input
      type="text"
      value={input}
      onChange={handleInputChange}
      placeholder="Type a message..."
      class="input-field"
    />
    <button type="submit" class="send-button" >Send</button>
  </form>
  <img src={logo} alt="Logo" class="logo" />
</div>
    </div>
  );
};

export default Chatbot;
