-- Atividade 1
create database escola;
use escola;

create table alunos (
id_aluno int not null auto_increment primary key,
nome varchar(50) not null,
idade int not null
);

create table cursos(
id_curso int not null auto_increment primary key,
nome_curso varchar(50) not null,
carga_horaria double);

create table matriculas(
id_matricula int not null auto_increment primary key,
id_aluno int not null,
data_matricula varchar(50));

-- Atividade 2
truncate table matriculas;


-- Atividade 3
drop database escola;