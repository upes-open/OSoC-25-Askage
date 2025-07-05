import { useEffect, useState } from "react";
import "./Popup.css";
import ChatScreen from "./ChatScreen";
import LoginScreen from "./LoginScreen";
import LoadingScreen from "./LoadingScreen";

function App() {
  const [authState, setAuthState] = useState("loading");

  function getBearerToken() {
    return new Promise((resolve) => {
      chrome.storage.local.get(["bearer_token"], (result) => {
        resolve(result.bearer_token);
      });
    });
  }

  function deleteBearerToken() {
    return new Promise((resolve) => {
      chrome.storage.local.remove(["bearer_token"], () => {
        resolve();
      });
    });
  }

  async function verifyBearerToken(bearerToken) {
    /*
    TODO: Implement
      - Implement calling GET /authenticated and getting 200/401 with empty body
    */

    const res = await fetch("https://example.com");

    return true;
  }

  async function fetchAuthState() {
    const bearerToken = await getBearerToken();

    // Invalid token
    if (!bearerToken) {
      setAuthState("login");
      return;
    }

    // Verify token
    if (!(await verifyBearerToken(bearerToken))) {
      await deleteBearerToken();
    }

    // Authenticated!
    setAuthState("chat");
  }

  useEffect(() => {
    fetchAuthState();
  }, []);

  return (
    <>
      <ChatScreen authState={authState} />
      <LoginScreen authState={authState} setAuthState={setAuthState} />
      <LoadingScreen authState={authState} />
    </>
  );
}

export default App;
