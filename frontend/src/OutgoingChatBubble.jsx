import "./OutgoingChatBubble.css";

function OutgoingChatBubble({ message }) {
  return (
    <div className="chat-bubble-container outgoing">
      <div className="outgoing-chat-bubble">{message}</div>
    </div>
  );
}

export default OutgoingChatBubble;
