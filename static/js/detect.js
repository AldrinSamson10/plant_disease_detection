const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const fileStatus = document.getElementById("fileStatus");
const analyzeBtn = document.getElementById("analyzeBtn");

if (imageInput) {
    imageInput.addEventListener("change", function () {
        const file = this.files[0];

        if (!file) {
            fileStatus.textContent = "No image selected";
            previewImage.style.display = "none";
            analyzeBtn.disabled = true;
            return;
        }

        // ✅ Show file selected text
        fileStatus.textContent = `Image selected: ${file.name}`;

        // ✅ Enable analyze button
        analyzeBtn.disabled = false;

        // ✅ Show preview
        const reader = new FileReader();
        reader.onload = function () {
            previewImage.src = reader.result;
            previewImage.style.display = "block";
        };
        reader.readAsDataURL(file);
    });
}