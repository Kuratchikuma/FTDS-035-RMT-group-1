import pandas as pd
import psycopg2 as db
import datetime as dt
from datetime import timedelta
from io import StringIO
from pytz import timezone
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import os


folderinput = '/opt/airflow/data'
folderoutput = '/opt/airflow/data/clean_data'

# membuat data yang akan dipakai 

def extract_data():
    # List kosong untuk menyimpan nama file
    directory_path = folderinput
    file_list = []
    
    # Mengecek apakah direktori valid
    if not os.path.isdir(directory_path):
        print(f"{directory_path} is not a valid directory.")
        return file_list
    
    # Loop untuk membaca semua file dalam direktori
    for filename in os.listdir(directory_path):
        # Menggabungkan path direktori dengan nama file
        file_path = os.path.join(directory_path, filename)
        
        # Mengecek apakah ini adalah file (bukan folder)
        if os.path.isfile(file_path):
            # Menambahkan file ke dalam list
            file_list.append(filename)
    
    # Mengembalikan list nama file
    return file_list

def transform():
    # Mengambil file dari extract_data
    file_list = extract_data()

    # Jika tidak ada file yang ditemukan, keluar dari fungsi
    if not file_list:
        print("No files found in the input directory.")
        return

    # Loop melalui setiap file dalam file_list
    for filename in file_list:
        input_path = os.path.join(folderinput, filename)
        output_path = os.path.join(folderoutput, filename)

        # Membaca file CSV
        try:
            df = pd.read_csv(input_path)

            # Menyimpan hasil transformasi ke folder output
            df.to_csv(output_path, index=False)
            print(f"Data dari {filename} berhasil ditransformasi dan disimpan di {output_path}")

        except Exception as e:
            print(f"Error processing file {filename}: {e}")
 
    
def load_data(): 
    return






#################_______________________DAG_____________________________________#########

# Pengaturan DAG
default_args = {
    'owner': 'ali_asan_fahri_harun_ihsan',
    'start_date': dt.datetime(2024, 10, 11, tzinfo=timezone('Asia/Jakarta')),
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
    }

with DAG('test_dag',
         default_args=default_args,
         schedule_interval='30 6 * * *',
         catchup=False
         ) as dag:

    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "I am reading the CSV now....."')
    
    extract_the_data = PythonOperator(task_id = 'get', 
                                      python_callable = extract_data, 
                                      dag = dag)
    
    transform_the_data = PythonOperator(task_id = 'clean', 
                                      python_callable = transform, 
                                      dag = dag)
    
    load_the_data = PythonOperator(task_id = 'load', 
                                      python_callable = load_data, 
                                      dag = dag)



print_starting >> extract_the_data >> transform_the_data >> load_the_data
