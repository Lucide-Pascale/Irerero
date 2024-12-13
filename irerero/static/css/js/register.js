const step1Form = document.getElementById('step1');
const step2Form = document.getElementById('step2');
const step3Form = document.getElementById('step3');
const nextStepButton = document.getElementById('nextStep');
const nextStep2Button = document.getElementById('nextStep2');
const backStep1Button = document.getElementById('backStep1');
const backStep2Button = document.getElementById('backStep2');

nextStepButton.addEventListener('click', () => {
    // Only proceed if the form is valid
    if (validateForm()) {
        step1Form.style.display = 'none'; // Hide step 1
        step2Form.style.display = 'block'; // Show step 2
    }
});

nextStep2Button.addEventListener('click', () => {
    step2Form.style.display = 'none'; // Hide step 2
    step3Form.style.display = 'block'; // Show step 3
});

backStep1Button.addEventListener('click', () => {
    step2Form.style.display = 'none'; // Hide step 2
    step1Form.style.display = 'block'; // Show step 1
});

backStep2Button.addEventListener('click', () => {
    step3Form.style.display = 'none'; // Hide step 3
    step2Form.style.display = 'block'; // Show step 2
});

function validateForm() {
    let isValid = true;

    // Validate First Name
    const firstname = document.getElementById('firstname');
    if (!/^[A-Za-z]+$/.test(firstname.value)) {
        document.getElementById('firstnameError').textContent = 'First name should only contain letters.';
        isValid = false;
    } else {
        document.getElementById('firstnameError').textContent = '';  // Clear the error
    }

    // Validate Second Name
    const secondname = document.getElementById('secondname');
    if (!/^[A-Za-z]+$/.test(secondname.value)) {
        document.getElementById('secondnameError').textContent = 'Second name should only contain letters.';
        isValid = false;
    } else {
        document.getElementById('secondnameError').textContent = '';  // Clear the error
    }

    // Validate ID Number
    const idnumber = document.getElementById('idnumber');
    if (!/^\d+$/.test(idnumber.value)) {
        document.getElementById('idnumberError').textContent = 'ID number should only contain digits.';
        isValid = false;
    } else {
        document.getElementById('idnumberError').textContent = '';  // Clear the error
    }

    // Validate Email
    const email = document.getElementById('email');
    if (!/\S+@\S+\.\S+/.test(email.value)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        isValid = false;
    } else {
        document.getElementById('emailError').textContent = '';  // Clear the error
    }

    // Validate Contact Number
    const contact = document.getElementById('contact');
    if (!/^\d+$/.test(contact.value)) {
        document.getElementById('contactError').textContent = 'Contact number should only contain digits.';
        isValid = false;
    } else {
        document.getElementById('contactError').textContent = '';  // Clear the error
    }

    return isValid;
}
