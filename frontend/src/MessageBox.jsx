import "./MessageBox.css";

function MessageBox({ inputRef }) {
  return (
    <div id="message">
      <input
        type="text"
        id="message-box"
        placeholder="Summarize their profile"
        ref={inputRef}
      />
      <button id="send-button">ASK</button>
    </div>
  );
}

export default MessageBox;

