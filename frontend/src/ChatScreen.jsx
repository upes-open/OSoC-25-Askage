import { useState, useEffect, useRef } from "react";
import Heading from "./Heading";
import ChatHistory from "./ChatHistory";
import MessageBox from "./MessageBox";
import "./ChatScreen.css";
import backgroundImage from "./assets/background.svg"

function ChatScreen({ authState }) {
  const [messages, setMessages] = useState([]);
  const initialized = useRef(false);
  const inputRef = useRef(null);
  const [messageBoxEnabled, setMessageBoxEnabled] = useState(true);
  const chatHistoryRef = useRef(null);
  const [webpageContentRaw, setWebpageContent] = useState("");
  const [message, setMessage] = useState("");
  const [scrapeCounter, setScrapeCounter] = useState(0);
  const [bearerToken, setBearerToken] = useState("");

  const addMessage = (type, content) => {
    setMessages((prev) => [...prev, { type, content }]);
    scrollChatHistoryToBottom();
  };

  const scrollChatHistoryToBottom = () => {
    setTimeout(() => {
      if (chatHistoryRef.current) {
        chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
      }
    }, 0);
  };

  const sendMessage = (tempMessage) => {
    setMessage(tempMessage);

    setMessageBoxEnabled(false);
    addMessage("outgoing", tempMessage);

    reloadWebpageContent();
  };

  useEffect(() => {
    if (webpageContentRaw) {
      broadcastMessage(message);
    }
  }, [webpageContentRaw]);

  const reloadWebpageContent = async () => {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true
    });

    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => document.body.innerText
    }, (results) => {
      setScrapeCounter(prev => prev + 1);
      setWebpageContent(`${scrapeCounter.toString()}:${results[0].result}`);
    });
  };

  const broadcastMessage = async (message) => {
    const webpageContent = webpageContentRaw.split(":")[1];
    bearerToken = localStorage.getItem("bearerToken");
    const conversationId = '0000'; // Replace with your actual conversation ID variable
    const response = "<example>";

    try {
      const res = await fetch(`http://localhost/api/conversations/${conversationId}/messages/`, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${bearerToken}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
          webpage_content: webpageContent,
        }),
      });

      if (res.status === 200) {
        const data = await res.json();
        response = data.response;
      } else {
        console.error(`Unexpected status: ${res.status}`);
      }
    } catch (error) {
      console.error("broadcastMessage error:", error);
    }

    addMessage("incoming", response);
    setMessageBoxEnabled(true);
  };


  function getBearerToken() {
    return new Promise((resolve) => {
      chrome.storage.local.get(["bearer_token"], (result) => {
        resolve(result.bearer_token);
      });
    });
  }

  const refreshBearerToken = async () => {
    setBearerToken(await getBearerToken());
  }

  useEffect(() => {
    if (!initialized.current) {
      refreshBearerToken();

      addMessage("incoming", "Hello");
      initialized.current = true;
    }
  }, []);

  useEffect(() => {
    if (authState === "chat") inputRef.current?.focus();
  }, [authState]);

  return (
    <div id="chat-screen" style={{ display: (authState === "chat") ? "flex" : "none", backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url(${backgroundImage})` }}>
      <Heading />
      <ChatHistory chatHistoryRef={chatHistoryRef} messages={messages} />
      <MessageBox inputRef={inputRef} sendMessage={sendMessage} enabled={messageBoxEnabled} />
    </div>
  );
}

export default ChatScreen;
