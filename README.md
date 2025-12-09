# 🙋🏼‍♀️ Professora Elisa - Speech-to-Speech English Learning Assistant

Assistente de conversação em tempo real para aprendizado de inglês, usando reconhecimento de voz no navegador, IA generativa (Amazon Bedrock Nova Pro) e síntese de voz (Amazon Polly).

## 🚀 Funcionalidades

- **Speech-to-Speech em Tempo Real**: Fale em português e receba resposta em áudio
- **Push-to-Talk**: Pressione e segure ESPAÇO para falar
- **IA Conversacional**: Respostas curtas e naturais usando Amazon Nova Pro
- **Voz Brasileira**: Síntese de voz com Amazon Polly (voz Camila)
- **Interface Intuitiva**: Design moderno e responsivo
- **Serverless**: Backend na AWS com Lambda + API Gateway

## 🛠️ Tecnologias

- **Frontend**: Streamlit + HTML/CSS/JavaScript
- **Backend**: AWS Lambda (Python 3.12)
- **API**: AWS API Gateway REST
- **IA**: Amazon Bedrock (Nova Pro)
- **Text-to-Speech**: Amazon Polly
- **Speech Recognition**: Web Speech API (navegador)
- **Infraestrutura**: AWS CloudFormation

## 📋 Pré-requisitos

- Python 3.8+
- Conta AWS com acesso a:
  - Amazon Bedrock (modelo Nova Pro)
  - Amazon Polly
  - AWS Lambda
  - AWS API Gateway
  - Navegador Chrome ou Edge (para reconhecimento de voz)
  obs.: Mozilla Firefox, infelizmente não suporta

## ⚙️ Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/aryribeiro/professora-elisa.git
cd professora-elisa
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Deploy da infraestrutura AWS

Use o CloudFormation para criar a infraestrutura:

1. Acesse **AWS CloudFormation Console**
2. **Create stack** → Upload `cloudformation-template-FINAL.json`
3. Stack name: `professora-elisa-stack`
4. **Next** → **Next** → ✅ Acknowledge IAM → **Submit**
5. Aguarde `CREATE_COMPLETE`
6. Copie o **APIEndpoint** dos Outputs

obs.: crie as permissões para Polly e Bedrock manualmente, quando for criar seu access key e secret key.

### 4. Configure o endpoint

Edite `app.py` linha 21 com o endpoint copiado:
```python
API_ENDPOINT = "https://SEU_API_ID.execute-api.us-east-1.amazonaws.com/prod/chat"
```

### 5. Execute localmente
```bash
streamlit run app.py
```

## 🎮 Como Usar

1. Abra o navegador em `http://localhost:8501`
2. **Pressione e segure ESPAÇO** enquanto fala em português
3. Solte ESPAÇO para processar
4. Ouça a resposta da professora em áudio

## 🌐 Deploy em Produção

### Streamlit Cloud

1. Faça push do código para GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. **Main file**: `app.py`
5. **Deploy!**

Acesse: `https://seu-app.streamlit.app`

## 📁 Estrutura do Projeto

```
professora-elisa/
├── app.py                              # Frontend Streamlit
├── cloudformation-template-FINAL.json  # Infraestrutura AWS
├── requirements.txt                    # Dependências Python
├── README.md                          # Este arquivo
```

## 🔧 Configuração AWS

### Recursos Criados pelo CloudFormation

- **Lambda Function**: `ProfessoraElisaFunction`
  - Runtime: Python 3.12
  - Timeout: 30s
  - Memory: 512 MB
  - Bedrock Nova Pro + Polly integration

- **API Gateway**: `ProfessoraElisaAPI`
  - Tipo: REST API
  - Stage: prod
  - Endpoint: `/chat`
  - CORS habilitado

- **IAM Role**: `ProfessoraElisaLambdaRole`
  - Permissões: Bedrock, Polly, CloudWatch Logs

### Configuração do Bedrock

O sistema usa Amazon Nova Pro com:
- **Model ID**: `amazon.nova-pro-v1:0`
- **Temperature**: 0.8
- **Top P**: 0.9
- **Max Tokens**: 100

### System Prompt

```
Your name is Elisa. You are having a ONE-ON-ONE conversation 
with a single Brazilian adult learning English. Speak directly 
to THEM (not "pessoal" or "vocês").

RULES:
- Keep responses SHORT (1-2 sentences max)
- Speak naturally like talking to ONE friend
- Mix Portuguese and English naturally
- Ask simple questions to keep conversation flowing
- Be warm and encouraging
- NEVER give long lessons or lists
- Focus on natural back-and-forth dialogue

Keep it conversational and brief!
```

## 💰 Estimativa de Custos (AWS)

| Serviço | Custo Estimado/Mês |
|---------|-------------------|
| Lambda (1000 invocações) | $0.20 |
| API Gateway (1000 requests) | $3.50 |
| Bedrock Nova Pro (1000 requests) | $2.40 |
| Polly (1000 requests) | $4.00 |
| CloudWatch Logs | $0.50 |
| **TOTAL** | **~$10.60/mês** |

*Baseado em 1000 conversas/mês (~33/dia)*

## 🐛 Troubleshooting

### Erro na API
- Verifique se a stack foi criada com sucesso
- Confirme que o endpoint está correto no `app.py`
- Veja logs no CloudWatch Logs

### Reconhecimento de voz não funciona
- Use Chrome ou Edge (Firefox não suporta Web Speech API)
- Permita acesso ao microfone quando solicitado

### Erro 502 Bad Gateway
- Verifique logs da Lambda no CloudWatch
- Confirme que Bedrock Nova Pro está habilitado na sua conta

## 🔒 Segurança

- API pública (sem autenticação)
- CORS configurado para aceitar qualquer origem (`*`)
- Para produção, considere adicionar API Key ou Cognito

## 👨‍💻 Autor

**Ary Ribeiro**
- Email: aryribeiro@gmail.com
- GitHub: [aryribeiro](https://github.com/aryribeiro)
- LinkedIn: [aryribeiro](https://www.linkedin.com/in/aryribeiro)

## 📄 Licença

Este projeto é de uso educacional.

## 🔮 Roadmap

- [ ] Adicionar autenticação (Cognito)
- [ ] Histórico de conversas (DynamoDB)
- [ ] Suporte a mais idiomas
- [ ] Feedback de pronúncia
- [ ] Modo de prática com temas específicos

---

**Versão**: 1.1 (Serverless)  
**Última atualização**: Dezembro 2025
