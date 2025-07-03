import { useState, useEffect, useRef } from "react";
import Heading from "./Heading";
import ChatHistory from "./ChatHistory";
import MessageBox from "./MessageBox";
import "./ChatScreen.css";

function ChatScreen({ inputRef }) {
  const [messages, setMessages] = useState([]);
  const initialized = useRef(false);

  const addMessage = (type, content) => {
    setMessages((prev) => [...prev, { type, content }]);
  };

  useEffect(() => {
    if (!initialized.current) {
      addMessage("outgoing", "Hey!");
      addMessage("incoming", "Askage this side!");
      initialized.current = true;
    }
  }, []);

  return (
    <div id="chat-screen">
      <Heading />
      <ChatHistory messages={messages} />
      <MessageBox inputRef={inputRef} />
    </div>
  );
}

export default ChatScreen;
