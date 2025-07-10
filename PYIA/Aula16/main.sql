-- Atividade 1
create table pedidos (
id_pedido int auto_increment primary key,
data_pedido varchar(50) not null,
id_cliente int not null,
foreign key (id_cliente) references clientes(id_cliente))

-- Atividade 2
create table produtos (
id_produto int auto_increment primary key,
nome_produto varchar(50),
preco double);

select * from produtos
where preco > 0