function abrirPopup() {
    document.getElementById('popup-localizacao').style.display = 'flex';
}

function fecharPopup() {
    document.getElementById('popup-localizacao').style.display = 'none';
}

function confirmarAcao() {
    alert('Localização ativada!');
    fecharPopup();
}
