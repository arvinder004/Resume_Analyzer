document.addEventListener('DOMContentLoaded', function() {
    const signInButton = document.getElementById('signInButton');
    const signInModal = document.getElementById('signInModal');
    const closeBtn = document.querySelector('.close');
    const analyzeButton = document.getElementById('analyzeButton');
    const resumeUpload = document.getElementById('resumeUpload');
    const resumeBuilderButton = document.getElementById('resumeBuilderButton');
    const aboutLink = document.querySelector('nav a[href="#aboutSection"]');
    const servicesLink = document.querySelector('nav a[href="#servicesSection"]');
    const aboutSection = document.getElementById('aboutSection');
    const servicesSection = document.getElementById('servicesSection');

    // Sign-in modal functionality
    if (signInButton && signInModal) {
        signInButton.addEventListener('click', function() {
            signInModal.style.display = 'flex';
        });
    }

    if (closeBtn && signInModal) {
        closeBtn.addEventListener('click', function() {
            signInModal.style.display = 'none';
        });

        window.addEventListener('click', function(event) {
            if (event.target === signInModal) {
                signInModal.style.display = 'none';
            }
        });
    }

    // Resume upload enables analyze button
    if (resumeUpload && analyzeButton) {
        resumeUpload.addEventListener('change', function() {
            analyzeButton.disabled = !(this.files && this.files[0]);
        });
    }

    // Resume analyze button redirection
    if (analyzeButton) {
        analyzeButton.addEventListener('click', function() {
            console.log("Redirecting to /analyze");
            window.location.href = "/analyze";
        });
    }

    // Resume Builder redirection
    if (resumeBuilderButton) {
        resumeBuilderButton.addEventListener('click', function() {
            window.location.href = 'resume_builder.html';
        });
    }

    // Smooth scrolling for About section
    if (aboutLink && aboutSection) {
        aboutLink.addEventListener('click', function(event) {
            event.preventDefault();
            aboutSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    }

    // Smooth scrolling for Services section
    if (servicesLink && servicesSection) {
        servicesLink.addEventListener('click', function(event) {
            event.preventDefault();
            servicesSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    }
});
