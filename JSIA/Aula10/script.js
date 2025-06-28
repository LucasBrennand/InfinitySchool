//Atividade 2
console.log("Atividade 2")
const paragrafo = document.getElementsByTagName("p")
for(i of paragrafo){
    i.innerHTML = "texto alterado"
}

//Atividade 3
console.log("Atividade 3")
const box = document.querySelectorAll(".box")
for(i of box){
    i.style = "background-color: blue"
}

//Atividade 4
console.log("Atividade 4")
const minhaImagem = document.getElementById("minhaImagem")
const meuLink = document.getElementById("meuLink")
mudarLinks = () =>{
    minhaImagem.setAttribute("src", "https://i.ytimg.com/vi/DQnVWG7jUXs/maxresdefault.jpg")
    meuLink.setAttribute("href", "https://i.ytimg.com/vi/DQnVWG7jUXs/maxresdefault.jpg")
}

//Atividade 5
console.log("Atividade 5")
const container = document.getElementById("container")
const botaoAdd = document.getElementById("adicionarParagrafo")
const botaoRemove = document.getElementById("removerParagrafo")

let arrayP = []
let novoP = ""
botaoAdd.addEventListener("click", ()=>{
    novoP = document.createElement("p")
    novoP.innerHTML = 
    `
    <p class="lorem">lorem24</p>
    `
    container.appendChild(novoP)
    console.log(novoP)


    
})

botaoRemove.addEventListener("click", ()=>{
    container.removeChild(novoP)
    
})

