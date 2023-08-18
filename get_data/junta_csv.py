import os
import pandas as pd

# Caminho para a pasta com os arquivos CSV de entrada
input_folder = 'output_tables'

# Caminho para a pasta onde os arquivos CSV combinados serão salvos
output_folder = 'merged_tables'

# Cria a pasta de saída se ela não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lista para armazenar os DataFrames de cada arquivo CSV
dataframes = []

# Itera pelos arquivos CSV na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Combina todos os DataFrames em um único DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Conta quantos arquivos já existem na pasta merged_tables
existing_files = [f for f in os.listdir(output_folder) if f.startswith('merged_output')]
next_number = len(existing_files) + 1

# Nome do arquivo de saída com o número sequencial
output_filename = f"merged_output_{next_number}.csv"
output_file = os.path.join(output_folder, output_filename)

# Salva o DataFrame combinado em um arquivo CSV
combined_df.to_csv(output_file, index=False)

print("Arquivo combinado salvo em:", output_file)
