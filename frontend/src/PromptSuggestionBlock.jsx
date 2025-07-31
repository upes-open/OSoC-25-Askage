import "./PromptSuggestionBlock.css";

function PromptSuggestionBlock({ text, onClick }) {
  return (
    <div onClick={onClick} className="prompt-suggestion-block">
      {text}
    </div>
  );
}

export default PromptSuggestionBlock;
