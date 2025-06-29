const username = document.getElementById("username");
const tarefasBtn = document.getElementById("tarefas-btn");
const tarefasInput = document.getElementById("tarefas-input");
const tarefasList = document.getElementById("tarefas-list");

// let namePrompt = prompt("Digite seu nome:")
// username.textContent = namePrompt;

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
