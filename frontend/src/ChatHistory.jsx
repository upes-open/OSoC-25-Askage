import "./ChatHistory.css";
import InfoChatBubble from "./InfoChatBubble";
import IncomingChatBubble from "./IncomingChatBubble";
import OutgoingChatBubble from "./OutgoingChatBubble";

function ChatHistory() {
  return (
    <div id="chat-history">
      <InfoChatBubble />
      <OutgoingChatBubble message="Hey!" />
      <IncomingChatBubble message="I am Askage!!" />
    </div>
  );
}

export default ChatHistory;
