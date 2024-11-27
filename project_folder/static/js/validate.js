// static/js/validate.js
document.querySelector('form').onsubmit = function(event) {
    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;
    
    if (!email || !password) {
        alert('Please fill in all fields');
        event.preventDefault();
    }
}
