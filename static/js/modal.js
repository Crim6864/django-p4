// modal.js

$(document).ready(function() {
    // Handle click event for opening login/register modal
    $('#openLoginModal').click(function() {
        $('#loginRegisterModal').modal('show');
    });


    // Function to handle login form submission via AJAX
    $('#loginForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function(response) {
                // Handle successful login response here
                // For example, display a success message or redirect the user
                $('#loginRegisterModal').modal('hide');
                location.reload(); // Reload the page to reflect the logged-in state
                // Display success message
                $('#loginSuccessMessage').text('Login successful!');
            },
            error: function(xhr, status, error) {
                // Handle error response here
                // For example, display an error message to the user
                $('#modalLoginError').text(xhr.responseText);
            }
        });
    });

    // Function to handle registration form submission via AJAX
    $('#registerForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function(response) {
                // Handle successful registration response here
                // For example, display a success message or redirect the user
                $('#loginRegisterModal').modal('hide');
                location.reload(); // Reload the page to reflect the registered user
                // Display success message
                $('#registerSuccessMessage').text('Registration successful!');
            },
            error: function(xhr, status, error) {
                // Handle error response here
                // For example, display an error message to the user
                $('#modalRegisterError').text(xhr.responseText);
            }
        });
    });
});
