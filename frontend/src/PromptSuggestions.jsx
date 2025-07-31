import { useEffect, useState } from "react";
import PromptSuggestionBlock from "./PromptSuggestionBlock";
import "./PromptSuggestions.css";

function PromptSuggestions({ suggestions, setMessageText, inputRef }) {
  return (
    <div id="prompt-suggestions-container">
      {suggestions.map((text, i) => {
        return <PromptSuggestionBlock onClick={() => {
          setMessageText(text);
          inputRef.current?.focus();
        }} text={text} />
      })}
    </div>
  );
}

export default PromptSuggestions;
