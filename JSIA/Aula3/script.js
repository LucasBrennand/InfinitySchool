//Atividade 1
console.log("Atividade 1")

const array = ["Vermelho", "Verde", "Azul", "Amarelo"]
console.log(array[2])

//Atividade 2
console.log("Atividade 2")
const animais = ["Cachorro", "Gatio", "Papagaio"]
animais.push("Tartaruga")
animais.shift()
animais.unshift("Coelho")
animais.splice(1, 1, "Hamster")
console.log(`Tamanho do array animais: ${animais.length}`)
console.log(animais[1])
console.log(animais)


//Atividade 3
console.log("Atividade 3")
const cores = ["Vermelho", "Verde", "Azul"]
cores.push("Amarelo", "Roxo")
cores.pop()
cores.splice(1, 1, "Laranja", "Marrom")
const novasCores = cores.slice(0, 2)
console.log(`Novas cores: ${novasCores}`)
const coresString =  cores.join(", ")
console.log(`Join: ${coresString}`)
cores.reverse()
console.log(cores)

//Atividade 4
console.log("Atividade 4")
const numeros = [1, 2, 3, 4, 5, 6, 7]
for (let i = 0; i < numeros.length; i++) {
    if(numeros[i] % 2 == 0){
        console.log(`${numeros[i]} é par`)
    }
    else{
        console.log(`${numeros[i]} é ímpar`)
    }
    
}

//Atividade 5
console.log("Atividade 5")
const nomes = ["Lucas", "Mia", "Adila", "Juan"]

for (const i of nomes) {
    console.log(i)
}