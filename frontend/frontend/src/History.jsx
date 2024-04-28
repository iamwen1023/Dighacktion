
import React from "react";

const Sidebar = ({ messages, setCurrentMessageIndex }) => {
  return (
    <div className="sidebar">
      <h2>Conversation History</h2>
      <ul>
        {/* {messages.map((message, index) => (
          <li key={index} onClick={() => setCurrentMessageIndex(index)}>
            {message.text}
          </li>
        ))} */}
     
      <li className="message-item">Helicobacter récurrents</li>
      <li  className="message-item">Dosage inexium</li>
      <p className="date-heading">Aujourd'hui</p>
      </ul>
      <ul>
      <li className="message-item">Myosite et maladie de Crohn</li>
      <p className="date-heading">Hier</p>
      </ul>
    </div>
  );
};

export default Sidebar;
