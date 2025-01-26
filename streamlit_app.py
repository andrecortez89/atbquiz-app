import streamlit as st
import random

# Definição das perguntas e respostas
perguntas = [
    {
        "pergunta": "Qual o mecanismo de ação dos betalactâmicos?",
        "opcoes": [
            "Inibição da síntese de DNA",
            "Inibição da síntese da parede celular",
            "Inibição da síntese proteica",
            "Desestabilização da membrana celular"
        ],
        "correta": "Inibição da síntese da parede celular"
    },
    {
        "pergunta": "Qual destas classes é eficaz contra bactérias atípicas?",
        "opcoes": ["Macrolídeos", "Betalactâmicos", "Aminoglicosídeos", "Glicopeptídeos"],
        "correta": "Macrolídeos"
    },
    {
        "pergunta": "Qual antibiótico pertence à classe das quinolonas?",
        "opcoes": ["Cefepima", "Amicacina", "Ciprofloxacino", "Vancomicina"],
        "correta": "Ciprofloxacino"
    },
    {
        "pergunta": "Qual classe de antimicrobianos é conhecida por causar nefrotoxicidade e ototoxicidade?",
        "opcoes": ["Macrolídeos", "Tetraciclinas", "Aminoglicosídeos", "Sulfonamidas"],
        "correta": "Aminoglicosídeos"
    },
    {
        "pergunta": "Qual dessas opções é um antibiótico bacteriostático?",
        "opcoes": ["Vancomicina", "Linezolida", "Meropenem", "Ceftriaxona"],
        "correta": "Linezolida"
    },
    {
        "pergunta": "Os carbapenêmicos possuem qual espectro de ação?",
        "opcoes": [
            "Gram-positivos apenas",
            "Gram-negativos apenas",
            "Gram-positivos e Gram-negativos",
            "Somente anaeróbios"
        ],
        "correta": "Gram-positivos e Gram-negativos"
    }
]

# Inicializar variáveis de estado do Streamlit
if "indice_pergunta" not in st.session_state:
    st.session_state.indice_pergunta = 0
    st.session_state.pontuacao = 0
    st.session_state.perguntas_embaralhadas = random.sample(perguntas, len(perguntas))
    st.session_state.respostas_usuario = []

# Título do quiz
st.title("💊 Quiz Interativo: Classes de Antimicrobianos")

# Verifica se ainda há perguntas a serem respondidas
if st.session_state.indice_pergunta < len(st.session_state.perguntas_embaralhadas):
    pergunta_atual = st.session_state.perguntas_embaralhadas[st.session_state.indice_pergunta]

    st.subheader(f"🔹 Pergunta {st.session_state.indice_pergunta + 1} de {len(perguntas)}")
    st.write(pergunta_atual["pergunta"])

    escolha = st.radio("Escolha uma opção:", pergunta_atual["opcoes"], index=None, key=f"pergunta_{st.session_state.indice_pergunta}")

    if st.button("Confirmar Resposta"):
        if escolha:
            # Verifica se a resposta está correta
            if escolha == pergunta_atual["correta"]:
                st.success("✅ Resposta correta!")
                st.session_state.pontuacao += 1
            else:
                st.error(f"❌ Resposta incorreta! A resposta correta era: {pergunta_atual['correta']}")

            # Salvar a resposta para revisão posterior
            st.session_state.respostas_usuario.append({
                "pergunta": pergunta_atual["pergunta"],
                "resposta_usuario": escolha,
                "resposta_correta": pergunta_atual["correta"]
            })

            # Avança para a próxima pergunta
            st.session_state.indice_pergunta += 1
            st.rerun()  # Atualiza a interface corretamente

# Exibir o resultado final quando todas as perguntas forem respondidas
else:
    st.subheader("🎯 Resultado Final")
    st.write(f"Você acertou **{st.session_state.pontuacao}** de **{len(perguntas)}** perguntas!")

    st.write("### 📋 Resumo das respostas:")
    for i, resposta in enumerate(st.session_state.respostas_usuario):
        st.write(f"**{i+1}. {resposta['pergunta']}**")
        if resposta['resposta_usuario'] == resposta['resposta_correta']:
            st.write(f"✅ **{resposta['resposta_usuario']}** (Correto)")
        else:
            st.write(f"❌ **{resposta['resposta_usuario']}** (Errado) → ✅ Correto: **{resposta['resposta_correta']}**")

    # Botão para reiniciar o quiz
    if st.button("🔄 Refazer o Quiz"):
        st.session_state.indice_pergunta = 0
        st.session_state.pontuacao = 0
        st.session_state.perguntas_embaralhadas = random.sample(perguntas, len(perguntas))
        st.session_state.respostas_usuario = []
        st.rerun()  # Atualiza a página para reiniciar o quiz
