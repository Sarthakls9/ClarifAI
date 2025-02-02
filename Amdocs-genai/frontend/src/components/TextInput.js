import React, { useState } from "react";
import "../styles/TextInput.css";

const TextInput = ({ onAnalyze }) => {
  const [inputText, setInputText] = useState("");

  const handleChange = (event) => {
    setInputText(event.target.value);
  };

  const handleAnalyze = () => {
    if (inputText.trim() === "") {
      alert("Please enter some text to verify.");
      return;
    }
    onAnalyze(inputText);
  };

  return (
    <div className="text-input-container">
      <label htmlFor="textInput" className="label">
        Paste text to verify:
      </label>
      <textarea
        id="textInput"
        value={inputText}
        onChange={handleChange}
        placeholder="Enter or paste the text here..."
        className="text-input"
      />
      <button onClick={handleAnalyze} className="analyze-button">
        Analyze
      </button>
    </div>
  );
};

export default TextInput;
