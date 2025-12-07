# 🎓 Professora Elisa! - Speech-to-Speech English Learning Assistant

Assistente de conversação em tempo real para aprendizado de inglês, usando reconhecimento de voz, IA generativa (Amazon Bedrock Nova Pro) e síntese de voz (Amazon Polly).

## 🚀 Funcionalidades

- **Speech-to-Speech em Tempo Real**: Fale em português e receba resposta em áudio
- **Push-to-Talk**: Pressione e segure ESPAÇO para falar
- **IA Conversacional**: Respostas curtas e naturais usando Amazon Nova Pro
- **Voz Brasileira**: Síntese de voz com Amazon Polly (voz Camila)
- **Interface Intuitiva**: Design moderno e responsivo

## 🛠️ Tecnologias

- **Frontend**: Streamlit + HTML/CSS/JavaScript
- **Backend**: FastAPI + WebSocket
- **IA**: Amazon Bedrock (Nova Pro)
- **Text-to-Speech**: Amazon Polly
- **Speech Recognition**: Web Speech API (navegador)

## 📋 Pré-requisitos

- Python 3.8+
- Conta AWS com acesso a:
  - Amazon Bedrock (modelo Nova Pro)
  - Amazon Polly
- Navegador Chrome ou Edge (para reconhecimento de voz)

## ⚙️ Instalação

1. **Clone o repositório**
```bash
git clone <seu-repositorio>
cd professora-elisa
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure as credenciais AWS**

Crie um arquivo `.env` na raiz do projeto:
```env
AWS_ACCESS_KEY_ID=sua_access_key
AWS_SECRET_ACCESS_KEY=sua_secret_key
```

4. **Execute a aplicação**
```bash
streamlit run app.py
```

O backend será iniciado automaticamente na porta 8001.

## 🎮 Como Usar

1. Abra o navegador em `http://localhost:8501`
2. Clique no botão do microfone para conectar
3. **Pressione e segure ESPAÇO** enquanto fala em português
4. Solte ESPAÇO para processar
5. Ouça a resposta da professora em áudio

## 📁 Estrutura do Projeto

```
professora-elisa/
├── app.py              # Frontend Streamlit
├── backend.py          # Backend FastAPI com WebSocket
├── requirements.txt    # Dependências Python
├── .env               # Credenciais AWS (não commitar!)
└── README.md          # Este arquivo
```

## 🔧 Configuração AWS

### Permissões IAM Necessárias

Sua conta AWS precisa das seguintes permissões:
- `bedrock:InvokeModel` (para Amazon Nova Pro)
- `polly:SynthesizeSpeech` (para Amazon Polly)

### Regiões Suportadas

- Amazon Bedrock: `us-east-1`
- Amazon Polly: `us-east-1`

## 🌐 Arquitetura

```
┌─────────────────┐
│   Streamlit     │
│   (Frontend)    │
└────────┬────────┘
         │
         │ WebSocket
         │
┌────────▼────────┐
│    FastAPI      │
│   (Backend)     │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│Bedrock│ │ Polly │
│ Nova  │ │Camila │
└───────┘ └───────┘
```

## 🎯 Prompt do Sistema

O assistente é configurado para:
- Conversar one-on-one (não em grupo)
- Respostas curtas (2-3 frases)
- Misturar português e inglês naturalmente
- Ser encorajador e amigável
- Fazer perguntas simples para manter a conversa

## 🐛 Troubleshooting

### Backend não inicia
- Verifique se a porta 8001 está livre
- Confirme que as credenciais AWS estão corretas no `.env`

### Reconhecimento de voz não funciona
- Use Chrome ou Edge (Firefox não suporta Web Speech API)
- Permita acesso ao microfone quando solicitado

### Erro de permissão AWS
- Verifique se sua conta tem acesso ao Bedrock e Polly
- Confirme que o modelo Nova Pro está habilitado na sua região

## 📝 Notas

- **Ambiente Local**: Esta versão funciona apenas localmente (localhost)
- **Navegador**: Requer Chrome ou Edge para reconhecimento de voz
- **Custos AWS**: Bedrock e Polly são serviços pagos (consulte preços AWS)

## 👨‍💻 Autor

**Ary Ribeiro**
- Email: aryribeiro@gmail.com

## 📄 Licença

Este projeto é de uso educacional.

## 🔮 Roadmap

- [ ] Deploy em produção com backend público
- [ ] Suporte a mais idiomas
- [ ] Histórico de conversas persistente
- [ ] Modo de prática com temas específicos
- [ ] Feedback de pronúncia

---

**Versão**: 1.0  
**Última atualização**: 2024
