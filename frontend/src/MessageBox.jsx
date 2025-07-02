import "./MessageBox.css";

function MessageBox() {
  return (
    <div id="message">
      <input type="text" id="message-box" placeholder="Summarize their profile" />
      <button id="send-button">ASK</button>
    </div>
  );
}

export default MessageBox;
