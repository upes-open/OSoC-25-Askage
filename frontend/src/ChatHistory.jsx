import "./ChatHistory.css";
import IncomingChatBubble from "./IncomingChatBubble";
import OutgoingChatBubble from "./OutgoingChatBubble";

function ChatHistory({ messages }) {
  return (
    <div id="chat-history">
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
