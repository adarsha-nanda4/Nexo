document.addEventListener('DOMContentLoaded', () => {
    
    // --- Delete Confirmation Logic ---
    const deleteForms = document.querySelectorAll('.delete-form');

    deleteForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const productTitle = e.target.closest('tr').querySelector('.p-title')?.innerText || "this product";
            
            const confirmed = confirm(`Are you sure you want to delete "${productTitle}"?\nThis action cannot be undone.`);
            
            if (!confirmed) {
                e.preventDefault(); // Stop submission if user cancels
            }
        });
    });

    // --- Optional: Form Change Detection ---
    // This adds a visual cue if the user tries to leave without saving
    const profileForm = document.querySelector('.profile-form');
    let formChanged = false;

    if (profileForm) {
        profileForm.addEventListener('input', () => {
            formChanged = true;
        });

        profileForm.addEventListener('submit', () => {
            formChanged = false; // Reset on valid submit
        });

        window.addEventListener('beforeunload', (e) => {
            if (formChanged) {
                e.preventDefault();
                e.returnValue = ''; // Standard browser warning
            }
        });
    }
});