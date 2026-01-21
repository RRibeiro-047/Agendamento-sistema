# 📅 Sistema de Agendamentos

Um sistema completo para gerenciamento de agendamentos desenvolvido com Flask, ideal para barbearias, salões de beleza, clínicas e outros negócios que necessitam de controle de reservas.

## 🚀 Tecnologias Utilizadas

### Backend
- **Python 3.x** - Linguagem principal
- **Flask** - Framework web leve e flexível
- **SQLite** - Banco de dados relacional
- **Jinja2** - Template engine para renderização HTML

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilização moderna
- **Bootstrap 5.3.2** - Framework CSS responsivo
- **JavaScript** - Interatividade e validações
- **Font Awesome 6.4.0** - Ícones profissionais

### Banco de Dados
- **SQLite3** - Armazenamento local e leve
- **Schema**: `agendamentos` (id, nome, servico, data, hora, data_criacao)

## 📁 Estrutura do Projeto

```
sistema-agenda/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── database.db           # Banco de dados SQLite
├── templates/            # Páginas HTML
│   ├── index.html        # Página principal de agendamento
│   └── admin.html        # Painel administrativo
├── static/               # Arquivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos personalizados
│   └── js/
│       └── script.js     # Lógica JavaScript
└── README.md            # Documentação do projeto
```

## 🛠️ Funcionalidades

### Para Clientes
- ✅ **Agendamento Online**: Formulário intuitivo para reservas
- ✅ **Validação em Tempo Real**: Verificação de dados antes do envio
- ✅ **Feedback Visual**: Confirmações e mensagens de erro amigáveis
- ✅ **Design Responsivo**: Funciona em desktop, tablet e mobile

### Para Administradores
- ✅ **Painel Administrativo**: Interface completa para gestão
- ✅ **Dashboard com Estatísticas**: Total, hoje e semana
- ✅ **Lista de Agendamentos**: Tabela detalhada com todos os dados
- ✅ **Auto-refresh**: Atualização automática a cada 30 segundos
- ✅ **Ordenação Cronológica**: Agendamentos mais recentes primeiro
- ✅ **Interface Profissional**: Design moderno com gradientes e animações

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.7+ instalado
- Git (opcional)

### Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone <URL-do-repositório>
   cd sistema-agenda
   ```

2. **Crie ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a aplicação**
   ```bash
   python app.py
   ```

6. **Acesse a aplicação**
   - Página principal: `http://localhost:5000/`
   - Painel admin: `http://localhost:5000/admin`

## 📋 Dependências

O arquivo `requirements.txt` contém:
```
Flask==2.3.3
```

## 🗄️ Banco de Dados

O sistema utiliza SQLite com a seguinte estrutura:

```sql
CREATE TABLE agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    servico TEXT NOT NULL,
    data TEXT NOT NULL,
    hora TEXT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

O banco de dados é criado automaticamente na primeira execução.

## 🎨 Design e UX

### Características de Design
- **Interface Moderna**: Gradientes, sombras e animações suaves
- **Cores Profissionais**: Esquema roxo/azul com contraste adequado
- **Tipografia Clara**: Hierarquia visual bem definida
- **Ícones Intuitivos**: Font Awesome para melhor compreensão
- **Layout Responsivo**: Adaptável a todos os dispositivos

### Experiência do Usuário
- **Feedback Imediato**: Respostas rápidas às ações do usuário
- **Validações Preventivas**: Evita erros antes de ocorrerem
- **Mensagens Claras**: Textos informativos e amigáveis
- **Navegação Intuitiva**: Fluxos lógicos e previsíveis

## 🔧 Configuração

### Variáveis de Ambiente (Opcional)
```python
# Em app.py
app.config['DEBUG'] = True  # Desativar em produção
app.config['SECRET_KEY'] = 'sua-chave-secreta'  # Para segurança
```

### Porta do Servidor
Por padrão, a aplicação roda na porta 5000. Para alterar:
```python
if __name__ == "__main__":
    app.run(debug=True, port=8080)
```

## 📱 API Endpoints

### Rotas Disponíveis
- `GET /` - Página principal de agendamento
- `POST /agendar` - Processa novo agendamento
- `GET /admin` - Painel administrativo

### Formato de Dados

**POST /agendar**
```json
{
    "nome": "João Silva",
    "servico": "Corte de Cabelo",
    "data": "20/01/2026",
    "hora": "14:30"
}
```

**Resposta de Sucesso**
```json
{
    "status": "success",
    "message": "Agendamento realizado com sucesso!"
}
```

**Resposta de Erro**
```json
{
    "status": "error",
    "message": "Dados incompletos"
}
```

## 🔒 Segurança

### Medidas Implementadas
- ✅ **Validação de Entrada**: Verificação de todos os dados recebidos
- ✅ **SQL Injection Protection**: Uso de parâmetros em queries
- ✅ **Error Handling**: Tratamento adequado de exceções
- ✅ **Sanitização**: Dados limpos antes do processamento

### Recomendações para Produção
- 🔒 Desativar modo debug
- 🔒 Implementar autenticação no painel admin
- 🔒 Usar HTTPS
- 🔒 Configurar firewall
- 🔒 Fazer backup regular do banco de dados

## 🚀 Deploy

### Opções de Hospedagem
1. **Heroku** - Fácil configuração para Python
2. **PythonAnywhere** - Focado em aplicações Python
3. **VPS DigitalOcean** - Controle total
4. **AWS EC2** - Escalabilidade infinita

### Deploy no Heroku (Exemplo)
```bash
# Instalar Heroku CLI
heroku create seu-app-name
git push heroku main
heroku run python -c "from app import init_db; init_db()"
```

## 🤝 Contribuição

### Como Contribuir
1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Diretrizes
- Seguir PEP 8 para código Python
- Comentários em português brasileiro
- Testar todas as funcionalidades antes de PR
- Manter compatibilidade com Python 3.7+

## 📝 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

### Dúvidas e Sugestões
- 📧 Email: contato@exemplo.com
- 💬 WhatsApp: (XX) XXXXX-XXXX
- 🐛 Issues: GitHub Issues do projeto

### Documentação Adicional
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [SQLite Documentation](https://sqlite.org/docs.html)

---

## 🎯 Roadmap Futuro

### Próximas Funcionalidades
- 📅 **Calendário Visual**: Interface com calendário mensal
- 📧 **Notificações por Email**: Lembretes para clientes
- 📱 **Aplicativo Mobile**: Versão nativa para iOS/Android
- 💳 **Pagamentos Online**: Integração com gateways de pagamento
- 📊 **Relatórios Avançados**: Análises e estatísticas detalhadas
- 👥 **Múltiplos Profissionais**: Cadastro de diferentes atendentes
- ⏰ **Gestão de Horários**: Configuração de disponibilidade

### Melhorias Técnicas
- 🔄 **API RESTful**: Endpoint completo para integrações
- 🗄️ **PostgreSQL**: Opção para banco de dados mais robusto
- 🐳 **Docker**: Containerização para deploy simplificado
- 🧪 **Testes Automáticos**: Suite de testes unitários e integração
- 📝 **Logging Sistema**: Registro de atividades e auditoria

---

**Desenvolvido com ❤️ usando Python e Flask**
