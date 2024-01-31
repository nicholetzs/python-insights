# Python Insights is about gain an intuitive, accurate, and deep understanding of a dataset and what they can predict 📊

In the archive.py file, you can use it as a normal file in your code editor. Below, I'll give you the code to use in the Jupyter Notebook:

# Step 1: Import the dataset
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")

# Step 2: Visualize the dataset (look at it) and correct the formatted dataset
# Useless columns -> for example, the customer ID, as we won't use it to determine the cancellation reason
tabela = tabela.drop(columns="CustomerID") # Drop the "CustomerID" column.
display(tabela)  

# Step 3: Correct the dataset
display(tabela.info())

# Empty values -> remove rows with empty values
tabela = tabela.dropna()  # Drop rows with empty values (automatically)
print(tabela.info())

# Step 4: Initial analysis of cancellations
# How many people canceled and how many did not
display(tabela["cancelou"].value_counts())
# Percentage
display(tabela["cancelou"].value_counts(normalize="True")) #normalizar é um procedimento estatístico, botar na base de 0 a 1, calcular o percentual proporção é porcentagem

# Step 5: Analysis of cancellation reasons
#!pip install 
import plotly.express as px
# Create 
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
     # Display the plot
    grafico.show()
