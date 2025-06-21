
    // Pegando o CPF do localStorage
    const cpf = document.getElementById('cpf').value;
    console.log(cpf);

    // Verifica se o CPF existe e preenche o campo oculto
    if (cpf) {
        document.getElementById('cpf').value = cpf;
    } else {
        alert('CPF não encontrado. Por favor, faça login novamente.');  
    }

