function validateForm() {
            let name = document.forms["patientForm"]["name"].value;
            let age = document.forms["patientForm"]["age"].value;
            let email = document.forms["patientForm"]["email"].value;

            let valid = true;

            document.getElementById("nameError").innerHTML = "";
            document.getElementById("ageError").innerHTML = "";
            document.getElementById("emailError").innerHTML = "";

            // Name validation
            if (name.length < 3) {
                document.getElementById("nameError").innerHTML = "Name must be at least 3 characters";
                valid = false;
            }

            // Age validation
            if (age <= 0 || age > 120) {
                document.getElementById("ageError").innerHTML = "Enter valid age";
                valid = false;
            }

            // Email validation
            let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
            if (!email.match(pattern)) {
                document.getElementById("emailError").innerHTML = "Invalid email";
                valid = false;
            }

            return valid;
        }