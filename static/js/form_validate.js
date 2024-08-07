document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('signupForm'); // Adjust ID if needed

    form.addEventListener('submit', function(event) {
        let isValid = true;

        // Example of validation logic
        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;

        // Validate username
        if (username.trim() === '') {
            isValid = false;
            document.getElementById('usernameError').innerText = 'Username is required.';
        } else {
            document.getElementById('usernameError').innerText = '';
        }

        // Validate password
        if (password.trim() === '') {
            isValid = false;
            document.getElementById('passwordError').innerText = 'Password is required.';
        } else {
            document.getElementById('passwordError').innerText = '';
        }

        // If form is invalid, prevent submission
        if (!isValid) {
            event.preventDefault();
        }
    });
});
