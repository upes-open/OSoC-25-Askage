import "./LoadingScreen.css";

function LoadingScreen({ authState }) {
  return (
    <div id="loading-screen" style={{ display: (authState === "loading") ? "flex" : "none" }}>
      add loading screen code here...
    </div>
  );
}

export default LoadingScreen;
