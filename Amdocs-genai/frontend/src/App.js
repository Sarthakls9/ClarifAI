import React, { useState } from "react";
import LinkInput from "./components/LinkInput";
import ImageInput from "./components/ImageInput";
import TextInput from "./components/TextInput";
import ResultsDisplay from "./components/ResultsDisplay";
import "./styles/app.css";

const App = () => {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleLinkAnalysis = async (link) => {
    setLoading(true);
    try {
      const response = await fetch("/api/analyze-link", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ link }),
      });
      const data = await response.json();
      setAnalysisResult(data);
    } catch (error) {
      console.error("Error analyzing the link:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleImageAnalysis = async (image) => {
    setLoading(true);
    const formData = new FormData();
    formData.append("image", image);

    try {
      const response = await fetch("/api/analyze-image", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setAnalysisResult(data);
    } catch (error) {
      console.error("Error analyzing the image:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleTextAnalysis = async (text) => {
    setLoading(true);
    try {
      const response = await fetch("/api/analyze-text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setAnalysisResult(data);
    } catch (error) {
      console.error("Error analyzing the text:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>ClarifAI - Misinformation Verifier</h1>
      <div className="inputs-container">
        <LinkInput onAnalyze={handleLinkAnalysis} />
        <ImageInput onAnalyze={handleImageAnalysis} />
        <TextInput onAnalyze={handleTextAnalysis} />
      </div>
      {loading && <div className="loading-message">Analyzing...</div>}
      {analysisResult && <ResultsDisplay result={analysisResult} />}
    </div>
  );
};

export default App;
