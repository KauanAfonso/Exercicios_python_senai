let listaDeCursos = [
"Ciência da computação" ,
"Análise e desenvolvimento de sistemas" ,
"Engenharia da computação" , 
"Sistemas de informação",
"Gestão da tecnologia da Informação" , 
"Ciência de Dados" ,
"Engenharia de software",
"Segurança da Informação"
]

let tamanho = listaDeCursos.length - 1
let numeroAleatorio = parseInt(Math.random() * tamanho + 1)
let nome = "Kauan"

console.log(`Parabéns ${nome}!! Seu curso é: ${listaDeCursos[numeroAleatorio]} `)