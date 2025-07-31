chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "get_session_data") {
    let sessionData = sessionStorage.getItem("askage_session");
    if (sessionData) sessionData = JSON.parse(sessionData);

    sendResponse(sessionData ? sessionData : null);
  }

  if (message.action === "new_session") {
    sessionStorage.setItem("askage_session", JSON.stringify({
      conversation_id: message.conversation_id
    }));
  }

  if (message.action === "save_session_message") {
    let sessionData = sessionStorage.getItem("askage_session");
    if (sessionData) sessionData = JSON.parse(sessionData);

    if (!sessionData) sessionData = { conversation_id: message.conversation_id };

    if (!sessionData["messages"]) {
      sessionData["messages"] = [];
    }

    sessionData["messages"].push({
      type: message.message_type,
      content: message.message_content
    });

    sessionStorage.setItem("askage_session", JSON.stringify(sessionData));
  }

  if (message.action === "get_session_messages") {
    let sessionData = sessionStorage.getItem("askage_session");
    if (sessionData) sessionData = JSON.parse(sessionData);

    if (!sessionData) sendResponse([]);

    let messages = sessionData["messages"];
    if (!messages) messages = [];

    sendResponse(messages);
  }

  return true;  // Keep message channel open
});
