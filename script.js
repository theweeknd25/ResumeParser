document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const fileInput = form.querySelector('input[type="file"]');
    const resultsContainer = document.querySelector(".results");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        if (!fileInput.files[0]) {
            alert("Please select a file before submitting.");
            return;
        }

        const formData = new FormData();
        formData.append("resume", fileInput.files[0]);

        resultsContainer.innerHTML = "<p>Parsing resume, please wait...</p>";

        try {
            const response = await fetch("http://127.0.0.1:5000/parse_resume", {
                method: "POST",
                body: formData
            });

            if (!response.ok) throw new Error("Failed to parse resume");

            const data = await response.json();

            resultsContainer.innerHTML = `
                <h3>Parsed Resume Details</h3>
                <div class="field"><strong>Name:</strong> ${data.name || "Not Found"}</div>
                <div class="field"><strong>Emails:</strong> ${(data.emails || ["Not Found"]).join(", ")}</div>
                <div class="field"><strong>Phones:</strong> ${(data.phones || ["Not Found"]).join(", ")}</div>
                <div class="field"><strong>URLs:</strong> ${(data.urls || ["Not Found"]).join(", ")}</div>
                <div class="field"><strong>Locations:</strong> ${(data.locations || ["Not Found"]).join(", ")}</div>
                <div class="field"><strong>Skills:</strong> ${(data.skills || ["Not Found"]).join(", ")}</div>
                <div class="field"><strong>Qualifications:</strong> ${(data.qualifications || ["Not Found"]).join(", ")}</div>
                <div class="field"><strong>Years of Experience:</strong> ${data.years_of_experience || "Not Found"}</div>
                <hr>
                <details>
                    <summary style="cursor:pointer;">Click to view extracted full text preview</summary>
                    <pre style="white-space: pre-wrap; font-size: 0.9em; background: #f0f0f0; padding: 10px; border-radius: 6px;">${data.full_text || "Not Available"}</pre>
                </details>
            `;
        } catch (error) {
            console.error(error);
            resultsContainer.innerHTML = "<p style='color: red;'>Error parsing resume. Check console for details.</p>";
        }
    });
});
