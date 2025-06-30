//Atividade 1
console.log("Atividade 1")

const nomeInput = document.querySelector("#nomeInput")
const enviar = document.querySelector("#enviar")
const div1 = document.querySelector(".atividade1")
const lista = document.querySelector("#lista")
const remove = document.querySelector("#remover")
const clear = document.querySelector("#clear")
const temaSelect = document.querySelector("#temaSelect")
const formBtn = document.querySelector("#formBtn")

let local = JSON.parse(localStorage.getItem("Nome")) || []
for(let i of local){
const itemAntigo = document.createElement("li")
lista.appendChild(itemAntigo)
itemAntigo.innerHTML = i
console.log(i)
}

let preferenciasLocal = JSON.parse(localStorage.getItem("Preferencias")) || []
console.log(preferenciasLocal)

let preferencias = {
    tema: "",
    fonte: ""
}

enviar.addEventListener("click", (event) => {
    const item = document.createElement("li")
    const nomeInputValue = nomeInput.value
    lista.appendChild(item)
    item.innerHTML = nomeInputValue
    local.push(nomeInputValue)
    console.log(local)
    localStorage.setItem("Nome", JSON.stringify(local))
})

remove.addEventListener("click", (event) => {
    const ultimoItem = lista.lastChild
    lista.removeChild(ultimoItem)
    local.pop()
    localStorage.setItem("Nome", JSON.stringify(local))
    console.log(local)
})

clear.addEventListener("click", (event) => {
    lista.remove(lista)
    local = []
    localStorage.setItem("Nome", JSON.stringify(local))
    console.log(local)
})

//Atvidade 4
console.log("Atividade 4")
formBtn.addEventListener("click", (event) => {
    event.preventDefault()
    const radio = document.querySelector(`input[name="fonte"]:checked`)
    preferencias.tema = temaSelect.value
    if (radio) {
        preferencias.fonte = radio.value
    } else {
        console.log("Nenhuma fonte foi selecionada.")
    }
    localStorage.setItem("Preferencias", JSON.stringify(preferencias))
    console.log(preferencias)
})

