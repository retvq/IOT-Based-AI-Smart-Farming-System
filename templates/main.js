document.addEventListener('DOMContentLoaded', function () {
    const convertButton = document.getElementById('convertButton');
    const resultContainer = document.getElementById('resultContainer');
    const resultText = document.getElementById('resultText');

    convertButton.addEventListener('click', function () {
        startSpeechRecognition();
    });

    function startSpeechRecognition() {
        const recognition = new webkitSpeechRecognition() || SpeechRecognition();
        recognition.lang = 'en-US';
        recognition.interimResults = true;

        recognition.onresult = function (event) {
            const result = event.results[event.results.length - 1][0].transcript;
            resultText.value = result;

            // Show the result container
            resultContainer.style.display = 'block';

            // Optional: Send the audio data directly to Cloud Functions for additional processing
            sendAudioDataToCloudFunctions(result);
        };

        recognition.onend = function () {
            // Additional logic after recognition ends
        };

        recognition.start();
    }

    function sendAudioDataToCloudFunctions(audioData) {
        // Replace 'YOUR_CLOUD_FUNCTION_URL' with the URL of your deployed Cloud Function
        $.ajax({
            url: 'YOUR_CLOUD_FUNCTION_URL',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ audioData }),
            success: function (data) {
                console.log('Transcription:', data.transcription);
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    }
});
