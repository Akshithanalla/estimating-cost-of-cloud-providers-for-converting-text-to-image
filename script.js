// script.js

// Function to validate the form before submission
function validateForm() {
    var textPrompt = document.getElementById("text_prompt").value;
    var imageWidth = document.getElementById("image_width").value;
    var imageHeight = document.getElementById("image_height").value;
    
    // Check if any field is empty
    if (textPrompt === "" || imageWidth === "" || imageHeight === "") {
        alert("All fields are required!");
        return false;
    }

    return true;
}
