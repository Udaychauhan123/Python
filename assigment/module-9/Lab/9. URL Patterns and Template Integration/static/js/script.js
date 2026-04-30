
// 🔍 Live Search Filter
const search = document.getElementById("search");
search.addEventListener("keyup", function() {
    let value = this.value.toLowerCase();
    let doctors = document.querySelectorAll(".doctor");

    doctors.forEach(function(doc) {
        doc.style.display = doc.innerText.toLowerCase().includes(value) ? "block" : "none";
    });
});


// ✨ Scroll Animation
const hiddenElements = document.querySelectorAll(".hidden");

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add("show");
        }
    });
});

hiddenElements.forEach(el => observer.observe(el));


// 🎯 Button Click Effect
document.querySelectorAll(".btn").forEach(btn => {
    btn.addEventListener("click", () => {
        btn.innerText = "Loading...";
        setTimeout(() => {
            btn.innerText = "Done ✓";
        }, 1000);
    });
});

// Form Validation
document.getElementById("contactForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let message = document.getElementById("message").value.trim();

    let valid = true;

    // Clear errors
    document.getElementById("nameError").innerText = "";
    document.getElementById("emailError").innerText = "";
    document.getElementById("msgError").innerText = "";

    // Name validation
    if (name === "") {
        document.getElementById("nameError").innerText = "Name is required";
        valid = false;
    }

    // Email validation
    if (email === "" || !email.includes("@")) {
        document.getElementById("emailError").innerText = "Valid email required";
        valid = false;
    }

    // Message validation
    if (message === "") {
        document.getElementById("msgError").innerText = "Message cannot be empty";
        valid = false;
    }

    // Success
    if (valid) {
        document.getElementById("successMsg").innerText = "Message sent successfully!";
        
        // Reset form
        document.getElementById("contactForm").reset();
    }
});