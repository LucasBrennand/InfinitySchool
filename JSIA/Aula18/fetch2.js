//Atividade 1
console.log("")
console.log("Atividade 1")

const produtos = [
{ nome: "Camisa",preco: 50 },
{ nome: "Calça", preco: 80 },
{ nome: "Sapato", preco: 120 }
];

const produtosComDesconto = produtos.map(produto => {
  return {
    nome: produto.nome,
    preco: produto.preco * 0.9
  };
});

console.log("Array original:");
console.log(produtos);
console.log("Array com desconto de 10%:");
console.log(produtosComDesconto);

//Atividade 2
console.log("")
console.log("Atividade 2")

//Atividade 3
console.log("")
console.log("Atividade 3")
const url = "https://api.example.com/dados";

fetch(url)
  .then(response => {
    if (response.ok) {
      return response.json().then(data => {
        console.log("Dados recebidos:", data);
      });
    } else if (response.status === 404) {
      console.log("Recurso não encontrado");
    } else {
      console.log("Erro ao carregar os dados");
    }
  })
  .catch(error => {
    console.log("Erro na requisição:", error);
  });

//Atividade 4
console.log("")
console.log("Atividade 4")




