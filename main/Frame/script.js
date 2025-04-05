document.addEventListener('DOMContentLoaded', function() {
    // Sign-in Modal Logic
    const signInButton = document.getElementById('signInButton');
    const signInModal = document.getElementById('signInModal');
    const closeBtn = document.querySelectorAll('.close')[0]; // Select the first close button

    signInButton.addEventListener('click', function() {
        signInModal.style.display = 'flex';
    });

    closeBtn.addEventListener('click', function() {
        signInModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === signInModal) {
            signInModal.style.display = 'none';
        }
    });

    // Register Modal Logic
    const registerButton = document.getElementById('registerButton');
    const registerModal = document.getElementById('registerModal');
    const registerCloseBtn = document.querySelectorAll('.close')[1]; // Select the second close button

    registerButton.addEventListener('click', function() {
        registerModal.style.display = 'flex';
    });

    registerCloseBtn.addEventListener('click', function() {
        registerModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === registerModal) {
            registerModal.style.display = 'none';
        }
    });

    // Resume Upload and Analysis Logic
    const analyzeButton = document.getElementById('analyzeButton');
    const resumeUpload = document.getElementById('resumeUpload');
    const uploadResumeButton = document.getElementById('uploadResumeButton');

    resumeUpload.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            analyzeButton.disabled = false;
        } else {
            analyzeButton.disabled = true;
        }
    });

    analyzeButton.addEventListener('click', function() {
        // Replace with actual analysis logic
        const analysisResults = {
            strengths: "Good formatting, relevant experience.",
            weaknesses: "Needs more specific skills, improve action verbs.",
            suggestions: "Tailor resume to each job, quantify achievements."
        };

        const queryString = `?strengths=${encodeURIComponent(analysisResults.strengths)}&weaknesses=${encodeURIComponent(analysisResults.weaknesses)}&suggestions=${encodeURIComponent(analysisResults.suggestions)}`;

        window.location.href = 'analysis_results.html' + queryString;
    });

    uploadResumeButton.addEventListener('click', function() {
        window.location.href = 'upload_resume.html';
    });

    // Resume Builder Link
    const resumeBuilderButton = document.getElementById('resumeBuilderButton');

    resumeBuilderButton.addEventListener('click', function() {
        window.location.href = 'resume_builder.html';
    });

    // About and Services Scroll Functionality
    const aboutLink = document.querySelector('nav a[href="#aboutSection"]');
    const servicesLink = document.querySelector('nav a[href="#servicesSection"]');
    const aboutSection = document.getElementById('aboutSection');
    const servicesSection = document.getElementById('servicesSection');

    if (aboutLink && aboutSection) {
        aboutLink.addEventListener('click', function(event) {
            event.preventDefault();
            aboutSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    }

    if (servicesLink && servicesSection) {
        servicesLink.addEventListener('click', function(event) {
            event.preventDefault();
            servicesSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    }
});