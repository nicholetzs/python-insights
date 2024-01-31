# Python Insights is about gain an intuitive, accurate, and deep understanding of a dataset and what they can predict 📊
# Python Insights - Analyzing Data with Python 📶
# Case - Customer Cancellation 𐙚

Scenario: You were hired by a company with more than 800,000 clients for a Data project. Recently, the company realized that of its total customer base, the majority are inactive customers, that is, those who have already canceled the service.
Needing to improve her results, she wants to be able to understand the main reasons for these cancellations and what are the most efficient actions to reduce this number.

In the archive.py file, you can use it as a normal file in your code editor. I don't usually csv the database because of the size, but you can use your own database in a variety of ways and modify the code as needed. 

---> Below, I'll give you the code to use in the Jupyter Notebook:

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

    # Finally, I recommend installing the Jupyter extension in VSCODE and using the code provided to better visualize the data and charts, which I haven't put here ദ്ദി ˉ͈̀꒳ˉ͈́ )✧
