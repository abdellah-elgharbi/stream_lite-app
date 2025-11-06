import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Analyse simple de données CSV")

# Upload du fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    # Lire le fichier CSV
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(df.head())
    # Choisir une colonne pour visualisation
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_cols:
        col_to_plot = st.selectbox("Choisissez une colonne à visualiser", numeric_cols)

        # Histogramme
        st.write(f"Histogramme de {col_to_plot}")
        fig, ax = plt.subplots()
        ax.hist(df[col_to_plot], bins=20, color='skyblue', edgecolor='black')
        st.pyplot(fig)
    else:
        st.warning("Aucune colonne numérique trouvée pour la visualisation.")
