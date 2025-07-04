import { useState, useEffect, useRef } from "react";
import Heading from "./Heading";
import ChatHistory from "./ChatHistory";
import MessageBox from "./MessageBox";
import "./ChatScreen.css";
import backgroundImage from "./assets/background.svg"

function ChatScreen({ authState }) {
  const [messages, setMessages] = useState([]);
  const initialized = useRef(false);
  const inputRef = useRef(null);

  const addMessage = (type, content) => {
    setMessages((prev) => [...prev, { type, content }]);
  };

  useEffect(() => {
    if (!initialized.current) {
      addMessage("incoming", "Hey! What do you need help with today?");
      addMessage("outgoing", "Can you help me summarize this person's work experience in a few sentences?");
      addMessage("incoming", "Here's a concise summary...");
      addMessage("incoming", "Thanks");
      initialized.current = true;
    }
  }, []);

  useEffect(() => {
    if (authState === true) inputRef.current?.focus();
  }, authState);

  return (
    <div id="chat-screen" style={{ display: (authState === "true") ? "flex" : "none", backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url(${backgroundImage})` }}>
      <Heading />
      <ChatHistory messages={messages} />
      <MessageBox inputRef={inputRef} />
    </div>
  );
}

export default ChatScreen;
