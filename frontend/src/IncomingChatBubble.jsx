import "./IncomingChatBubble.css";

function IncomingChatBubble({ message }) {
  return (
    <div id="chat-bubble-container" style={{ justifyContent: "left" }}>
      <div id="incoming-chat-bubble">{message}</div>
    </div>
  );
}

export default IncomingChatBubble;
