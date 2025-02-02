import React, { useState } from "react";
import "../styles/ImageInput.css";

const ImageInput = ({ onAnalyze }) => {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type.startsWith("image/")) {
      setSelectedImage(file);
    } else {
      alert("Please select a valid image file.");
    }
  };

  const handleAnalyze = () => {
    if (!selectedImage) {
      alert("Please upload an image to verify.");
      return;
    }
    onAnalyze(selectedImage);
  };

  return (
    <div className="image-input-container">
      <label htmlFor="imageInput" className="label">
        Upload an Image to verify:
      </label>
      <input
        type="file"
        id="imageInput"
        accept="image/*"
        onChange={handleFileChange}
        className="file-input"
      />
      {selectedImage && (
        <div className="image-preview">
          <img
            src={URL.createObjectURL(selectedImage)}
            alt="Selected Preview"
            className="preview-img"
          />
        </div>
      )}
      <button onClick={handleAnalyze} className="analyze-button">
        Analyze
      </button>
    </div>
  );
};

export default ImageInput;
