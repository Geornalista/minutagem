import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
import unidecode

import plotly.graph_objs as go

st.set_page_config(
  page_title='Minutagem de Gols',
  page_icon='⚽',
  layout="wide")

with open('style.css') as f:
	st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

ligas = ['Argentina','Austrália','Áustria','Bélgica','Brasil','Bulgária','China','Croácia',
         'Dinamarca','Inglaterra','França','Alemanha','Grécia','Itália','Japão','Holanda',
         'Noruega','Polônia','Portugal','Romênia','Rússia','Escócia','Coréia do Sul','Espanha',
         'Suécia','Suíça','Turquia','EUA','Uruguai','Sérvia']

with st.container():
  liga = st.selectbox('Escolha a liga',ligas)
  liga = unidecode.unidecode(liga.lower())

tab1,tab2 = st.tabs([
  "📊 Gols Marcados",
  "🥅 Gols Sofridos"])
        
d = {
  'argentina': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Argentina%20Primera%20Divisi%C3%B3n_2022.xlsx?raw=true',
  'australia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Australia%20A-League_20222023.xlsx?raw=true',
  'austria': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Austria%20Bundesliga_20222023.xlsx?raw=true',
  'belgica': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Belgium%20Pro%20League_20222023.xlsx?raw=true',
  'brasil': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Brazil%20Serie%20A_2022.xlsx?raw=true',
  'bulgaria': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Bulgaria%20First%20League_20222023.xlsx?raw=true',
  'china': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/China%20Chinese%20Super%20League_2022.xlsx?raw=true',
  'croacia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Croatia%20Prva%20HNL_20222023.xlsx?raw=true',
  'dinamarca': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Denmark%20Superliga_20222023.xlsx?raw=true',
  'inglaterra': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/England%20Premier%20League_20222023.xlsx?raw=true',
  'franca': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/France%20Ligue%201_20222023.xlsx?raw=true',
  'alemanha': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Germany%20Bundesliga_20222023.xlsx?raw=true',
  'grecia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Greece%20Super%20League_20222023.xlsx?raw=true',
  'italia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Italy%20Serie%20A_20222023.xlsx?raw=true',
  'japao': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Japan%20J1%20League_2022.xlsx?raw=true',
  'holanda': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Netherlands%20Eredivisie_20222023.xlsx?raw=true',
  'noruega': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Norway%20Eliteserien_2022.xlsx?raw=true',
  'polonia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Poland%20Ekstraklasa_20222023.xlsx?raw=true',
  'portugal': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Portugal%20Liga%20NOS_20222023.xlsx?raw=true',
  'romenia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Romania%20Liga%20I_20222023.xlsx?raw=true',
  'russia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Russia%20Russian%20Premier%20League_20222023.xlsx?raw=true',
  'escocia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Scotland%20Premiership_20222023.xlsx?raw=true',
  'coreia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/South%20Korea%20K%20League%201_2022.xlsx?raw=true',
  'espanha': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Spain%20La%20Liga_20222023.xlsx?raw=true',
  'suecia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Sweden%20Allsvenskan_2022.xlsx?raw=true',
  'suica': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Switzerland%20Challenge%20League_20222023.xlsx?raw=true',
  'turquia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Turkey%20S%C3%BCper%20Lig_20222023.xlsx?raw=true',
  'eua': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/USA%20MLS_2022.xlsx?raw=true',
  'uruguai': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Uruguay%20Primera%20Divisi%C3%B3n_2022.xlsx?raw=true',
  'servia': 'https://github.com/futpythontrader/YouTube/blob/main/Bases_de_Dados_(2022-2023)/Serbia%20SuperLiga_20222023.xlsx?raw=true'
}

link = d[liga]
df = pd.read_excel(link)
df = df[['Home','Away','FT_Goals_H', 'FT_Goals_A', 'Goals_H_Minutes', 'Goals_A_Minutes']]
clubes = list(df.Home.unique())
clubes.sort()

