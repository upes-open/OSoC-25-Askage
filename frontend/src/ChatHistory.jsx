import "./ChatHistory.css";
import InfoChatBubble from "./InfoChatBubble";
import IncomingChatBubble from "./IncomingChatBubble";
import OutgoingChatBubble from "./OutgoingChatBubble";

function ChatHistory({ messages, chatHistoryRef }) {
  return (
    <div id="chat-history" ref={chatHistoryRef}>
      <InfoChatBubble />
    
      {messages.map((msg, index) =>
        msg.type === "outgoing" ? (
          <OutgoingChatBubble key={index} message={msg.content} />
        ) : (
          <IncomingChatBubble key={index} message={msg.content} />
        )
      )}
    </div>
  );
}

export default ChatHistory;
