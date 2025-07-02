import "./ChatHistory.css";
import IncomingChatBubble from "./IncomingChatBubble";
import OutgoingChatBubble from "./OutgoingChatBubble";

function ChatHistory() {
  return (
    <div id="chat-history">
      
      <OutgoingChatBubble message="Hey!" />
      <IncomingChatBubble message="I am Askage!!" />

    </div>
  );
}

export default ChatHistory;
