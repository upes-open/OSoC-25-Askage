import "./OutgoingChatBubble.css";

function OutgoingChatBubble({ message }) {
  return (
    <div className="message user-message">
      <div className="message-text">{message}</div>
    </div>
  );
}

export default OutgoingChatBubble;