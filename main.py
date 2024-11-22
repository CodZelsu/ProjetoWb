from flask import Flask, render_template
import sqlite3
import re

app = Flask(__name__)

from app.default import *

def conectar_db():
    conectar = sqlite3.connect('cliente.db')
    return conectar

def conectar_db():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''

CREATE TABLE hotel_info (
    id_hotel BIGINT AUTO_INCREMENT,
    quartos INT,
    quartos_livres INT(10),
    nome VARCHAR(30),
    funcionario BIGINT,
    PRIMARY KEY (id_hotel)
);

CREATE TABLE funcionario (
    id_funcionario BIGINT AUTO_INCREMENT,
    nome VARCHAR(30),
    cpf VARCHAR(255),
    funcao VARCHAR(10),
    telefone BIGINT,
    email VARCHAR(255),
    senha VARCHAR(255),
    PRIMARY KEY (id_funcionario)
);

CREATE TABLE quartos (
    id_quartos BIGINT AUTO_INCREMENT,
    num_quartos INT(10),
    status_quarto BOOLEAN,
    cliente BIGINT,
    preco_dia DECIMAL,
    PRIMARY KEY (id_quartos)
);

ALTER table quartos 
	add info_quarto varchar(255),
    add foreign key (cliente) references cliente (id_cliente);

CREATE TABLE cliente (
	id_cliente bigint auto_increment,
    nome varchar(255),
    cpf varchar(255),
    num_telefone bigint,
    email varchar(255),
    dat_entrada date,
    dat_saida date,
    num_quarto int(10),
    senha varchar(255),
    primary key (id_cliente)
);

CREATE TABLE pagamentos (
	id_pagamento bigint auto_increment,
    id_cliente bigint,
    id_quartos bigint,
    valor decimal,
    data_pagamento date,
    metodo_pagamento varchar(50),
    primary key (id_pagamento),
    foreign key (id_cliente) references cliente (id_cliente),
    foreign key (id_quartos) references quartos (id_quartos)
    );

@app.route("/")
def index():
    return render_template('cadastro.html')
    
    )
    ''')