const username = document.getElementById("username");
const tarefasBtn = document.getElementById("tarefas-btn");
const tarefasInput = document.getElementById("tarefas-input");
const tarefasList = document.getElementById("tarefas-list");
const tarefaContador = document.querySelector("#tarefa-contador")

// let namePrompt = prompt("Digite seu nome:")
// username.textContent = namePrompt;
const getTarefas = JSON.parse(localStorage.getItem("Tarefas"))
let tarefasArray = []
tarefasBtn.addEventListener("click", (event) => {
  if (tarefasInput.value !== "") {
    let tarefasInputValue = tarefasInput.value;
    let novoItem = document.createElement("div");
    novoItem.classList.add("tarefas-item");
    tarefasList.appendChild(novoItem);
    novoItem.innerHTML = `
                                <li class="tarefas-li">${tarefasInputValue}</li>
                                <button id="tarefas-removerBtn">Remover</button>
                            
    `;
    tarefasArray.push(novoItem)
    localStorage.setItem("Tarefas", JSON.stringify(tarefasArray))
    console.log(tarefasArray)
    tarefasInput.value = "";
    event.preventDefault();
  }
});

tarefasList.addEventListener("click", (event) => {
  if (event.target.tagName === "LI") {
    const li = event.target;
    if (li.style.textDecoration != "line-through") {
      li.style.textDecoration = "line-through";
    } else {
      li.style.textDecoration = "none";
    }
  }
  if (event.target.tagName === "BUTTON") {
    event.target.parentElement.remove();
  }
});
