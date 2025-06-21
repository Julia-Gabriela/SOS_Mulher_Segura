document.addEventListener("DOMContentLoaded", function () {
    const cepInput = document.querySelector('input[name="cep"]');
    const bairroInput = document.querySelector('input[name="bairro"]');
    const complementoInput = document.querySelector('input[name="complemento"]');
    const cidadeInput = document.querySelector('input[name="cidade"]');
    const ufSelect = document.getElementById('uf');

    const ufs = [
        { sigla: 'AC', nome: 'Acre' },
        { sigla: 'AL', nome: 'Alagoas' },
        { sigla: 'AP', nome: 'Amapá' },
        { sigla: 'AM', nome: 'Amazonas' },
        { sigla: 'BA', nome: 'Bahia' },
        { sigla: 'CE', nome: 'Ceará' },
        { sigla: 'DF', nome: 'Distrito Federal' },
        { sigla: 'ES', nome: 'Espírito Santo' },
        { sigla: 'GO', nome: 'Goiás' },
        { sigla: 'MA', nome: 'Maranhão' },
        { sigla: 'MT', nome: 'Mato Grosso' },
        { sigla: 'MS', nome: 'Mato Grosso do Sul' },
        { sigla: 'MG', nome: 'Minas Gerais' },
        { sigla: 'PA', nome: 'Pará' },
        { sigla: 'PB', nome: 'Paraíba' },
        { sigla: 'PR', nome: 'Paraná' },
        { sigla: 'PE', nome: 'Pernambuco' },
        { sigla: 'PI', nome: 'Piauí' },
        { sigla: 'RJ', nome: 'Rio de Janeiro' },
        { sigla: 'RN', nome: 'Rio Grande do Norte' },
        { sigla: 'RS', nome: 'Rio Grande do Sul' },
        { sigla: 'RO', nome: 'Rondônia' },
        { sigla: 'RR', nome: 'Roraima' },
        { sigla: 'SC', nome: 'Santa Catarina' },
        { sigla: 'SP', nome: 'São Paulo' },
        { sigla: 'SE', nome: 'Sergipe' },
        { sigla: 'TO', nome: 'Tocantins' }
    ];

    ufs.forEach(uf => {
        const option = document.createElement('option');
        option.value = uf.sigla;
        option.textContent = uf.nome;
        ufSelect.appendChild(option);
    });

    cepInput.addEventListener("blur", function () {
        const cep = cepInput.value.replace(/\D/g, '');

        if (cep.length !== 8) {
            alert("CEP inválido. Digite 8 números.");
            return;
        }

        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Erro na requisição");
                }
                return response.json();
            })
            .then(data => {
                if ("erro" in data) {
                    alert("CEP não encontrado.");
                    return;
                }

                bairroInput.value = data.bairro || '';
                cidadeInput.value = data.localidade || '';
                ufSelect.value = data.uf || '';
                complementoInput.value = data.logradouro || ''
            })
            .catch(() => {
                alert("Erro ao buscar CEP. Tente novamente.");
            });
    });
});
