
# Frontend (Chrome Extension)

Welcome! Before contributing, please set up a local copy of this Chrome extension.  
_Make sure you're using a Chromium-based browser such as Google Chrome, Brave, or Opera._

## 🚀 Installation

Clone the repository and install dependencies:

```sh
cd frontend  # Navigate to the frontend directory
npm install  # Install project dependencies
```

## 🧩 Load the Chrome Extension (One-Time Setup)

Follow these steps to install the extension in your browser:

1. Run `npm run build` to generate the `/dist` directory.
2. Go to `chrome://extensions` in your browser.
3. Enable **Developer mode** (toggle in the top-right corner).
4. Click **Load unpacked** and select the `/dist` directory.
5. Click the extensions icon in the browser’s address bar.
6. Find **Askage** and click the **Pin** icon to make it easily accessible.

✅ Askage is now installed and ready to use! 🎉

## 🔁 Reloading the Extension

To see changes after editing the code:

1. Run `npm run build` inside the `/frontend` directory.
2. Go to `chrome://extensions` and click **Reload** under the Askage extension.

> [!TIP]  
> Keep the `chrome://extensions` page open during development for quick reloading.

## 🤝 Contributing

Before submitting a PR, please ensure:

- Your code is tested and free of errors.
- You’ve followed proper formatting and best practices.

### Submit a Pull Request

1. Push your changes to your forked repository.
2. Open a pull request to the master branch using the format:  
   `#<issue-number> - <feature-title>`  
   Example: `#5 - Added basic authentication`

3. Wait for a mentor to review your PR. Monitor for any requested changes.

Thanks for contributing to **Askage**! 💻🚀
