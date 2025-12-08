import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Professora Elisa!", page_icon="🙋🏼‍♀️", layout="centered")

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🙋🏼‍♀️ Professora Elisa!</h1><p>Conversa em Tempo Real - Speech-to-Speech</p></div>', unsafe_allow_html=True)

# API Gateway endpoint gerado pelo CloudFormation
API_ENDPOINT = "https://fgtailjin9.execute-api.us-east-1.amazonaws.com/prod/chat"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .container {{
            background: white;
            border-radius: 30px;
            padding: 50px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 500px;
            width: 100%;
        }}
        #talkButton {{
            width: 200px;
            height: 200px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-size: 80px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            margin: 20px auto;
        }}
        #talkButton:hover {{
            transform: scale(1.05);
        }}
        #talkButton.listening {{
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
            animation: pulse 1s infinite;
        }}
        #talkButton.speaking {{
            background: linear-gradient(135deg, #6bcf7f 0%, #48bb78 100%);
            animation: pulse 1s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
        }}
        #status {{
            margin-top: 30px;
            font-size: 22px;
            font-weight: bold;
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="container">
        <button id="talkButton">🎤</button>
        <div id="status">Pressione ESPAÇO para falar</div>
    </div>

    <script>
        const API_URL = '{API_ENDPOINT}';
        let currentAudio = null;
        let isProcessing = false;
        
        const button = document.getElementById('talkButton');
        const status = document.getElementById('status');
        
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        
        if (!SpeechRecognition) {{
            status.textContent = '❌ Use Chrome ou Edge';
            button.disabled = true;
        }} else {{
            const recognition = new SpeechRecognition();
            recognition.lang = 'pt-BR';
            recognition.continuous = false;
            recognition.interimResults = false;
            
            let isRecognizing = false;
            
            document.addEventListener('keydown', (e) => {{
                if (e.code === 'Space' && !isRecognizing && !isProcessing) {{
                    e.preventDefault();
                    isRecognizing = true;
                    recognition.start();
                    button.className = 'listening';
                    button.innerHTML = '🔴';
                    status.textContent = '🔴 Ouvindo... Solte ESPAÇO';
                }}
            }});
            
            document.addEventListener('keyup', (e) => {{
                if (e.code === 'Space' && isRecognizing) {{
                    e.preventDefault();
                    recognition.stop();
                }}
            }});
            
            recognition.onresult = async (event) => {{
                const transcript = event.results[0][0].transcript;
                console.log('Você disse:', transcript);
                
                button.className = '';
                button.innerHTML = '⏳';
                status.textContent = '⏳ Aguardando resposta...';
                isProcessing = true;
                
                try {{
                    const response = await fetch(API_URL, {{
                        method: 'POST',
                        headers: {{
                            'Content-Type': 'application/json',
                        }},
                        body: JSON.stringify({{ text: transcript }})
                    }});
                    
                    if (!response.ok) {{
                        throw new Error('Erro na API: ' + response.status);
                    }}
                    
                    const data = await response.json();
                    console.log('Resposta:', data.text);
                    
                    // Decode base64 audio
                    const audioBytes = Uint8Array.from(atob(data.audio), c => c.charCodeAt(0));
                    const audioBlob = new Blob([audioBytes], {{ type: 'audio/mpeg' }});
                    const audioUrl = URL.createObjectURL(audioBlob);
                    
                    playAudio(audioUrl);
                    
                }} catch (error) {{
                    console.error('Erro:', error);
                    status.textContent = '❌ Erro: ' + error.message;
                    button.className = '';
                    button.innerHTML = '🎤';
                    isProcessing = false;
                }}
            }};
            
            recognition.onend = () => {{
                isRecognizing = false;
            }};
            
            recognition.onerror = (event) => {{
                console.error('Erro reconhecimento:', event.error);
                isRecognizing = false;
                
                if (!isProcessing) {{
                    if (event.error === 'no-speech') {{
                        status.textContent = '⚠️ Não ouvi nada. Tente novamente';
                    }} else if (event.error === 'aborted') {{
                        status.textContent = '🎙️ Pressione ESPAÇO para falar';
                    }} else {{
                        status.textContent = '🎙️ Pressione ESPAÇO para falar';
                    }}
                    button.className = '';
                    button.innerHTML = '🎤';
                }}
            }};
        }}
        
        function playAudio(audioUrl) {{
            if (currentAudio) {{
                currentAudio.pause();
                currentAudio = null;
            }}
            
            button.className = 'speaking';
            button.innerHTML = '🔊';
            status.textContent = '🔊 Professora falando...';
            
            currentAudio = new Audio(audioUrl);
            currentAudio.volume = 1.0;
            currentAudio.play();
            
            currentAudio.onended = () => {{
                URL.revokeObjectURL(audioUrl);
                currentAudio = null;
                button.className = '';
                button.innerHTML = '🎤';
                status.textContent = '🎙️ Pressione ESPAÇO para falar';
                isProcessing = false;
            }};
            
            currentAudio.onerror = () => {{
                console.error('Erro ao reproduzir áudio');
                status.textContent = '❌ Erro ao reproduzir áudio';
                button.className = '';
                button.innerHTML = '🎤';
                isProcessing = false;
            }};
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=600)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <strong>🙋🏼‍♀️ Professora Elisa!</strong> - Desenvolvido para interação em tempo real<br>
    Criado por <strong>Ary Ribeiro</strong>: <a href="mailto:aryribeiro@gmail.com">aryribeiro@gmail.com</a><br>
    <small>Versão 1.0 | Streamlit + Python</small>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        color: #333333;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    /* Esconde completamente todos os elementos da barra padrão do Streamlit */
    header {display: none !important;}
    footer {display: none !important;}
    #MainMenu {display: none !important;}
    /* Remove qualquer espaço em branco adicional */
    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    /* Remove quaisquer margens extras */
    .element-container {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
</style>
""", unsafe_allow_html=True)