def figuras(clube,HGM,AGM,HGS,AGS):
  with tab1:

    fig1 = go.Figure()
    fig1.add_trace(go.Histogram(x=HGM, xbins=dict(start=0, size=10, end=90.1),
                      name='Mandante',orientation='v',marker_color='rgba(205,79,57,1)'))
    fig1.add_trace(go.Histogram(x=AGM, xbins=dict(start=0, size=10, end=90.1),
                      name='Visitante',orientation='v',marker_color='rgba(39,139,0,1)'))
    fig1.update_layout(
      title_text=clube+" - Minutagem dos Gols Marcados",
      barmode='group',
      autosize=False,
      xaxis_title="MINUTOS",
      yaxis_title="GOLS",
      bargap=0.2,
      width=1200,
      height=500,
      margin=dict(
          l=50,
          r=50,
          b=50,
          t=50,
          pad=0.1
      ),

      xaxis = dict(
            tickmode = 'linear',
            tick0 = 00,
            dtick = 10
      ),
      
      yaxis=dict(
          tickmode = 'linear',
          tick0 = 0,
          dtick = 1,
          showgrid=True,
          showline=True,
          showticklabels=True,
          zeroline=True,
      ),
      paper_bgcolor="lightgray",
      plot_bgcolor="silver",
      )
    
    st.plotly_chart(fig1, use_container_width=True)

  with tab2:
    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(x=HGS, xbins=dict(start=0, size=10, end=90.1),
                      name='Mandante',orientation='v',marker_color='rgba(205,79,57,1)'))
    fig2.add_trace(go.Histogram(x=AGS, xbins=dict(start=0, size=10, end=90.1),
                      name='Visitante',orientation='v',marker_color='rgba(39,139,0,1)'))
    fig2.update_layout(
      title_text=clube+" - Minutagem dos Gols Sofridos",
      barmode='group',
      autosize=False,
      xaxis_title="MINUTOS",
      yaxis_title="GOLS",
      bargap=0.2,
      width=1200,
      height=500,
      margin=dict(
          l=50,
          r=50,
          b=50,
          t=50,
          pad=0.1
      ),

      xaxis = dict(
            tickmode = 'linear',
            tick0 = 00,
            dtick = 10
      ),
      
      yaxis=dict(
          tickmode = 'linear',
          tick0 = 0,
          dtick = 1,
          showgrid=True,
          showline=True,
          showticklabels=True,
          zeroline=True,
      ),
      paper_bgcolor="lightgray",
      plot_bgcolor="silver",
      )
    st.plotly_chart(fig2, use_container_width=True)

for clube in clubes:
  lista_Hgm = []
  lista_Hgs = []
  lista_Agm = []
  lista_Ags = []

  casa = 'Home == "'+clube+'"'
  fora = 'Away == "'+clube+'"'
  df_casa = df.query(casa)
  df_fora = df.query(fora)

  for index, row in df_casa.iterrows():
    gh = row['FT_Goals_H']
    ga = row['FT_Goals_A']

    min_H = row['Goals_H_Minutes']
    min_A = row['Goals_A_Minutes']

    min_H = min_H.replace('[','')
    min_H = min_H.replace(']','')
    min_H = min_H.split(',')

    min_A = min_A.replace('[','')
    min_A = min_A.replace(']','')
    min_A = min_A.split(',')    
    
    for item in min_H:
      if item:
        if item.find('+') == -1:
            lista_Hgm.append(int(item.strip()[1:-1]))
        else:
          xx = item.strip().split('+')
          if (int(xx[0].strip()[1:]) + int(xx[1].strip()[:-1])) > 90:
            lista_Hgm.append(90)
          else:
            lista_Hgm.append(int(xx[0].strip()[1:]) + int(xx[1].strip()[:-1]))
      #else:
      #  lista_Hgm.append(0)

    for item in min_A:
      if item:
        if item.find('+') == -1:
            lista_Hgs.append(int(item.strip()[1:-1]))
        else:
          xx = item.strip().split('+')
          if (int(xx[0].strip()[1:]) + int(xx[1].strip()[:-1])) > 90:
            lista_Hgs.append(90)
          else:
            lista_Hgs.append(int(xx[0].strip()[1:]) + int(xx[1].strip()[:-1]))
      #else:
      #  lista_Hgs.append(0)

  for index, row in df_fora.iterrows():
    gh = row['FT_Goals_H']
    ga = row['FT_Goals_A']

    min_H = row['Goals_H_Minutes']
    min_A = row['Goals_A_Minutes']

    min_H = min_H.replace('[','')
    min_H = min_H.replace(']','')
    min_H = min_H.split(',')

    min_A = min_A.replace('[','')
    min_A = min_A.replace(']','')
    min_A = min_A.split(',')

    for item in min_A:
      if item:
        if item.find('+') == -1:
            lista_Agm.append(int(item.strip()[1:-1]))
        else:
          xx = item.strip().split('+')
          lista_Agm.append(int(xx[0].strip()[1:]) + int(xx[1].strip()[:-1]))
      #else:
      #  lista_Agm.append(0)

    for item in min_H:
      if item:
        if item.find('+') == -1:
            lista_Ags.append(int(item.strip()[1:-1]))
        else:
          xx = item.strip().split('+')
          lista_Ags.append(int(xx[0].strip()[1:]) + int(xx[1].strip()[:-1]))
      #else:
      #  lista_Ags.append(0)
  
  figuras(clube,lista_Hgm,lista_Agm,lista_Hgs,lista_Ags)