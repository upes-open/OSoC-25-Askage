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
    try {
      const response = await fetch("http://localhost/api/authenticated/", {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${bearerToken}`
        }
      });

      if (response.status === 200) return true;
      else if (response.status === 401) return false;
      else throw new Error(`Unexpected status: ${response.status}`);

    } catch (error) { throw new Error("Token verification error"); }
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

      setAuthState("login");
      return;
    }

    // Authenticated!
    setAuthState("chat");
  }

  const fetchDomLoadState = () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      console.log(tabs[0].id)
      chrome.tabs.sendMessage(tabs[0].id, {
        action: "is_dom_loaded"
      }, (response) => {
        if (response === undefined || !response.loaded) {
          setTimeout(() => {
            fetchDomLoadState();
          }, 100);

          return;
        }

        fetchAuthState();
      });
    })
  }

  useEffect(() => {
    fetchDomLoadState();
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
