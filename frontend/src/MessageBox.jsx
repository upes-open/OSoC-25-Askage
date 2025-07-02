import React, { useEffect } from "react";
import "./MessageBox.css";

const MessageBox = ({ inputRef }) => {
  useEffect(() => {
    if (inputRef?.current) {
      inputRef.current.focus(); 
    }
  }, []);

  return (
    <div className="message-box">
      <input
        type="text"
        placeholder="Type your message..."
        ref={inputRef}
        className="message-input"
      />
    </div>
  );
};

export default MessageBox;

