document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        // Clear previous alerts
        const errorDiv = document.getElementById("error-message");
        if (errorDiv) errorDiv.remove();

        // Basic validation
        if (!name || !email || !password) {
            displayError("All fields are required.", event);
        } else if (password.length < 6) {
            displayError("Password must be at least 6 characters long.", event);
        }
    });

    function displayError(message, event) {
        // Prevent form submission
        event.preventDefault();

        // Create an error message element
        const errorDiv = document.createElement("div");
        errorDiv.id = "error-message";
        errorDiv.style.color = "red";
        errorDiv.style.marginTop = "10px";
        errorDiv.textContent = message;

        // Insert the error message before the form
        const form = document.querySelector("form");
        form.parentNode.insertBefore(errorDiv, form);
    }
});
