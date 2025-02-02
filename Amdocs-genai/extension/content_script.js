// Content Script for interacting with the webpage

// Function to extract text content from the page
function extractText() {
    let pageText = document.body.innerText || document.body.textContent;
    return pageText;
}

// Function to extract image sources from the page
function extractImages() {
    const images = Array.from(document.images);
    const imageSources = images.map(img => img.src);
    return imageSources;
}

// Function to extract all links from the page
function extractLinks() {
    const links = Array.from(document.getElementsByTagName('a'));
    const linkURLs = links.map(link => link.href);
    return linkURLs;
}

// Detect when the extension is activated on the page
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "extract-text") {
        // Extract the text from the webpage
        const extractedText = extractText();
        sendResponse({ text: extractedText });
    }

    if (request.action === "extract-images") {
        // Extract all image sources from the webpage
        const extractedImages = extractImages();
        sendResponse({ images: extractedImages });
    }

    if (request.action === "extract-links") {
        // Extract all links from the webpage
        const extractedLinks = extractLinks();
        sendResponse({ links: extractedLinks });
    }

    return true;  // This is required to keep the message channel open for async response
});
