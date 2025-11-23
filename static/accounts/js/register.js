function agregarChip(divId) {
    const texto = prompt("Ingresa la habilidad:");
    if (texto && texto.trim() !== "") {
        const chip = document.createElement("span");
        chip.className = "chip";
        chip.textContent = texto;
        document.getElementById(divId).appendChild(chip);
    }
}
