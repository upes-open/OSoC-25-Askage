import "./ChatScreen.css";
import Heading from "./Heading";
import MessageBox from "./MessageBox";
import ChatHistory from "./ChatHistory";

function ChatScreen() {
  return (
    <>
      <Heading />
      <ChatHistory />
      <MessageBox />
    </>
  );
}

export default ChatScreen;
