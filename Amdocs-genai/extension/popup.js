// Function to check the text input
document.getElementById('check-text-btn').addEventListener('click', function() {
    const textInput = document.getElementById('text-input').value.trim();

    if (textInput === "") {
        alert('Please enter some text to check.');
        return;
    }

    // Send the text to the background script for processing
    chrome.runtime.sendMessage(
        { type: 'check-text', data: textInput },
        function(response) {
            displayResult('text', response);
        }
    );
});

// Function to check the link input
document.getElementById('check-link-btn').addEventListener('click', function() {
    const linkInput = document.getElementById('link-input').value.trim();

    if (linkInput === "") {
        alert('Please enter a valid URL to check.');
        return;
    }

    // Send the link to the background script for processing
    chrome.runtime.sendMessage(
        { type: 'check-link', data: linkInput },
        function(response) {
            displayResult('link', response);
        }
    );
});

// Function to check the image input
document.getElementById('check-image-btn').addEventListener('click', function() {
    const imageInput = document.getElementById('image-input').files[0];

    if (!imageInput) {
        alert('Please upload an image to check.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput);

    // Send the image to the background script for processing
    chrome.runtime.sendMessage(
        { type: 'check-image', data: formData },
        function(response) {
            displayResult('image', response);
        }
    );
});

// Function to display the result in the popup
function displayResult(type, response) {
    let resultElement;

    // Determine the result display area based on the input type
    if (type === 'text') {
        resultElement = document.getElementById('text-result');
    } else if (type === 'link') {
        resultElement = document.getElementById('link-result');
    } else if (type === 'image') {
        resultElement = document.getElementById('image-result');
    }

    // Clear any previous result
    resultElement.innerHTML = '';

    if (response && response.success) {
        // Show the trust score or authenticity result
        resultElement.innerHTML = `
            <strong>Trust Score: </strong>${response.score}<br>
            <strong>Result: </strong>${response.message}
        `;
    } else {
        resultElement.innerHTML = `
            <strong>Error: </strong>There was an issue processing the request.
        `;
    }
}
