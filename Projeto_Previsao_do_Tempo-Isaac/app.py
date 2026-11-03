import streamlit as st
from dados_api import previsao_temperatura

#Cidades
cidades = {
    "Santana de Parnaíba": [-23.4442, -46.9178],
    "Paris": [48.8566, 2.3522],
    "Tóquio": [35.67649849393377, 139.7731277308499],
    "New York": [40.7128, -74.0060],
    "Chichén Itzá": [20.6843, -88.5678],
    "Atenas": [37.9838, 23.7275],
    "Hong Kong": [22.3193, 114.1694]
}

st.sidebar.title("Previsão do Tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a Cidade:",cidades.keys())
latitude , longitude = cidades[cidade]

st.title(f'Previsão do Tempo em {cidade} paras os Próximos 7 Dias.')
st.markdown("---")

dados,temperatura_media = previsao_temperatura(latitude,longitude)

for i,d in temperatura_media.iterrows():
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1,col2,col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura Média",f"{d['temperatura_media']:.2f}º")

        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"
            elif d['temperatura_media'] < 18:
                temp = "cool.png"
            elif d['temperatura_media'] < 25:
                temp = "comfort.png"
            else:
                temp = "warm.png"

            st.image(temp,width=40)