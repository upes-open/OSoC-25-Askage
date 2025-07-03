import "./IncomingChatBubble.css";

function IncomingChatBubble({ message }) {
  return (
    <div className="message ai-message">

      <div className="ai-avatar">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" fill="url(#gradient)" />

          <path d="M8 14s1.5 2 4 2 4-2 4-2" stroke="white" strokeWidth="1.5" strokeLinecap="round" />

          <circle cx="9" cy="9" r="1" fill="white" />
          <circle cx="15" cy="9" r="1" fill="white" />

          <defs>
            <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#667eea" />
              <stop offset="100%" stopColor="#764ba2" />
            </linearGradient>
          </defs>
        </svg>
      </div>

      <div className="message-text">{message}</div>
    </div>
  );
}

export default IncomingChatBubble;