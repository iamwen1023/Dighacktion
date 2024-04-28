
import React from "react";

const Sidebar = ({ messages, setCurrentMessageIndex }) => {
  return (
    <div className="sidebar">
      <h2>Message History</h2>
      <ul>
        {/* {messages.map((message, index) => (
          <li key={index} onClick={() => setCurrentMessageIndex(index)}>
            {message.text}
          </li>
        ))} */}
      </ul>
    </div>
  );
};

export default Sidebar;
