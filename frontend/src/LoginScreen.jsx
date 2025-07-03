import "./LoginScreen.css";

function LoginScreen({ authState }) {
  return (
    <div id="login-screen" style={{ display: (authState === "false") ? "flex" : "none" }}>
      add login screen code here...
    </div>
  );
}

export default LoginScreen;
