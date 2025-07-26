import "./IncomingChatBubble.css"
import icon from "./assets/icon.png"

function IncomingChatBubble({ message }) {
  return (
    <div className="message ai-message">
      <img className="message-avatar" src={icon} alt="Askage Avatar" />
      <div className="message-text">{message}</div>
    </div>
  );
}

export default IncomingChatBubble;