//Atividade 1
console.log("Atividade 1")

const enviar = document.getElementById("enviar")
const nomeInput = document.getElementById("nome-input")
const para = document.getElementById("para")

const nomeLista = []
enviar.addEventListener("click", (event) => {
    let nomeInputValue = nomeInput.value
    let li = document.createElement("li")
    para.appendChild(li)
    li.textContent = nomeInputValue
    nomeLista.push(nomeInputValue)
    localStorage.setItem("nome", JSON.stringify(nomeLista))
})
lista = JSON.parse(localStorage.getItem("nome"))
console.log(lista)
items = document.createElement("li")
items.textContent = JSON.parse(localStorage.getItem("nome") )
para.appendChild(items)
console.log(items)
