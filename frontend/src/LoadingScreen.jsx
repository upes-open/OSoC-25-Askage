import "./LoadingScreen.css";

function LoadingScreen({ authState }) {
  return (
    <div id="loading-screen" style={{ display: (authState === "loading") ? "flex" : "none" }}>
      <div className="loading-container">
        <div className="loading-spinner"></div>
      </div>
    </div>
  );
}

export default LoadingScreen;
