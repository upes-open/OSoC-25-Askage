import "./MessageBox.css";

function MessageBox() {
  return (
    <>
      <div id="message">
        <textarea
          id="message-box"
          placeholder="Enter your message here..."
        ></textarea>
      </div>
    </>
  );
}

export default MessageBox;
