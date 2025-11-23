// Funciones generales compartidas

// Validación de correos institucionales de INACAP
function validateInacapEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@(inacap\.cl|inacapmail\.cl)$/;
    return emailRegex.test(email);
}

// Validación de contraseña
function validatePassword(password) {
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
    return passwordRegex.test(password);
}

// Mostrar error en campo
function showError(fieldId, message) {
    const field = document.getElementById(fieldId);
    const errorElement = document.getElementById(fieldId + 'Error');
    
    if (field && errorElement) {
        field.classList.add('invalid');
        field.classList.remove('valid');
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }
}

// Limpiar error
function clearError(fieldId) {
    const field = document.getElementById(fieldId);
    const errorElement = document.getElementById(fieldId + 'Error');
    
    if (field && errorElement) {
        field.classList.remove('invalid');
        field.classList.add('valid');
        errorElement.style.display = 'none';
    }
}

// Mostrar mensaje de éxito
function showSuccess(message) {
    // Crear elemento de alerta
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-success';
    alertDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: #d4edda;
        color: #155724;
        padding: 15px 20px;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    `;
    alertDiv.textContent = message;
    
    document.body.appendChild(alertDiv);
    
    // Remover después de 5 segundos
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Configurar validación en tiempo real
function setupRealTimeValidation() {
    const inputs = document.querySelectorAll('.input-field');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            const fieldId = this.id;
            clearError(fieldId);
        });
    });
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    setupRealTimeValidation();
});