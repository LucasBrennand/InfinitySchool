//Atividade 1
console.log("Atividade 1")

const numerosForEach = [-5, 2, 0, 1, 2, 3, -24, 14, -4]

numerosForEach.forEach(element => {
    if (element === 0){
        console.log(`${element} é o número 0`)
    }
    else if (element < 0){
        console.log(`${element} é um número negativo`)
    }
    else{
        console.log(`${element} é um número positivo`)
    }
});

//Atividade 2
console.log("Atividade 2")

const numerosMap = [2, 3, 6, 1, 4, 20]

numerosQuadrado = numerosMap.map(num => num ** 2)
console.log(numerosQuadrado)


//Atividade 3
console.log("Atividade 3")

const numerosFilter = [1, 3, 5, 7, 8, 9, 10, 13, 15]

numerosFiltrado = numerosFilter.filter(num => num % 2 == 0)
console.log(numerosFiltrado)


//Atividade 4
console.log("Atividade 4")

const numerosReduce = [1, 3, 5, 7, 8, 9, 10, 13, 15]

numerosReduzido = numerosReduce.reduce((acumulador, index) => {
    return acumulador + index
})
console.log(numerosReduzido)


//Atividade 5
console.log("Atividade 5")

const numerosSome = [1, 2, 3, 4, 5, 6, 8, -10, 12]

numerosExiste = numerosSome.some(num => num < 0)
console.log(numerosExiste)

//Atividade 6
console.log("Atividade 6")

const numeroFind = [2, 4, 5, 6, 8, 9, 10]

numeroEncontrado = numeroFind.find(num => num % 2 !== 0)

if (numeroEncontrado !== undefined){
    console.log(`Primeiro número ímpar encontrado: ${numeroEncontrado}`)
}
else{
    console.log("Nenhum número ímpar encontrado")
}

//Atividade 7
console.log("Atividade 7")

const numeroEvery = [2, 4, 6, 8, 10]

numerosPares = numeroEvery.every(num => num % 2 == 0)
console.log(numerosPares)
