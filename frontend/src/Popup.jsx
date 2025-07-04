import { useEffect, useState } from "react";
import "./Popup.css";
import ChatScreen from "./ChatScreen";
import LoginScreen from "./LoginScreen";
import LoadingScreen from "./LoadingScreen";

function App() {
  const [authState, setAuthState] = useState(null);

  useEffect(() => {
    setAuthState("false");  // Hardcoded: No JS Logic for now
  }, []);

  return (
    <>
      <ChatScreen authState={authState} />
      <LoginScreen authState={authState} />
      <LoadingScreen authState={authState} />
    </>
  );
}

export default App;
