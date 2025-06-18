// //Atividade 5
// console.log("Atividade 5")

// const n = 5
// let i
// while(i < 5){

// }

//Atividade 7
console.log("Atividade 7")
let numeros = [];
let i = 0;
let soma = 0
while (i < 20) {
    let numeroAleatorio = Math.floor(Math.random() * 100) + 1;
    numeros.push(numeroAleatorio);
    i++;
}
console.log(`Array de números aleatórios: ${numeros}`);

let pares = numeros.filter(number => number % 2 == 0)
let paresQuadrado = pares.map(number => number ** 2)
console.log(`Array de números pares ao quadrado: ${paresQuadrado}`)
let somaPares = paresQuadrado.map(number => {
    soma+=number
})
console.log(`Array de soma dos numeros pares: ${somaPares}`)