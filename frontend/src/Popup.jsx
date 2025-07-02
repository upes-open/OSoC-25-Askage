import { useRef, useEffect } from "react";
import "./Popup.css";
import ChatScreen from "./ChatScreen";

function App() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current?.focus(); 
  }, []);

  return (
    <>
      <ChatScreen inputRef={inputRef} />
    </>
  );
}

export default App;

