
# Frontend (Chrome Extension)

Before contributing, you need to install a local copy of this Chrome extension in your browser.  
_Please make sure you're using a Chromium-based browser like Google Chrome, Brave, or Opera._

## Installation

First, clone the entire repository to your system. Then run this script to install all dependencies:

```sh
cd frontend  # Navigate to the frontend directory
npm install
```

## Install Chrome Extension (One-Time Setup)

Once everything is set up, follow these steps to install the Chrome extension in your browser for testing:

1. Run `npm run build`. This will generate a `/dist` directory.
2. Open `chrome://extensions` in your browser and enable **Developer mode** from the top-right corner.
3. Click the **Load unpacked** button, and select the `/dist` directory that was just generated.
4. Click the extensions icon in your browser’s address bar to view all installed extensions.
5. You’ll see **Askage** listed there. Click the **Pin** icon to make it easily accessible.

Hurray! 🎉 Askage is now installed in your browser!

## Reload Extension

Whenever you make changes to the frontend code, you’ll need to reload the extension to see the updates. Here’s how:

1. In the `/frontend` directory, run `npm run build` to rebuild the extension.
2. Open `chrome://extensions` and click the **Reload** button for the Askage extension.

All done! 🎉 Your changes to Askage are now live.

> [!TIP]
> Keep the `chrome://extensions` page open in a separate tab during development, as you'll need to reload the extension frequently after making changes.

## Contributing

Before contributing, please ensure:

- You've thoroughly tested your code and resolved any errors.
- Your code is properly formatted and follows best practices.

Failure to follow these steps may result in your PR being declined or requiring additional changes.

Once you're ready to contribute your changes to the master repository, follow these steps:

- <TODO: Add steps>

Thank you for contributing to Askage! 💻🚀
