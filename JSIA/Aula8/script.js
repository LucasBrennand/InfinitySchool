//Atividade 1
console.log("Atividade 1")

const carro = {
    marca: "Toyota",
    modelo: "Corolla",
    ano: 1988
}

console.log(carro)

//Atividade 2
console.log("Atividade 2")

const pessoa = {
    nome: "Lucas",
    idade: 22,
    profissao: "Desenvolvedor"
}

pessoa.profissao = "Monitor"
pessoa.cidade = "Recife"
console.log(pessoa)

//Atividade 3
console.log("Atividade 3")

const livro = {
    titulo: "Percy Jackson",
    autor: "Rick Riordan",
    ano: 2008,
    editora: "Disney"
}

let {titulo, autor} = livro
console.log(titulo)
console.log(autor)

//Atividade 4
console.log("Atividade 4")

const livros = [
  { titulo: "Dom Casmurro", autor: "Machado de Assis" },
  { titulo: "O Senhor dos Anéis", autor: "J.R.R. Tolkien" },
  { titulo: "1984", autor: "George Orwell" },
  { titulo: "A Revolução dos Bichos", autor: "George Orwell" },
  { titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry" },
  { titulo: "Cem Anos de Solidão", autor: "Gabriel García Márquez" },
  { titulo: "Harry Potter e a Pedra Filosofal", autor: "J.K. Rowling" },
  { titulo: "O Código Da Vinci", autor: "Dan Brown" },
  { titulo: "Capitães da Areia", autor: "Jorge Amado" },
  { titulo: "Grande Sertão: Veredas", autor: "João Guimarães Rosa" }
];

for (i of livros){
    console.log(i.titulo)
}
const novoLivro = {
    titulo: "Percy Jackson",
    autor: "Rick Riordan",
}

livros.push(novoLivro)
console.log(livros)

//Atividade 5
console.log("Atividade 5")

const carro1 = {
    marca: "Jeep",
    modelo: "Compass",
    ano: 2017
}

const carro2 = {
    marca: "Hyundai",
    modelo: "Tucson",
    ano: 2008
}

const carros = {...carro1, ...carro2}
console.log(carros)

//Atividade 6
console.log("Atividade 6")

//Atividade 7
console.log("Atividade 7")

//Atividade 8
console.log("Atividade 1")