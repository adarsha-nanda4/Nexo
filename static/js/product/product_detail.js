document.addEventListener('DOMContentLoaded', () => {
    
    // --- Image Interaction ---
    const mainImage = document.getElementById('main-image');

    if (mainImage) {
        // Simple loaded class to fade in image
        mainImage.onload = function() {
            this.style.opacity = '1';
        };
        // Force opacity if cached
        if (mainImage.complete) mainImage.style.opacity = '1';

        // Mouse Move Zoom Effect (Desktop)
        const container = mainImage.parentElement;
        
        container.addEventListener('mousemove', (e) => {
            // Only apply zoom on non-touch devices/large screens
            if (window.innerWidth > 768) {
                const { left, top, width, height } = container.getBoundingClientRect();
                const x = (e.clientX - left) / width * 100;
                const y = (e.clientY - top) / height * 100;
                
                mainImage.style.transformOrigin = `${x}% ${y}%`;
                mainImage.style.transform = 'scale(1.5)'; // Zoom level
            }
        });

        container.addEventListener('mouseleave', () => {
            mainImage.style.transformOrigin = 'center center';
            mainImage.style.transform = 'scale(1)';
        });
    }

    // --- Action Button Tracking (Optional) ---
    const callBtn = document.querySelector('.btn-call');
    const whatsAppBtn = document.querySelector('.btn-whatsapp');

    if (callBtn) {
        callBtn.addEventListener('click', () => {
            console.log('User clicked Call button');
            // Optional: You could track analytics here
        });
    }

    if (whatsAppBtn) {
        whatsAppBtn.addEventListener('click', () => {
            console.log('User clicked WhatsApp button');
        });
    }
});