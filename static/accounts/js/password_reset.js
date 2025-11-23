// Muestra error en un campo y crea el mensaje si no existe
function showError(fieldId, msg) {
    const input = document.getElementById(fieldId);
    if (!input) return;

    // Añadir clase de error al input
    input.classList.add('is-invalid');

    // Buscar contenedor de mensaje existente
    let err = input.parentElement.querySelector('.field-error');
    if (!err) {
        // creamos el nodo de error justo después del input
        err = document.createElement('div');
        err.className = 'field-error text-danger';
        err.style.fontSize = '0.875rem';
        err.style.marginTop = '6px';
        input.parentElement.appendChild(err);
    }
    err.textContent = msg;
}

// Limpia el error de un campo (quita mensaje y clase)
function clearError(fieldId) {
    const input = document.getElementById(fieldId);
    if (!input) return;

    input.classList.remove('is-invalid');

    const err = input.parentElement.querySelector('.field-error');
    if (err) err.remove();
}

// Muestra un mensaje de éxito (o info) en el contenedor #alertContainer
function showSuccess(msg) {
    const container = document.getElementById('alertContainer');
    if (!container) return;
    container.innerHTML = ''; // limpiar previos
    const div = document.createElement('div');
    div.className = 'alert alert-success';
    div.textContent = msg;
    container.appendChild(div);
}

// (Opcional) función para mostrar errores generales
function showGeneralError(msg) {
    const container = document.getElementById('alertContainer');
    if (!container) return;
    container.innerHTML = '';
    const div = document.createElement('div');
    div.className = 'alert alert-danger';
    div.textContent = msg;
    container.appendChild(div);
}
