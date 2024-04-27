
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

    <button type="submit" class="send-button" >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="h-5 w-5"><path d="M3.478 2.405a.75.75 0 00-.926.94l2.432 7.905H13.5a.75.75 0 010 1.5H4.984l-2.432 7.905a.75.75 0 00.926.94 60.519 60.519 0 0018.445-8.986.75.75 0 000-1.218A60.517 60.517 0 003.478 2.405z"></path></svg>
    </button>
  </form>
  <img src={logo} alt="Logo" class="logo" />
</div>
    </div>
  );
};

export default Chatbot;
