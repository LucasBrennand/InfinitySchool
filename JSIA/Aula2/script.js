// //Atividade 1
console.log("Atividade 1")
i = 0

while(i <= 10){
    console.log(i)
    i++
}



// //Atividade 2
console.log("Atividade 2")
let userInput
do{
    userInput = parseInt(prompt("Digite um número"))
    console.log(`Input: ${userInput}`)
} while(userInput > 0)


// //Atividade 3
console.log("Atividade 3")
random = Math.floor(Math.random() * 11)
console.log(random)

while(true){
    guess = parseInt(prompt("Advinhe um numero de 0 a 10"))
    if (guess === random){
        console.log(`Voce acertou! O número era ${random}`)
        break
    }
}

// //Atividade 4
console.log("Atividade 4")
userInput = parseInt(prompt("Digite um número"))
let i = 1
let soma = 0

while (i <= userInput) {
    soma += i
    i++
    console.log(soma)
}

// //Atividade 5
console.log("Atividade 5")

const tamanho = 20
for (let i = 0; i <= tamanho; i++) {
    if(i == 15){
        console.log("15 encontrado, saindo..")
        break
    }
    if (i % 3 == 0){
        console.log("Multiplo de 3, pulando")
        continue
    }
    
    console.log(i)
}


//Atividade 6
console.log("Atividade 6")

strInput = prompt("Digite uma palavra")

for(i of strInput){
    console.log(i)
}