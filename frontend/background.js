const redirectUri = chrome.identity.getRedirectURL("provider_cb");
const client_id = "712242987155-c2f5stg43cs59i69ir06ktb2p02shgqk.apps.googleusercontent.com";
const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${client_id}&response_type=code&redirect_uri=${encodeURIComponent(redirectUri)}&scope=openid%20email%20profile&prompt=consent`;

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "GOOGLE_SIGN_IN") {

    // Remove cached token (if any)
    chrome.identity.getAuthToken({ interactive: false }, (token) => {
      if (token) {
        chrome.identity.removeCachedAuthToken({ token }, () => {
          fetch(`https://accounts.google.com/o/oauth2/revoke?token=${token}`)
            .then(() => startLoginFlow(sendResponse))
            .catch(() => sendResponse(false));
        });

      } else startLoginFlow(sendResponse);
    });

    return true; // Keep sendResponse alive async
  }
});

function startLoginFlow(sendResponse) {
  chrome.identity.launchWebAuthFlow({ url: authUrl, interactive: true }, (redirectUrl) => {
    if (chrome.runtime.lastError || !redirectUrl) {
      sendResponse(false);
      return;
    }

    const url = new URL(redirectUrl);
    const code = url.searchParams.get("code");
    authenticateGoogle(code, sendResponse);
  });
}

async function authenticateGoogle(code, sendResponse) {
  /*
  TODO: Implement
    - Send code to backend and receive bearer_token in response body JSON
    - Then, store that token in chrome.storage.local
    - Return true or false depending upon success or not
  */

  try {
    const res = await fetch("https://example.com");

    const bearerToken = "1234";  // Let's say we got it from backend

    await saveBearer(bearerToken);
    sendResponse(true);
  } catch (err) {
    sendResponse(false);
  }
}

function saveBearer(bearerToken) {
  return new Promise((resolve) => {
    chrome.storage.local.set({"bearer_token": bearerToken}, () => resolve());
  })
}