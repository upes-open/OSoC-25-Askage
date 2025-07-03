chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === "GOOGLE_SIGN_IN") {
        chrome.identity.getAuthToken({ interactive: true }, function (token) {
            alert(token)
        });

        return true; // Needed to keep sendResponse alive
    }
});
