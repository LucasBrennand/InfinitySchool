//Atividade 1
console.log("Atividade 1");
let divisao = (a, b) => {
  try {
    if (a === 0) {
      throw new Error("Divisão por 0");
    }
  } catch (error) {
    console.log(`Error: ${error.message}`);
  } finally {
    console.log("Final");
  }
  return a / b;
};
divisao(0, 6);

//Atividade 2
console.log("Atividade 2");
let dados = {
  nome: "Lu",
  idade: 17,
};
const erros = []
let validarDados = (objeto) => {
  try {
    if (objeto.nome.length < 3) {
      erros.push("Nome menor que 3 letras");
    }
    if (objeto.idade < 18) {
      erros.push("Menor de idade");
    }
    throw new Error(erros.join("; "))
  } catch (error) {
    console.log("Erros: ",error)
  }
}

validarDados(dados)

//Atividade3
console.log("Atividade 3");
const userIdade = -1

try {
    if (typeof(userIdade) === 17){
        throw new Error("Not a number")
    }
    else if (userIdade < 0){
        throw new Error("Number below 0")
    }
} catch (error) {
    console.log("Error: ",error)
}

//Atividade4
console.log("Atividade 4");

let division = (a, b) => {
    try {
        if (a === 0){
            throw new Error("Divisor é 0")
        }
        
    } catch (error) {
        console.log(`Error: ${error}`)
    }
}

division(0, 20)