import React, { useState } from "react";
import "../styles/LinkInput.css";

const LinkInput = ({ onAnalyze }) => {
  const [url, setUrl] = useState("");

  const handleChange = (event) => {
    setUrl(event.target.value);
  };

  const handleAnalyze = () => {
    if (url.trim() === "") {
      alert("Please enter a valid URL.");
      return;
    }
    onAnalyze(url);
  };

  return (
    <div className="link-input-container">
      <label htmlFor="linkInput" className="label">
        Enter the URL to verify:
      </label>
      <input
        type="url"
        id="linkInput"
        placeholder="https://example.com"
        value={url}
        onChange={handleChange}
        className="url-input"
      />
      <button onClick={handleAnalyze} className="analyze-button">
        Analyze
      </button>
    </div>
  );
};

export default LinkInput;
