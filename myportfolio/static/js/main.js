// main.js

// Get all navigation links
var navLinks = document.querySelectorAll('nav ul li a');

// Get current URL
var currentUrl = window.location.href;

// Loop through each navigation link
for (var i = 0; i < navLinks.length; i++) {
    // If the navigation link's href matches the current URL
    if (navLinks[i].href === currentUrl) {
        // Add 'active' class to the navigation link
        navLinks[i].classList.add('active');
    }
}