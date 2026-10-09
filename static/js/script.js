document.addEventListener("DOMContentLoaded", function () {

    // Add small animation to cards
    const cards = document.querySelectorAll(
        ".service-card, .stat-card, .performance-card, .about-card"
    );

    cards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {

            card.style.transform = "translateY(-3px)";
            card.style.transition = "0.2s";

        });

        card.addEventListener("mouseleave", function () {

            card.style.transform = "translateY(0)";

        });

    });


    // Confirm before prediction
    const forms = document.querySelectorAll(".prediction-form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const button =
                form.querySelector(".predict-btn");

            if (button) {

                button.innerHTML =
                    "Analyzing patient data...";

                button.style.opacity = "0.8";

            }

        });

    });

});