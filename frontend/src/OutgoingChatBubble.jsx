import "./OutgoingChatBubble.css";

function OutgoingChatBubble({ message }) {
  return (
    <div id="chat-bubble-container" style={{ justifyContent: "right" }}>
      <div id="outgoing-chat-bubble">{message}</div>
    </div>
  );
}

export default OutgoingChatBubble;
