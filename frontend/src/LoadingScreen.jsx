import "./LoadingScreen.css";

function LoadingScreen({ authState }) {
  return (
    <div id="loading-screen" style={{ display: (authState === "loading") ? "flex" : "none" }}>
      <div id="loader"></div>

      <div id="loader-screen-info">
        Great things take time...
      </div>
    </div>
  );
}

export default LoadingScreen;
