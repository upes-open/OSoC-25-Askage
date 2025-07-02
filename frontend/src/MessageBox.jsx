import "./MessageBox.css";
import Button from "@mui/material/Button";
import SendIcon from "@mui/icons-material/Send";

function MessageBox() {
  return (
    <>
      <div id="message">
        <textarea id="message-box" placeholder="Ask"></textarea>
        <Button variant="contained" endIcon={<SendIcon />}>
          Send
        </Button>
      </div>
    </>
  );
}

export default MessageBox;
