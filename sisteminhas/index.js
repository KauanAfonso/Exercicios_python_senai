const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const session = require('express-session');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Configuração da sessão
app.use(session({
  secret: 'seu_segredo_aqui',
  resave: false,
  saveUninitialized: true,
}));

// Configuração do banco de dados
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'meu_banco_de_dados'
});

// Middleware de autenticação
function verificaAutenticacao(req, res, next) {
  if (req.session.user) {
    return next(); // Usuário autenticado
  }
  res.status(401).send('Você precisa estar logado para acessar esta página.');
}

// Endpoint de login
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  connection.query('SELECT * FROM usuarios WHERE username = ?', [username], (error, results) => {
    if (error) {
      return res.status(500).send('Erro ao acessar o banco de dados.');
    }

    if (results.length === 0) {
      return res.status(401).send('Usuário não encontrado.');
    }

    const user = results[0];

    // Verifica se a senha está correta (sem hash)
    if (user.password === password) {
      req.session.user = user; // Armazena o usuário na sessão
      return res.redirect('/index'); // Redireciona para a página de index
    } else {
      return res.status(401).send('Senha incorreta.');
    }
  });
});

// Rota protegida (exemplo do index)
app.get('/index', verificaAutenticacao, (req, res) => {
  res.send('Bem-vindo ao Index! Você está logado.');
});

// Rota para logout
app.post('/logout', (req, res) => {
  req.session.destroy(err => {
    if (err) {
      return res.status(500).send('Erro ao sair.');
    }
    res.send('Logout realizado com sucesso!');
    return res.redirect('/login')
  });
});

// Inicia o servidor
app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});
