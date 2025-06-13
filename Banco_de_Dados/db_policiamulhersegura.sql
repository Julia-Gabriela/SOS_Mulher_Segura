-- Recriação do banco do zero (opcional)
-- DROP DATABASE IF EXISTS DB_PoliciaMulherSegura;
CREATE DATABASE DB_PoliciaMulherSegura;
USE DB_PoliciaMulherSegura;

-- Tabela de vítimas (CPF agora é BIGINT)
CREATE TABLE IF NOT EXISTS Vitimas (
    CPF BIGINT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone CHAR(11),
    email VARCHAR(100),
    dataNasc DATE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Tabela de medidas protetivas oficiais (CPF como BIGINT e chave estrangeira correta)
CREATE TABLE IF NOT EXISTS Medidas_oficiais (
    id_medida INT PRIMARY KEY AUTO_INCREMENT,
    CPF BIGINT,
    descricao TEXT NOT NULL,
    data_inicio DATE,
    data_fim DATE,
    distancia_minima_metros INT,
    status VARCHAR(50) DEFAULT 'Ativa',
    FOREIGN KEY (CPF) REFERENCES Vitimas(CPF)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Tabela de denúncias recebidas via integração (CPF como BIGINT e FK correta)
CREATE TABLE IF NOT EXISTS Denuncias_recebidas (
    id_denuncia INT PRIMARY KEY,
    CPF BIGINT,
    tipo_denuncia VARCHAR(50),
    descricao TEXT,
    data_hora DATETIME,
    localizacao VARCHAR(255),
    provas_anexadas BOOLEAN,
    status_avaliacao VARCHAR(50) DEFAULT 'Pendente',
    FOREIGN KEY (CPF) REFERENCES Vitimas(CPF),
    CHECK (tipo_denuncia IN ('alerta', 'detalhada'))
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Tabela de ocorrência policial oficial
CREATE TABLE IF NOT EXISTS Ocorrencias (
    id_ocorrencia INT PRIMARY KEY AUTO_INCREMENT,
    id_denuncia INT,
    responsavel VARCHAR(100),
    descricao_ocorrencia TEXT,
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    encaminhamento VARCHAR(255),
    FOREIGN KEY (id_denuncia) REFERENCES Denuncias_recebidas(id_denuncia)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Tabela de policiais responsáveis
CREATE TABLE IF NOT EXISTS Policiais (
    id_policial INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    matricula VARCHAR(20) UNIQUE,
    email VARCHAR(100),
    setor VARCHAR(100)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Inserção de vítimas
INSERT INTO Vitimas (CPF, nome, telefone, email, dataNasc) VALUES
(12345678901, 'Ana Paula da Silva', '61987654321', 'ana.silva@email.com', '1990-05-12'),
(98765432100, 'Mariana Costa', '61991234567', 'mariana.costa@email.com', '1985-09-23');

-- Inserção de medidas protetivas
INSERT INTO Medidas_oficiais (CPF, descricao, data_inicio, data_fim, distancia_minima_metros, status) VALUES
(12345678901, 'Proibição de aproximação a menos de 300 metros.', '2024-12-01', '2025-12-01', 300, 'Ativa'),
(98765432100, 'Restrição total de contato e aproximação física.', '2025-01-15', '2025-07-15', 0, 'Ativa');

-- Inserção de denúncias recebidas
INSERT INTO Denuncias_recebidas (id_denuncia, CPF, tipo_denuncia, descricao, data_hora, localizacao, provas_anexadas, status_avaliacao) VALUES
(1, 12345678901, 'alerta', 'Alerta de emergência disparado via aplicativo.', '2025-05-05 08:32:00', 'QS 5 Conjunto 2, Samambaia Sul, DF', TRUE, 'Pendente'),
(2, 98765432100, 'detalhada', 'Agressões verbais e ameaça no domicílio.', '2025-05-04 22:15:00', 'Quadra 104, Recanto das Emas, DF', TRUE, 'Avaliando');

-- Inserção de policiais
INSERT INTO Policiais (nome, matricula, email, setor) VALUES
('Sgt. João Batista', 'PCDF1234', 'joao.batista@pcdf.df.gov.br', 'Delegacia Especial de Atendimento à Mulher (DEAM)'),
('Insp. Carla Menezes', 'PCDF5678', 'carla.menezes@pcdf.df.gov.br', 'Núcleo de Proteção à Mulher');

-- Inserção de ocorrências
INSERT INTO Ocorrencias (id_denuncia, responsavel, descricao_ocorrencia, encaminhamento) VALUES
(1, 'Sgt. João Batista', 'Patrulha Maria da Penha foi acionada. Vítima acolhida e levada à DEAM.', 'Encaminhada para DEAM I - Asa Sul'),
(2, 'Insp. Carla Menezes', 'Inquérito aberto. Medida protetiva sugerida. Acompanhamento contínuo.', 'Encaminhada para Defensoria Pública do DF');
