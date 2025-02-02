# **🔍 ClarifAI Web Extension**  

**Empower yourself to verify the authenticity of online content, combat misinformation, and promote a trustworthy digital ecosystem.**  
ClarifAI is your real-time fact-checking companion for web links, images, and text inputs. By leveraging advanced AI models, it delivers trust scores and insights to help you make informed decisions online.  

---

## 🚀 **Features**
- **🔗 Link Analysis:** Fact-check entire web pages and get trust scores based on verified content.  
- **🖼️ Image Analysis:** Detect deepfakes and identify image manipulations.  
- **✍️ Text Analysis:** Verify statements and highlight misinformation with contextual insights.  
- **✨ Intuitive UI:** Simple, clean interface for quick and effective content verification.  
- **⚡ Real-Time Scoring:** Get results in seconds with advanced AI-backed processing.  

---

## 🏗️ **Project Structure**

```
ClarifAI/
├── backend/
│   ├── app.py               # Backend API routes
│   ├── routes/               # Route-specific logic
│   ├── models/               # NLP and image authentication models
│   └── utils/                # Helper functions
├── database/
│   ├── db_config.py          # Database configurations
│   └── fact_cache.db         # Local fact cache
├── extension/
│   ├── popup.html            # Popup for user interaction
│   ├── popup.js              # Popup logic
│   ├── styles.css            # Popup styles
│   └── background.js         # Background event handling
└── frontend/
    ├── public/
    └── src/
```

---

## 🛠️ **Tech Stack**
### **Backend**
- 🐍 Python (Flask)
- 🤗 Hugging Face Transformers for NLP and Image Analysis  
- 🔧 TensorFlow for deepfake detection  

### **Frontend**
- ⚛️ React.js  
- 🎨 CSS for a clean, modern UI  

### **APIs & Libraries**
- 🧠 Hugging Face Models  
- 📊 Custom Fact Cache Database  

---

## 🧑‍💻 **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/Sarthakls9/clarifai-web-extension.git
cd clarifai-web-extension
```

### **2. Set Up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Start Backend Server**
```bash
python backend/app.py
```

### **5. Load Extension**
1. Open Chrome and navigate to `chrome://extensions/`
2. Enable **Developer Mode**
3. Click **Load Unpacked** and select the `extension/` directory

---

## 🌟 **Usage Guide**
1. **Open the Extension:** Click the ClarifAI icon from the browser toolbar.  
2. **Verify Links:** Paste or navigate to a web link to analyze credibility.  
3. **Upload Images:** Detect possible deepfakes with a simple image upload.  
4. **Analyze Text:** Paste statements and check for misinformation.  
5. **View Results:** Trust scores and insights are displayed in real-time.  

---


## 🧪 **Testing**
Run the test suite to ensure everything is working correctly:  
```bash
pytest tests/
```

---

## 🧩 **Future Enhancements**
- 🌍 **Multi-Language Support:** Detect misinformation in regional languages.  
- 📱 **Mobile Version:** Android/iOS compatibility.  
- 🧑‍🤝‍🧑 **Crowdsourced Fact-Checking:** Community-driven verification.  
- 🖥️ **Advanced Media Detection:** Support for GIFs and videos.  

---

## 👨‍💻 **Contributors**
- Sarthak Gupta ([GitHub Profile](https://github.com/Sarthakls9))  

---
