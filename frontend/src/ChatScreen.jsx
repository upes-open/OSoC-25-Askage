import "./ChatScreen.css";
import Heading from "./Heading";
import MessageBox from "./MessageBox";
import ChatHistory from "./ChatHistory";

function ChatScreen() {
  return (
    <div id="chat-screen">
      <Heading />
      <ChatHistory />
      <MessageBox />
    </div>
  );
}

export default ChatScreen;
