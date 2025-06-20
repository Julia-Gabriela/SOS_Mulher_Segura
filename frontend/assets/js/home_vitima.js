// Adicionamos um "escutador" que espera o HTML estar completamente pronto
document.addEventListener('DOMContentLoaded', function() {

    // 1. Pegar os elementos do HTML com os quais vamos interagir
    const sosButton = document.getElementById('sos-button-trigger');
    const modalConfirmacao = document.getElementById('modal-confirmacao');
    const btnConfirmarChamado = document.getElementById('btn-confirmar-chamado');
    const btnCancelarChamado = document.getElementById('btn-cancelar-chamado');
    const modalAcionada = document.getElementById('modal-acionada');
    const btnFecharAcionada = document.getElementById('btn-fechar-acionada');

    // 2. VERIFICA SE OS ELEMENTOS ESSENCIAIS FORAM ENCONTRADOS
    if (sosButton && modalConfirmacao && modalAcionada) {
        
        // Quando o botão principal SOS for clicado
        sosButton.addEventListener('click', (event) => {
            event.preventDefault(); 
            modalConfirmacao.classList.remove('escondido'); 
        });

        // Quando o botão "Cancelar" da primeira janela for clicado
        btnCancelarChamado.addEventListener('click', () => {
            modalConfirmacao.classList.add('escondido'); 
        });

        // Quando o botão "Confirmar" da primeira janela for clicado
        btnConfirmarChamado.addEventListener('click', () => {
            modalConfirmacao.classList.add('escondido'); 
            modalAcionada.classList.remove('escondido'); 

            // Futuramente, aqui podemos adicionar a lógica para enviar
            // o alerta para o servidor Django.
        });

        // Quando o botão "X" da segunda janela for clicado
        btnFecharAcionada.addEventListener('click', () => {
            modalAcionada.classList.add('escondido'); 
        });

        // Fechar clicando fora da caixa
        modalConfirmacao.addEventListener('click', (event) => {
            if (event.target === modalConfirmacao) {
                modalConfirmacao.classList.add('escondido');
            }
        });

        modalAcionada.addEventListener('click', (event) => {
            if (event.target === modalAcionada) {
                modalAcionada.classList.add('escondido');
            }
        });
    }
});