import "./ChatScreen.css";
import Heading from "./Heading";
import MessageBox from "./MessageBox";
import ChatHistory from "./ChatHistory";

function ChatScreen({ inputRef }) {
  return (
    <div id="chat-screen">
      <Heading />
      <ChatHistory />
      <MessageBox inputRef={inputRef} /> 
    </div>
  );
}

export default ChatScreen;
