
// Função de login
async function login(event) {
    event.preventDefault();
    const cpf = document.getElementById('cpf').value;
    const senha = document.getElementById('senha').value;

    const response = await fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cpf, senha })
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem('token', data.access);
        alert('Login bem-sucedido!');
        window.location.href = 'home_vitimas.html';
    } else {
        alert('Erro no login: ' + data.error);
    }
}

// Função de cadastro
async function cadastrar(event) {
    event.preventDefault();
    const cpf = document.getElementById('cpf').value;
    const senha = document.getElementById('senha').value;
    const nome = document.getElementById('nome').value;

    const response = await fetch('http://127.0.0.1:8000/api/cadastro/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cpf, senha, nome })
    });

    const data = await response.json();

    if (response.ok) {
        alert('Cadastro realizado com sucesso!');
        window.location.href = 'index.html';
    } else {
        alert('Erro no cadastro: ' + data.error);
    }
}
