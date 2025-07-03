import { useRef, useEffect, useState } from "react";
import "./Popup.css";
import ChatScreen from "./ChatScreen";
import LoginScreen from "./LoginScreen";

function App() {
  const [authState, setAuthState] = useState(null);

  useEffect(() => {
    setAuthState(false);  // Display Login Screen (No JS Logic for now)
  }, []);

  return (
    <>
      <ChatScreen authState={authState} />
      <LoginScreen authState={authState} />
    </>
  );
}

export default App;

