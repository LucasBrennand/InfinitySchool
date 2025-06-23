//Atividade 2
console.log("Atividade 2")

function calcularDesconto(preco, desconto){
    preco = preco - ((preco * desconto) / 100)
    console.log(preco)
}

calcularDesconto(100,20)

//Atividade 3
console.log("Atividade 3")

let soma = 0
function calcularSoma(...numeros){
    for (i of numeros){
        soma+=i
    }
    console.log(`A soma de todos os números deu ${soma}`)
}

calcularSoma(1,3,5,6,2,9)

//Atividade 6
console.log("Atividade 6")
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
const filtrarPares = numeros.filter(num => num % 2 == 0)
console.log(filtrarPares)