import "./ChatScreen.css";
import Heading from "./Heading";
import MessageBox from "./MessageBox";
import ChatHistory from "./ChatHistory";
import SendButton from "./SendButton";

function ChatScreen() {
  return (
    <>
      <Heading />
      <MessageBox />
      <SendButton />
      <ChatHistory />
    </>
  );
}

export default ChatScreen;
