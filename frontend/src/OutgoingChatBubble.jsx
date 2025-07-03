import "./OutgoingChatBubble.css";

function OutgoingChatBubble({ message }) {
  return (
    <div id="chat-bubble-container" style={{ justifyContent: "right" }}>
      {/* <div id="outgoing-chat-bubble">{message}</div> */}
      <div className={'message user-message'}>
            <div className="message-content">
              <div className="message-text">{message}</div>
            </div>
          </div>
      
    </div>
  );
}

export default OutgoingChatBubble;