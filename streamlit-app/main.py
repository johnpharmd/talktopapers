from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from Bio import Entrez
import streamlit as st
import pandas as pd
import smtplib
import os

# Set up Entrez access
email = os.getenv("EMAIL")
Entrez.email = email


def fetch_pubmed_data(keywords):
    search_handle = Entrez.esearch(db='pubmed', term=keywords, retmax=50)
    search_results = Entrez.read(search_handle)
    id_list = search_results['IdList']
    summary_handle = Entrez.esummary(db='pubmed', id=','.join(id_list))
    summary_results = Entrez.read(summary_handle)
    
    return pd.DataFrame(summary_results)


if __name__ == '__main__':

    # Set up Streamlit app
    st.title("PubMed Search")
    query = st.text_input("Enter search terms:")
    if st.button("Search"):
        # Retrieve article data from PubMed and display in dataframe
        articles = fetch_pubmed_data(query)
        results_df = pd.DataFrame(articles) #, columns=["article"])
        st.write(results_df)