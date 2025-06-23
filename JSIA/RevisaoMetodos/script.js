// //Processador de Dados de Vendas
// Banco de dados = Array
// Menu interativo = opcional
// Funcionalidades:
// 1. Calcular o valor total de cada venda
// 2. Filtrar vendas de uma certa categoria
// 3. Calcular o valor total de vendas de certa categoria
// 4. Listar o produto mais vendido
// 5. Calcular a media de preço de todos os produtos
// 6. Agrupar vendas por mês
// 7. Ordenar vendas por atributo (preço, quantidade ou data)

// Objeto:
// ID: inteiro, produto: String, preço: float, quantidade: int, categoria: String, data: String

const produtos = [
  { id: 1, produto: "Teclado", preco: 129.90, quantidade: 10, categoria: "Periféricos", data: "2025-06-01" },
  { id: 2, produto: "Mouse", preco: 79.99, quantidade: 15, categoria: "Periféricos", data: "2025-06-02" },
  { id: 3, produto: "Monitor", preco: 899.00, quantidade: 7, categoria: "Eletrônicos", data: "2025-06-03" },
  { id: 4, produto: "Cabo HDMI", preco: 25.50, quantidade: 20, categoria: "Acessórios", data: "2025-06-04" },
  { id: 5, produto: "Notebook", preco: 3599.90, quantidade: 5, categoria: "Informática", data: "2025-06-05" },
  { id: 6, produto: "Webcam", preco: 199.00, quantidade: 8, categoria: "Periféricos", data: "2025-06-06" },
  { id: 7, produto: "Pen Drive 32GB", preco: 39.90, quantidade: 25, categoria: "Armazenamento", data: "2025-06-07" },
  { id: 8, produto: "HD Externo", preco: 329.99, quantidade: 4, categoria: "Armazenamento", data: "2025-06-08" },
  { id: 9, produto: "SSD 500GB", preco: 299.90, quantidade: 9, categoria: "Armazenamento", data: "2025-06-09" },
  { id: 10, produto: "Fonte 600W", preco: 249.00, quantidade: 6, categoria: "Hardware", data: "2025-06-10" },
  { id: 11, produto: "Placa de Vídeo", preco: 1299.90, quantidade: 3, categoria: "Hardware", data: "2025-06-11" },
  { id: 12, produto: "Memória RAM 8GB", preco: 199.90, quantidade: 10, categoria: "Hardware", data: "2025-06-12" },
  { id: 13, produto: "Gabinete Gamer", preco: 349.90, quantidade: 4, categoria: "Hardware", data: "2025-06-13" },
  { id: 14, produto: "Cooler CPU", preco: 89.90, quantidade: 10, categoria: "Hardware", data: "2025-06-14" },
  { id: 15, produto: "Cadeira Gamer", preco: 999.00, quantidade: 2, categoria: "Mobiliário", data: "2025-06-15" },
  { id: 16, produto: "Roteador Wi-Fi", preco: 249.90, quantidade: 6, categoria: "Redes", data: "2025-06-16" },
  { id: 17, produto: "Switch Ethernet", preco: 179.00, quantidade: 4, categoria: "Redes", data: "2025-06-17" },
  { id: 18, produto: "Notebook Gamer", preco: 5999.90, quantidade: 3, categoria: "Informática", data: "2025-06-18" },
  { id: 19, produto: "Impressora", preco: 699.00, quantidade: 4, categoria: "Periféricos", data: "2025-06-19" },
  { id: 20, produto: "Scanner", preco: 449.90, quantidade: 3, categoria: "Periféricos", data: "2025-06-20" },
  { id: 21, produto: "Headset", preco: 149.90, quantidade: 12, categoria: "Áudio", data: "2025-06-21" },
  { id: 22, produto: "Caixa de Som Bluetooth", preco: 229.00, quantidade: 7, categoria: "Áudio", data: "2025-06-22" },
  { id: 23, produto: "Microfone USB", preco: 349.00, quantidade: 5, categoria: "Áudio", data: "2025-06-10" },
  { id: 24, produto: "Estabilizador", preco: 199.90, quantidade: 6, categoria: "Energia", data: "2025-06-05" },
  { id: 25, produto: "Nobreak", preco: 899.90, quantidade: 4, categoria: "Energia", data: "2025-06-11" },
  { id: 26, produto: "Tablet", preco: 1299.90, quantidade: 6, categoria: "Eletrônicos", data: "2025-06-01" },
  { id: 27, produto: "Carregador Universal", preco: 89.90, quantidade: 10, categoria: "Acessórios", data: "2025-06-03" },
  { id: 28, produto: "Suporte de Monitor", preco: 59.90, quantidade: 15, categoria: "Acessórios", data: "2025-06-07" },
  { id: 29, produto: "Adaptador USB", preco: 19.90, quantidade: 20, categoria: "Acessórios", data: "2025-06-09" },
  { id: 30, produto: "Controle USB", preco: 139.90, quantidade: 8, categoria: "Periféricos", data: "2025-06-12" }
];

// valorTotalVenda = produtos.map(num => num.preco * num.quantidade)
// console.log(valorTotalVenda)

// filtrarVendasCategoria = produtos.filter(nome => {
//     if (nome.categoria === "Energia"){
//         return nome.id
//     }
// })
// console.log(filtrarVendasCategoria)
vendasTotalCategoria = produtos.reduce((acumulador=0, valor) => {
    if (valor.categoria === "Energia"){
        valor.vendasTotais = valor.preco * valor.quantidade
        console.log(`Vendas Totais: ${valor.vendasTotais}`)
        acumulador=valor.vendasTotais + acumulador.
        console.log(`Acumulador: ${acumulador}`)
    }
    return acumulador
})

console.log(vendasTotalCategoria)