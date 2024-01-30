chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.type === "SEARCH") {
        // Extract the city and state information from the request
        const { city, state } = request;

        // Construct the URL for your API endpoint or server function
        const apiEndpoint = 'http://localhost:5000/search'; // Replace with your actual API endpoint

        // Set up the payload to send to your server
        const payload = { city, state };

        // Make an API call to your server
        fetch(apiEndpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
            .then(response => response.json())
            .then(data => {
                // Once data is received from the server, send it back to the popup
                sendResponse({ success: true, data: data });
            })
            .catch(error => {
                // Handle any errors that occur during the fetch
                console.error('Error fetching data:', error);
                sendResponse({ success: false, error: 'Failed to fetch data.' });
            });

        // Return true to indicate that the response will be sent asynchronously
        return true;
    }

    // Add more message handling as needed
});

// You can add more background functionalities here, such as listening for specific browser events, etc.
