// ================= ACTIVE MENU HIGHLIGHT =================
document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;

    const navLinks = document.querySelectorAll(".nav a, .top-nav a");

    navLinks.forEach(link => {
        const linkPath = link.getAttribute("href");

        // Highlight exact match
        if (linkPath === currentPath) {
            link.style.color = "#2e7d32";
            link.style.fontWeight = "bold";
        }

        // Special case: Dashboard/Home
        if (currentPath === "/" && linkPath === "/") {
            link.style.color = "#2e7d32";
            link.style.fontWeight = "bold";
        }
    });
});

// ================= SAFE SMOOTH SCROLL =================
document.addEventListener("DOMContentLoaded", function () {
    const anchors = document.querySelectorAll('a[href^="#"]');

    anchors.forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            const targetId = this.getAttribute("href");

            // Prevent error if element doesn't exist
            if (targetId && targetId !== "#" && document.querySelector(targetId)) {
                e.preventDefault();
                document.querySelector(targetId)
                    .scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});