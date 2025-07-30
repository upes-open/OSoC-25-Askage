import { useState, useEffect, useRef } from "react";
import Heading from "./Heading";
import ChatHistory from "./ChatHistory";
import MessageBox from "./MessageBox";
import "./ChatScreen.css";

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
  const [conversationId, setConversationId] = useState(null);
  const [shouldCreateConversation, setShouldCreateConversation] = useState(false);

  const addMessage = (type, content, silent = false) => {
    setMessages((prev) => [...prev, { type, content }]);
    scrollChatHistoryToBottom();

    if (!silent) saveConversationMessage(type, content);
  };

  const scrollChatHistoryToBottom = () => {
    setTimeout(() => {
      if (chatHistoryRef.current) {
        chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
      }
    }, 1);
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
    const webpageContent = webpageContentRaw.slice(webpageContentRaw.indexOf(":") + 1);
    let response = "Apologies, there was an issue on my end.";

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
        })
      });

      if (res.status == 200) {
        response = (await res.json())["response"];
      } else {
        console.error(`Unexpected status: ${res.status}`);
      }
    } catch (error) {
      console.error("broadcastMessage error:", error);
    }

    // Add response message
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
    setShouldCreateConversation(true);
  }

  const saveConversationSession = async (temp_conversation_id) => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.tabs.sendMessage(tab.id, {
      action: "new_session",
      conversation_id: temp_conversation_id
    });
  }

  const saveConversationMessage = async (type, content) => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.tabs.sendMessage(tab.id, {
      action: "save_session_message",
      message_type: type,
      message_content: content,
      conversation_id: conversationId
    });
  }

  const createConversation = async () => {
    if (!shouldCreateConversation) return;

    const res = await fetch(`http://localhost/api/conversations/`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${bearerToken}`
      }
    });

    try {
      const temp_conversation_id = (await res.json())["conversation_id"];

      setConversationId(temp_conversation_id);
      saveConversationSession(temp_conversation_id);

      addMessage("incoming", "Hello! How can I assist you today?");
    } catch (err) {
      console.error(err);
    }
  }

  const loadStoredMessages = async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.tabs.sendMessage(tab.id, {
      action: "get_session_messages"
    }, (response) => {
      response.forEach(message => {
        addMessage(message.type, message.content, true);
      });

      setTimeout(() => {
        scrollChatHistoryToBottom();
      }, 1);
    });
  }

  const storedConversationStatus = async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    // Get stored session
    chrome.tabs.sendMessage(tab.id, {
      action: "get_session_data"
    }, (response) => {
      if (!response) {
        createConversation();
        return;
      }

      const storedConversationId = response.conversation_id;

      if (!storedConversationId) {
        createConversation();
        return;
      }

      setConversationId(storedConversationId);
      loadStoredMessages();
    });
  }

  useEffect(() => {
    if (shouldCreateConversation) {
      setShouldCreateConversation(false);

      storedConversationStatus();
    }
  }, [shouldCreateConversation]);

  useEffect(() => {
    if (!initialized.current) {
      refreshBearerToken();
      initialized.current = true;
    }
  }, []);

  const inputFocus = () => {
    setTimeout(() => {
      inputRef.current?.focus();
    }, 1);
  }

  useEffect(() => {
    if (authState === "chat" && conversationId != null) {
      inputFocus();
    }
  }, [authState, conversationId]);

  useEffect(() => {
    window.addEventListener("keydown", (e) => {
      inputFocus();
    });

    return () => {
      window.removeEventListener("focus", inputFocus);
    };
  }, []);

  return (
    <>
      <div id="chat-screen" style={{ display: (authState === "chat" && conversationId != null) ? "flex" : "none" }}>
        <Heading />
        <ChatHistory chatHistoryRef={chatHistoryRef} messages={messages} />
        <MessageBox inputRef={inputRef} sendMessage={sendMessage} enabled={messageBoxEnabled} />
      </div>

      <div id="creating-conversation-screen" style={{ display: (authState === "chat" && conversationId == null) ? "flex" : "none" }}>
        <div className="loading-container">
          <div className="loading-spinner"></div>
        </div>
      </div>
    </>
  );
}

export default ChatScreen;
