document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const signupPage = document.querySelector(".signup-page");  // Target the signup page container

    // Set the background image dynamically on the signup page container
    signupPage.style.backgroundImage = "url('/static/image02.jpg')";
    signupPage.style.backgroundSize = "cover";  // Ensures the background covers the entire container without zooming
    signupPage.style.backgroundPosition = "center";  // Centers the background image
    signupPage.style.backgroundAttachment = "fixed";  // Optional: Adds parallax effect on scroll

    form.addEventListener("submit", function (event) {
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (!name || !email || !password) {
            alert("All fields are required!");
            event.preventDefault(); // Prevent form submission
        } else if (password.length < 6) {
            alert("Password must be at least 6 characters long.");
            event.preventDefault();
        }
    });
});
