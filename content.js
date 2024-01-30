// content.js

// Extract text from the currently active webpage (you can customize this part)
const extractedText = document.body.innerText;

// Send the extracted text to the background script
chrome.runtime.sendMessage({ text: extractedText }, response => {
    console.log(response); // You can handle the response here
});
