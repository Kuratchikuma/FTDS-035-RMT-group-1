import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


def app():
    # title
    st.title('Exploratory Data Analysis (EDA) dari Dataset')
    st.write('##### Dibawah ini merupakan Exploratory Data Analysis (EDA) yang telah dilakukan untuk memahami bagaimana isi dataset secara general.')

    st.markdown('----')

    # show dataframe
    st.write('#### Dataset yang Digunakan')
    df = pd.read_csv('Dataset_fix.csv')
    st.dataframe(df)

    st.markdown('----')

    st.write('#### Wordcloud Kolom Cuisine')
    st.image('cuisine_cloud.png', caption='Wordcloud Kolom Cuisine')
    st.write('''
    - Terlihat kafe sudah menjadi hal yang paling sering muncul pada word cloud. Meskipun terlihat pada wordcloud masih muncul kata yang kemungkinan tidak menunjukkan kafe. Misalkan secara harfiah toko kue dan kafe itu berbeda. Namun data yang kita dapat sudah kita filter menjadi kafe pada dataset sumber.
    ''')
    
    st.markdown('----')

    st.write('#### Wordcloud Opening Hours')
    st.image('opening_hours.png', caption='Wordcloud Kolom Opening Hours')
    st.write('''
    - Rata-rata kafe buka di semua hari. Terlihat kata senin sampai minggu itu masuk kategori kata yang berukuran besar.
    ''')

    st.markdown('----')

    st.write('#### Statistik Price From dan Price Till')
    price_stats = df.groupby('kota')[['price_from', 'price_till']].describe().T
    st.dataframe(price_stats)
    st.image('price_from.png', caption='Boxplot Harga Mulai')
    st.image('price_till.png', caption='Boxplot Harga Maksimal')
    st.write('''
    - Kafe-kafe di Jakarta menunjukkan harga rata-rata price_from sebesar Rp43.233 dan price_till sebesar Rp105.466. Median untuk price_from dan price_till masing-masing adalah Rp50.000 dan Rp100.000. Ini berarti sebagian besar kafe memulai harga di sekitar Rp50.000, dengan harga tertinggi yang biasa ditemukan di sekitar Rp100.000. Harga rata-rata menunjukkan bahwa meskipun ada variasi, sebagian besar kafe cenderung menjaga harga dalam rentang yang cukup terjangkau.
    ''')
    
    st.markdown('----')

    st.write('#### Distribusi Rating Tiap Tempat')
    st.image('rating.png', caption='Distribusi Rating Tiap Tempat')
    st.write('''
    - Sebagian besar cafe di Jakarta memiliki rating antara 4.0 hingga 4.5, menunjukkan bahwa cafe umumnya mendapatkan penilaian yang baik.
    ''')

    st.markdown('----')

    st.write('#### Count Tiap Tipe Cuisine yang Ada Didalam Dataset')
    cuisine_distribution = df['cuisine'].value_counts().reset_index()
    cuisine_distribution.columns = ['Cuisine Type', 'Count']
    st.dataframe(cuisine_distribution)
    st.write('''
    - Dominasi Kafe:

    Kafe merupakan jenis tempat makan yang sangat dominan di Jakarta, dengan total 1.329 entri. Jumlah ini sangat jauh di atas jenis cuisine lain. Hal ini bisa mengindikasikan bahwa tren nongkrong atau bersosialisasi di kafe sangat kuat di Jakarta. Kafe di Jakarta bisa saja beragam, dari yang menawarkan kopi hingga makanan ringan, yang menargetkan pasar muda dan profesional.

    - Keanekaragaman Jenis Cuisine:

    Meskipun kafe mendominasi, Jakarta tetap menawarkan keragaman cuisine, dengan jenis seperti Toko Roti (35), China (20), Jepang (15), dan Italia (12). Ini menunjukkan bahwa ada variasi pilihan makanan, meskipun jumlahnya tidak sebanyak kafe. Ini juga bisa menunjukkan bahwa restoran-restoran spesifik seperti ini lebih fokus pada niche pasar tertentu.

    - Restoran Internasional di Jakarta:

    Kehadiran cuisine Jepang, Italia, India, dan China menggambarkan preferensi masyarakat urban Jakarta yang mulai mengadopsi dan menggemari makanan internasional. Restoran jenis ini mungkin berada di area dengan target pelanggan kelas menengah ke atas atau berada di pusat perbelanjaan.
    ''')

    st.markdown('----')

    st.write('#### Distribusi Kategori Harga')
    st.image('price_cat.png', caption='Distribusi Kategori Harga')
    st.write('''
    - Low Category (Rp0 - Rp25.000): Hanya sedikit cafe yang menawarkan harga di bawah Rp25.000. Ini menunjukkan bahwa cafe di Jakarta umumnya menetapkan harga yang cukup tinggi untuk layanan mereka.
    - Medium Category (Rp25.000 - Rp100.000): Mayoritas cafe di Jakarta berada dalam rentang harga ini, yang mencerminkan tren harga yang terjangkau namun tidak terlalu murah.
    - High Category (Rp100.000 - Rp400.000): Ada sejumlah cafe yang menetapkan harga minimum di atas Rp100.000, yang menunjukkan segmen pasar yang lebih premium.
    ''')

    st.markdown('----')

    
if __name__ == '__main__':
    app()
    