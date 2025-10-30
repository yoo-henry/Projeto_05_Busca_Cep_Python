import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####


##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####

st.sidebar.title("Busca CEP")
st.sidebar.image("logo.png")
pagina = st.sidebar.selectbox("Escolha uma das opções:", opcoes) 

# Buscar CEP

if pagina == "Buscar CEP":
    st.title("Buscar CEP")
    st.image("principal.png")


# Descobrir CEP

elif pagina == "Descobrir CEP":
    st.title("Descobrir CEP")
    st.image("descobrir.png")
    st.title("Descobrir CEP pelo Endereço")
    st.write("Digite o endereço (ex:Rua Olga, Barueri, SP)")

##### BOTÃO BUSCAR CEP #####

if pagina == "Buscar CEP":
    st.header("Buscar endereço pelo CEP")
    cep = st.text_input("Digite o CEP (somente números):")


    if st.button("Buscar"):
            if len(cep) != 8 or not cep.isdigit():
                st.error("Por favor, insira um CEP  válido com 8 digitos numéricos.")
            else:
                try:
                    endereço = BuscarCep.buscar_cep(cep)
                    if endereço:
                         st.success("Endereço encontrado:")
                         st.write(f"CEP: {endereço[0]}")
                         st.write(f"Endereço: {endereço[1]}")
                         st.write(f"Bairro: {endereço[2]}")
                         st.write(f"cidade: {endereço[3]}")
                         st.write(f"Estado: {endereço[4]}")

                         ## Mapas
                         st.title("Localização no Mapa")
                         df = pd.DataFrame({"latitude": [endereço[5]], "longitude": [endereço[6]]})
                         st.map(df, zoom=15)
                    else:
                         st.error("CEP não encontrado")
                except Exception as e:
                     st.error(f"Ocorreu um erro ao buscar o CEP: {e}")
        
             

##### BOTÃO DESCOBRIR CEP #####

elif pagina == "Descobrir CEP":
    st.header("Descobrir CEP pelo Endereço")
    endereço_usuario = st.text_input("Digite o endereço (ex: Rua Olga, Barueri, SP):")

    if st.button("Descobrir"):
            if not endereço_usuario.strip():
               st.error("Por favor, insira um endereço válido.")
            else:
                try:
                    resultado = BuscarCep.descobrir_cep(endereço_usuario)
                    st.success("Link de busca no Google")
                    st.write(resultado)
                except Exception as e:
                    st.error(f"Ocorreu um erro ao descobrir CEP: {e}")
