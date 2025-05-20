CREATE TABLE clientes (
	id UUID NOT NULL, 
	nome VARCHAR(100), 
	email VARCHAR(100), 
	cpf VARCHAR(14), 
	data_criacao TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE produtos (
	id UUID NOT NULL, 
	nome VARCHAR(100) NOT NULL, 
	descricao VARCHAR(255), 
	preco NUMERIC(10, 2) NOT NULL, 
	imagem_url VARCHAR(255), 
	categoria categoriaproduto NOT NULL, 
	data_criacao TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE pedidos (
	id UUID NOT NULL, 
	produtos_ids UUID[] NOT NULL, 
	cliente_id UUID, 
	status VARCHAR NOT NULL, 
	data_criacao TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cliente_id) REFERENCES clientes (id)
);