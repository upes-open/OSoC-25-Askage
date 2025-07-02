import Button from "@mui/material/Button";
import SendIcon from "@mui/icons-material/Send";

function SendButton() {
  return (
    <>
      <Button variant="contained" endIcon={<SendIcon />}>
        Send
      </Button>
    </>
  );
}

export default SendButton;
