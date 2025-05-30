create table cliente(
	cliente_id INT generated always as identity,
	nome VARCHAR(255) null,
	email VARCHAR(255) null,
	telefone VARCHAR(11) null,
	cpf VARCHAR(11) null,
	primary KEY(cliente_id)
);

create table status_pedido(
	id INT generated always as identity,
	descricao VARCHAR(50) not null,
	primary key(id)
);

create table pedido(
	pedido_id INT generated always as identity,
	cliente_id INT,
	status INT not null,
	data_criacao time not null,
	data_alteracao time null,
	data_finalizacao time null,
	primary key(pedido_id),
	constraint fk_cliente foreign key(cliente_id) references cliente(cliente_id),
	constraint fk_status_pedido foreign key(status) references status_pedido(id)
);

create table categoria_produto(
	id INT generated always as identity,
	nome VARCHAR(50) not null,
	primary key(id)
);

create table produto(
	produto_id INT generated always as identity,
	nome VARCHAR(255) not null,
	descricao VARCHAR(255) not null,
	preco DECIMAL not null,
	categoria INT,
	imagem VARCHAR(255) NULL,
	primary key(produto_id),
	constraint fk_categoria_produto FOREIGN key(categoria) references categoria_produto(id)
);

create table pedido_produtos(
	id INT generated always as identity,
	pedido_id INT NOT NULL,
	produto_id INT NOT NULL,
	primary key(id),
	constraint fk_pedido_id foreign key(pedido_id) references pedido(pedido_id),
	constraint fk_produto_id foreign key(produto_id) references produto(produto_id)
);

create table pagamento(
	pedido INT not null,
	codigo_pagamento VARCHAR(255) not null,
	status VARCHAR(100),
	primary KEY(pedido, codigo_pagamento),
	constraint fk_pedido foreign key(pedido) references pedido(pedido_id)
);

/** insert categoria_produto */
insert into categoria_produto(nome) values ('Lanche');
insert into categoria_produto(nome) values ('Acompanhamento');
insert into categoria_produto(nome) values ('Bebida');
insert into categoria_produto(nome) values ('Sobremesa');

/** insert pedido_status */
insert into status_pedido(descricao) values ('Recebido');
insert into status_pedido(descricao) values ('Em prepação');
insert into status_pedido(descricao) values ('Pronto');
insert into status_pedido(descricao) values ('Finalizado');