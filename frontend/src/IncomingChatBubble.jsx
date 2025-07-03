import "./IncomingChatBubble.css";

function IncomingChatBubble({ message }) {
  return (
    <div className="chat-bubble-container incoming">
      <div className="incoming-chat-bubble">{message}</div>
    </div>
  );
}

export default IncomingChatBubble;
