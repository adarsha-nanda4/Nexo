lucide.createIcons();

const togglePassword = document.getElementById("togglePassword");
const passwordInput = document.getElementById("password");
const eyeIcon = document.getElementById("eyeIcon");

togglePassword.addEventListener("click", () => {
  const isPassword = passwordInput.type === "password";
  passwordInput.type = isPassword ? "text" : "password";
  eyeIcon.setAttribute("data-lucide", isPassword ? "eye-off" : "eye");
  lucide.createIcons();
});

const emailInput = document.getElementById("email");
const emailValidIcon = document.getElementById("emailValidIcon");

emailInput.addEventListener("input", () => {
  emailValidIcon.classList.toggle("hidden", !emailInput.validity.valid);
});
