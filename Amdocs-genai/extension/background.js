// background.js for handling messages between popup, content script, and backend API

// Listens for a request from the popup or content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "check-text") {
        // Extract text and send it to backend for analysis
        const text = request.text;
        analyzeText(text).then(response => {
            sendResponse({ result: response });
        }).catch(error => {
            sendResponse({ error: "Error analyzing text" });
        });
    }

    if (request.action === "check-image") {
        // Extract image URL and send it to backend for analysis
        const imageUrl = request.imageUrl;
        analyzeImage(imageUrl).then(response => {
            sendResponse({ result: response });
        }).catch(error => {
            sendResponse({ error: "Error analyzing image" });
        });
    }

    if (request.action === "check-link") {
        // Extract link and send it to backend for analysis
        const link = request.link;
        analyzeLink(link).then(response => {
            sendResponse({ result: response });
        }).catch(error => {
            sendResponse({ error: "Error analyzing link" });
        });
    }

    return true; // Required to handle async responses
});

// Function to analyze text using backend API
async function analyzeText(text) {
    try {
        const response = await fetch("http://localhost:5000/api/analyze-text", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text })
        });

        const result = await response.json();
        return result;  // Return the analysis result from the backend
    } catch (error) {
        console.error("Error analyzing text:", error);
        return { error: "Error analyzing text" };
    }
}

// Function to analyze image using backend API
async function analyzeImage(imageUrl) {
    try {
        const response = await fetch("http://localhost:5000/api/analyze-image", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ imageUrl })
        });

        const result = await response.json();
        return result;  // Return the analysis result from the backend
    } catch (error) {
        console.error("Error analyzing image:", error);
        return { error: "Error analyzing image" };
    }
}

// Function to analyze link using backend API
async function analyzeLink(link) {
    try {
        const response = await fetch("http://localhost:5000/api/analyze-link", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ link })
        });

        const result = await response.json();
        return result;  // Return the analysis result from the backend
    } catch (error) {
        console.error("Error analyzing link:", error);
        return { error: "Error analyzing link" };
    }
}
