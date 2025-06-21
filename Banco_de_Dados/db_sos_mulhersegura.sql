-- Criação do banco
CREATE DATABASE IF NOT EXISTS db_sos_mulhersegura CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE db_sos_mulhersegura;

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(128) NOT NULL,
    telefone CHAR(11) NOT NULL,
    data_nascimento DATE,
    data_cadastro DATE,
    cep VARCHAR(9) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    complemento VARCHAR(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE usuarios ADD COLUMN cidade VARCHAR(100);
ALTER TABLE usuarios ADD COLUMN uf VARCHAR(2);

-- Tabela de medidas protetivas
CREATE TABLE IF NOT EXISTS medidas_protetivas (
    id_medida INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(14),
    descricao TEXT NOT NULL,
    data_inicio DATE,
    data_fim DATE,
    distancia_minima_metros INT,
    FOREIGN KEY (cpf) REFERENCES usuarios(cpf)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de denúncias
CREATE TABLE IF NOT EXISTS denuncias (
    id_denuncia INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(14) NOT NULL,
    descricao TEXT NOT NULL,
    data_hora DATETIME NOT NULL,
    localizacao VARCHAR(255) NOT NULL,
    provas_anexadas BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (cpf) REFERENCES usuarios(cpf)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de provas
CREATE TABLE IF NOT EXISTS provas (
    id_prova INT PRIMARY KEY AUTO_INCREMENT,
    id_denuncia INT,
    tipo_prova VARCHAR(50) CHECK (tipo_prova IN ('foto', 'áudio', 'documento', 'outro')),
    caminho_arquivo VARCHAR(255),
    FOREIGN KEY (id_denuncia) REFERENCES denuncias(id_denuncia)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de contatos de confiança
CREATE TABLE IF NOT EXISTS contatos_confianca (
    id_contato INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(14),
    nome_contato VARCHAR(100),
    telefone VARCHAR(15),
    email VARCHAR(100),
    FOREIGN KEY (cpf) REFERENCES usuarios(cpf)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de histórico de denúncias
CREATE TABLE IF NOT EXISTS historico_denuncias (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(14),
    id_denuncia INT,
    status VARCHAR(50),
    data_status DATETIME,
    FOREIGN KEY (cpf) REFERENCES usuarios(cpf),
    FOREIGN KEY (id_denuncia) REFERENCES denuncias(id_denuncia)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de configurações
CREATE TABLE IF NOT EXISTS configuracoes (
    id_config INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(14),
    notificacoes_ativas BOOLEAN,
    receber_alertas_email BOOLEAN,
    receber_alertas_sms BOOLEAN,
    FOREIGN KEY (cpf) REFERENCES usuarios(cpf)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
SELECT * FROM usuarios;
SELECT * FROM denuncias;

ALTER TABLE denuncias
ADD COLUMN arquivo VARCHAR(255);
ALTER TABLE denuncias ADD COLUMN status VARCHAR(20) DEFAULT 'pendente';