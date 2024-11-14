
// Check login status on page load
document.addEventListener("DOMContentLoaded", () => {
    if (localStorage.getItem("isLoggedIn") === "true") {
        showWelcomeScreen(localStorage.getItem("username"));
    } else {
        showLoginScreen();
    }
});

// Function to handle login
function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username && password) {
        // Simulate successful login
        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("username", username);
        showWelcomeScreen(username);
    } else {
        alert("Please enter username and password.");
    }
}

// Function to show the welcome screen
function showWelcomeScreen(username) {
    document.getElementById("loginContainer").style.display = "none";
    document.getElementById("welcomeContainer").style.display = "block";
    document.getElementById("user").innerText = username;
}

// Function to show the login screen
function showLoginScreen() {
    document.getElementById("loginContainer").style.display = "block";
    document.getElementById("welcomeContainer").style.display = "none";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
}

// Function to handle logout
function logout() {
    localStorage.removeItem("isLoggedIn");
    localStorage.removeItem("username");
    showLoginScreen();
}