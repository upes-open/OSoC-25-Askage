const googleLogin = () => {
  chrome.runtime.sendMessage({ type: "GOOGLE_SIGN_IN" }, (response) => {
    if (chrome.runtime.lastError) {
      console.error("Runtime error:", chrome.runtime.lastError.message);
      return;
    }

    if (response.error) {
      console.error("Login failed:", response.error);
    } else {
      console.log("Google Token:", response.token);

      // Optional: fetch profile
      fetch("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", {
        headers: {
          Authorization: `Bearer ${response.token}`
        }
      })
        .then(res => res.json())
        .then(profile => {
          console.log("User profile:", profile);
        })
        .catch(err => {
          console.error("Profile fetch error:", err);
        });
    }
  });
};
