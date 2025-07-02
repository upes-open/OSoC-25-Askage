import React, { useRef } from "react";
import MessageBox from "./MessageBox";
import "./Popup.css";

const Popup = () => {
  const inputRef = useRef(null); 

  return (
    <div className="popup-container">
      <MessageBox inputRef={inputRef} />
    </div>
  );
};

export default Popup;

