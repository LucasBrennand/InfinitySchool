// //Atividade 1
// console.log("Atividade 1")
// i = 0

// while(i <= 10){
//     console.log(i)
//     i++
// }



// //Atividade 2
// console.log("Atividade 2")
// let userInput
// do{
//     userInput = parseInt(prompt("Digite um número"))
//     console.log(`Input: ${userInput}`)
// } while(userInput > 0)


// //Atividade 3
// console.log("Atividade 3")
// random = Math.floor(Math.random() * 11)
// console.log(random)

// while(true){
//     guess = parseInt(prompt("Advinhe um numero de 0 a 10"))
//     if (guess === random){
//         console.log(`Voce acertou! O número era ${random}`)
//         break
//     }
// }

//Atividade 4
console.log("Atividade 4")
userInput = parseInt(prompt("Digite um número"))
let i = 0
let soma = 0

while (i <= userInput) {
    soma += i
    i++
    console.log(soma)
}