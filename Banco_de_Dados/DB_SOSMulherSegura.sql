-- Criação do banco
CREATE DATABASE IF NOT EXISTS DB_SOS_MulherSegura;
USE DB_SOS_MulherSegura;

-- DROP DATABASE DB_SOS_MulherSegura;

-- Tabela de usuários (vítimas e outros)
CREATE TABLE IF NOT EXISTS Usuarios (
    CPF INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    telefone CHAR(11) NOT NULL,
    dataNasc DATE,
    data_cadastro DATE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Tabela de medidas protetivas vinculadas à vítima
CREATE TABLE IF NOT EXISTS Medidas_protetivas (
    id_medida INT PRIMARY KEY AUTO_INCREMENT,
    CPF INT,
    descricao TEXT NOT NULL,
    data_inicio DATE,
    data_fim DATE,
    distancia_minima_metros INT,
    FOREIGN KEY (CPF) REFERENCES Usuarios(CPF)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Tabela de denúncias
CREATE TABLE IF NOT EXISTS Denuncias (
    id_denuncia INT PRIMARY KEY AUTO_INCREMENT,
    CPF INT,
    tipo_denuncia VARCHAR(50),
    descricao TEXT,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    localizacao VARCHAR(255),
    provas_anexadas BOOLEAN,
    FOREIGN KEY (CPF) REFERENCES Usuarios(CPF),
    CHECK (tipo_denuncia IN ('alerta', 'detalhada'))
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Tabela de provas anexadas às denúncias
CREATE TABLE IF NOT EXISTS Provas (
    id_prova INT PRIMARY KEY AUTO_INCREMENT,
    id_denuncia INT,
    tipo_prova VARCHAR(50),
    caminho_arquivo VARCHAR(255),
    FOREIGN KEY (id_denuncia) REFERENCES Denuncias(id_denuncia),
    CHECK (tipo_prova IN ('foto', 'áudio', 'documento', 'outro'))
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Contatos de confiança vinculados à vítima
CREATE TABLE IF NOT EXISTS Contatos_confianca (
    id_contato INT PRIMARY KEY AUTO_INCREMENT,
    CPF INT,
    nome_contato VARCHAR(100),
    telefone VARCHAR(15),
    email VARCHAR(100),
    FOREIGN KEY (CPF) REFERENCES Usuarios(CPF)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Histórico de denúncias
CREATE TABLE IF NOT EXISTS Historico_denuncias (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    CPF INT,
    id_denuncia INT,
    status VARCHAR(50),
    data_status DATETIME,
    FOREIGN KEY (CPF) REFERENCES Usuarios(CPF),
    FOREIGN KEY (id_denuncia) REFERENCES Denuncias(id_denuncia)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Configurações de notificações
CREATE TABLE IF NOT EXISTS Configuracoes (
    id_config INT PRIMARY KEY AUTO_INCREMENT,
    CPF INT,
    notificacoes_ativas BOOLEAN,
    receber_alertas_email BOOLEAN,
    receber_alertas_sms BOOLEAN,
    FOREIGN KEY (CPF) REFERENCES Usuarios(CPF)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
