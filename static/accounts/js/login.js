// Validar formulario de login
function validateLoginForm(email, password) {
    let isValid = true;

    // Validar email
    if (!email) {
        showError('email', 'El correo electrónico es requerido');
        isValid = false;
    } else if (!validateInacapEmail(email)) {
        showError('email', 'Solo se permiten correos @inacap.cl o @inacapmail.cl');
        isValid = false;
    } else {
        clearError('email');
    }

    // Validar contraseña
    if (!password) {
        showError('password', 'La contraseña es requerida');
        isValid = false;
    } else {
        clearError('password');
    }

    return isValid;
}

// Manejar envío del formulario de login
function handleLoginSubmit(e) {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    if (validateLoginForm(email, password)) {
        // Simular envío del formulario
        const button = e.target.querySelector('button[type="submit"]');
        const originalText = button.textContent;
        button.textContent = 'Iniciando Sesión...';
        button.classList.add('btn-loading');
        button.disabled = true;
        
        // Simular petición al servidor
        setTimeout(() => {
            showSuccess('¡Inicio de sesión exitoso!');
            
            // Restaurar botón
            button.textContent = originalText;
            button.classList.remove('btn-loading');
            button.disabled = false;
            
            // Redirigir (simulado)
            setTimeout(() => {
                window.location.href = '/dashboard/';
            }, 1000);
        }, 2000);
    }
}

// Inicializar login
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLoginSubmit);
    }
});