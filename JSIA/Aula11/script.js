//Atividade 1
console.log("Atividade 1")
const addBtn = document.getElementById("addBtn")

btnClick = () => alert("Click")
addBtn.addEventListener("click", () => alert("Click 2"))

//Atividade 2
console.log("Atividade 2")
const ulBtn = document.getElementById("ulBtn")
const ul = document.getElementById("ul")
const tarefa = document.getElementById("tarefa")

ulBtn.addEventListener("click", ()=>{
    let item = document.createElement("li")
    let tarefaValue = tarefa.value
    ul.appendChild(item)
    item.innerHTML = tarefaValue
})

//Atividade 3
console.log("Atividade 3")
const cartaoBtn = document.getElementById("cartaoBtn")
const tituloInput = document.getElementById("tituloInput")
const descInput = document.getElementById("descInput")

cartaoBtn.addEventListener("click", (event)=>{
    let novoDiv = document.createElement("div")
    let tituloDiv = document.createElement("h3")
    let descDiv = document.createElement("p")
    let tituloValue = tituloInput.value
    let descValue = descInput.value

    document.body.appendChild(novoDiv)
    novoDiv.style.outline = "2px solid red"
    novoDiv.appendChild(tituloDiv)
    console.log(tituloDiv)
    tituloDiv.innerHTML = tituloValue
    novoDiv.appendChild(descDiv)
    descDiv.innerHTML = descValue
    event.preventDefault()

})

//Atividade 4
console.log("Atividade 4")

const atv4 = document.getElementById("atv4")

// atv4.addEventListener("mousemove", (event)=> {
//     let coordenadas = document.createElement("p")
//     atv4.appendChild(coordenadas)
//     coordenadas.innerHTML = 
//     `   <p>Coordenadas X:${event.offsetX}</p>
//         <p>Coordenadas Y:${event.offsetY}</p>
//     `
// })