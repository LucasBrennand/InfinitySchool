// // Atividade 1
// console.log("Atividade 1");

// const pessoa = {
//   name: "Lucas",
//   idade: 22,
//   cidade: "Recife",
// };

// const pessoaString = JSON.stringify(pessoa);
// console.log(pessoaString);

// // Atividade 2
// console.log("Atividade 2");

// const produtos = [
//   {
//     nome: "Banana",
//     preco: 2.5,
//   },
//   {
//     nome: "Maça",
//     preco: 1.75,
//   },
// ];

// const produtoString = JSON.stringify(produtos);
// console.log(produtoString);

// Atividade 3
console.log("Atividade 3");

const buscarUsuarios = async () => {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users", {
      method: "GET",
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    data.forEach((element) => {
      console.log(element.name);
    });
  } catch (error) {
    console.error("Error:", error);
  }
};
buscarUsuarios();

// Atividade 4
console.log("Atividade 4");

const newItem = {
  userId: 3,
  title: "lorem ipsem",
  body: "dolores etnium",
};

const criarPost = async () => {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newItem),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    console.log(`Resposta da API: `, data)

  } catch (error) {
    console.error("Error:", error);
  }
};

criarPost()
