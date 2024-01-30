document.addEventListener('DOMContentLoaded', function () {
  const searchForm = document.getElementById('searchForm'); // Make sure this element exists
  const cityInput = document.getElementById('cityInput');
  const stateInput = document.getElementById('stateInput');
  const loadingElement = document.getElementById('loading');
  const resultsElement = document.getElementById('results');
  const progressBar = document.getElementById('progressBar'); // Ensure this ID matches your HTML
  const finishedContainer = document.getElementById('finishedContainer'); // Container for finished message and download button
  const downloadButton = document.getElementById('downloadButton');

  searchForm.addEventListener('submit', function (event) {
    event.preventDefault();

    progressBar.style.display = 'block';
    loadingElement.style.display = 'none';
    resultsElement.style.display = 'none';
    finishedContainer.style.display = 'none';

    const city = cityInput.value;
    const state = stateInput.value;

    chrome.runtime.sendMessage({ type: "SEARCH", city, state }, function (response) {
      progressBar.style.display = 'none';

      if (response && response.success) {
        displayResults(response.data);
        prepareDownload(response.data);
        finishedContainer.style.display = 'block'; // Show finished message and download button
      } else {
        resultsElement.textContent = 'Failed to fetch data.';
        resultsElement.style.display = 'block';
      }
    });
  });

  // ... rest of your functions ...
});
