// login.js - Lógica de autenticación

// Credenciales válidas (en producción esto estaría en un backend)
const VALID_CREDENTIALS = {
    username: 'admin',
    password: 'admin123'
};

// Contador de intentos fallidos
let failedAttempts = 0;

// Elementos del DOM
const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const alertContainer = document.getElementById('alert-container');
const alertMessage = document.getElementById('alert-message');
const btnLogin = document.getElementById('btn-login');

// Event Listeners
loginForm.addEventListener('submit', handleLogin);

// Verificar si ya está autenticado
window.addEventListener('DOMContentLoaded', () => {
    const isAuthenticated = sessionStorage.getItem('isAuthenticated');
    if (isAuthenticated === 'true') {
        window.location.href = 'index.html';
    }
});

/**
 * Maneja el proceso de login
 * @param {Event} event - Evento del formulario
 */
function handleLogin(event) {
    event.preventDefault();

    // Obtener valores
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    // Limpiar alerta previa
    hideAlert();

    // Validar campos vacíos
    if (!username || !password) {
        showAlert('Por favor complete todos los campos', 'error');
        return;
    }

    // Validar credenciales
    if (username === VALID_CREDENTIALS.username && password === VALID_CREDENTIALS.password) {
        // Login exitoso
        handleSuccessfulLogin(username);
    } else {
        // Login fallido
        handleFailedLogin();
    }
}

/**
 * Maneja un login exitoso
 * @param {string} username - Nombre de usuario
 */
function handleSuccessfulLogin(username) {
    // Guardar sesión
    sessionStorage.setItem('isAuthenticated', 'true');
    sessionStorage.setItem('currentUser', username);
    sessionStorage.setItem('loginTime', new Date().toISOString());

    // Resetear intentos fallidos
    failedAttempts = 0;

    // Mostrar mensaje de éxito
    showAlert('Inicio de sesión exitoso. Redirigiendo...', 'success');

    // Redirigir después de un breve delay
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1000);
}

/**
 * Maneja un login fallido
 */
function handleFailedLogin() {
    failedAttempts++;

    let message = 'Usuario o contraseña incorrectos';

    // Mostrar advertencia después de 3 intentos
    if (failedAttempts >= 3) {
        message += '. Has excedido el número máximo de intentos recomendados.';
    }

    showAlert(message, 'error');

    // Limpiar campos de contraseña
    passwordInput.value = '';
    passwordInput.focus();
}

/**
 * Muestra una alerta
 * @param {string} message - Mensaje a mostrar
 * @param {string} type - Tipo de alerta ('success' o 'error')
 */
function showAlert(message, type = 'error') {
    alertMessage.textContent = message;
    alertContainer.className = `alert alert-${type} show`;
}

/**
 * Oculta la alerta
 */
function hideAlert() {
    alertContainer.classList.remove('show');
}

// Validación en tiempo real
usernameInput.addEventListener('input', () => {
    if (alertContainer.classList.contains('show')) {
        hideAlert();
    }
});

passwordInput.addEventListener('input', () => {
    if (alertContainer.classList.contains('show')) {
        hideAlert();
    }
});
