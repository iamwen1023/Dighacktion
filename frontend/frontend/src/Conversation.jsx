
import React from "react";

const Conversation = ({ messages }) => {
  return (
    <div className="conversation">
      <h2>Conversation</h2>
      <div className="conversation-messages">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.isUser ? "user" : "bot"}`}
          >
            {message.text}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Conversation;
