//Atividade 5
console.log("Atividade 5")

const n = 5
while(i <= 5){
    print(i)
    i--
}

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
console.log(`Array de números pares: ${pares}`)
let paresQuadrado = pares.map(number => number ** 2)
console.log(`Array de números pares ao quadrado: ${paresQuadrado}`)

let somaPares = paresQuadrado.forEach(element => {
    soma+=element
});

console.log(`Soma de todos os numeros pares: ${soma}`)
