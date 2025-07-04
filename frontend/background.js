chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "GOOGLE_SIGN_IN") {
    chrome.identity.getAuthToken({ interactive: true }, function (token) {
      if (chrome.runtime.lastError || !token) {
        sendResponse({ error: chrome.runtime.lastError?.message || "No token received" });
      } else {
        sendResponse({ token });
      }
    });

    return true; // Keep sendResponse alive asynchronously
  }
});
