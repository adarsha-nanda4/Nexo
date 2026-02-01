// document.addEventListener('DOMContentLoaded', () => {
//     // Selectors
//     const loginForm = document.getElementById('login-form');
//     const usernameInput = document.getElementById('username');
//     const passwordInput = document.getElementById('password');
//     const togglePasswordBtn = document.getElementById('toggle-password');
//     const errorMessage = document.getElementById('error-message');
//     const becomeSellerBtn = document.getElementById('become-seller-btn');

//     // 1. Password Toggle Logic
//     togglePasswordBtn.addEventListener('click', () => {
//         const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
//         passwordInput.setAttribute('type', type);
//         togglePasswordBtn.textContent = type === 'password' ? 'Show' : 'Hide';
//         togglePasswordBtn.setAttribute('aria-label', type === 'password' ? 'Show password' : 'Hide password');
//     });

//     // 2. Clear Error on Input
//     const clearError = (e) => {
//         e.target.classList.remove('error');
//         errorMessage.textContent = '';
//     };
//     usernameInput.addEventListener('input', clearError);
//     passwordInput.addEventListener('input', clearError);

//     // 3. Form Validation
//     loginForm.addEventListener('submit', (e) => {
//         e.preventDefault();
//         const username = usernameInput.value.trim();
//         const password = passwordInput.value.trim();
//         let isValid = true;
        
//         usernameInput.classList.remove('error');
//         passwordInput.classList.remove('error');

//         if (!username) {
//             usernameInput.classList.add('error');
//             errorMessage.textContent = 'Username is required.';
//             isValid = false;
//         } else if (!password) {
//             passwordInput.classList.add('error');
//             errorMessage.textContent = 'Password is required.';
//             isValid = false;
//         }

//         if (isValid) {
//             errorMessage.textContent = '';
//             console.log('Login attempt:', { username });
            
//             const btn = loginForm.querySelector('.btn-primary');
//             const originalText = btn.textContent;
//             btn.textContent = 'Logging in...';
//             btn.style.opacity = '0.7';
            
//             setTimeout(() => {
//                 // Here you would typically submit to backend
//                 // window.location.href = "/dashboard"; 
//                 alert('Form submitted (check console)');
//                 btn.textContent = originalText;
//                 btn.style.opacity = '1';
//                 loginForm.reset();
//             }, 800);
//         }
//     });

//     // 4. Become Seller Button
//     becomeSellerBtn.addEventListener('click', () => {
//         console.log('Redirect to seller registration');
//     });
// });