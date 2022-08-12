# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image

image01 = Image.open('57368940_393784414789934_3557869638635225088_n.jpg')
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("ROVI MADEIRAS LTDA - ME")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("CONFIANÇA, QUALIDADE E PREÇO")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("CNPJ: 098.098.098/0001-03")
st.subheader("RUA SERVIDÃO 6, 100")
st.subheader("CHÁCARAS HAVAÍ, HORTOLÂNDIA - SP")
# Use st.write("") para adicionar um texto ao seu Web app
st.write("NESSA PÁGINA VOCÊ PODERÁ INICIAR UM ORÇAMENTO COM NOSSA EMPRESA, PARA MAIS INFORMAÇÕES, ACESSE O LINK PARA O NOSSO WHATSAPP")
st.write("HORÁRIO DE FUNCIONAMENTO: DE SEGUNDA À SEXTA DAS 7:30 ÀS 17:00")
st.subheader("------ **Desenvolvido por: Massaki de O. Igarashi** -----")

menu = ["PBR",
        "PALLET_DE_VIGA",
        "PALLET_PERSONALIZADO",
        "MENU"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("Texto Side Bar")
    
if choice == "PBR":       
    st.subheader("PADRÃO BRASILEIRO DE PALLET")
    st.write("SIGA O LINK PARA INFORMAÇÕES DE VALORES")    
    cols01 = st.columns(3)    
    cols01[0].write('QUANTIDADE DE PALLETS POR CARGA')
    cols01[1].write('QUANTIDADE DE PALLETS POR MÊS')
    cols02[2].write('PERSONALIZAÇÃO ESPECIAL: SUPERIOR FECHADO, TOCO COM TAMANHO ESPECIAL, etc')
elif choice == "PALLET_DE_VIGA":
    st.subheader("ORÇAMENTO PARA PALLET DE VIGAS")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    ALTURA | COMPRIMENTO | LARGURA
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )
elif choice == "PALLET_PERSONALIZADO":
    st.image(image01, width=800, caption='Rótulo da Imagem 01') 
elif choice == "MENU"
 resp1 = st.text_input('insira seu email')
    st.write(resp1)
    resp2 = st.text_input('insira seu número de telefone')
    st.write(resp2)
    
