# Menyelesaikan Permasalahan Institusi Pendidikan
# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Sebagai institusi pendidikan, Jaya Jaya Institut ingin mengatasi permasalahan tingginya angka dropout di kalangan mahasiswa. Jaya jaya maju berencana  menggunakan dataset yang telah mereka kumpulkan mengenai performa mahasiswa untuk mengembangkan model machine learning prediktif, dan untuk mengembangkan dashboard yang dapat memudahkan mereka dalam memahami data dan memantau perkembangan akademik mahasiswa secara lebih efisien.

### Permasalahan Bisnis
1. Faktor apa saja yang sangat menentukan terhadap dropoutnya siswa?
2. Bagaimana caranya pihak institusi dapat dengan mudah memantau faktor faktor resiko tersebut melalui visualisasi?
3. Bagaimana cara memprediksi siswa yang berkemungkinan tidak akan lulus(dropout) berdasarkan faktor resiko yang didapatkan sebelumnya?
4. Bagaimana intitusi dapat dengan mudah mengimplementasikan prediksi siswa yang akan dropout?

### Cakupan Proyek
- Melakukan analisis terhadap data performa siswa. Mencari faktor yang paling menentukan terhadap status siswa(Dropout, Enrolled, Graduate)
- Membuat dashboard interaktif agar institusi dapat dengan mudah memantau faktor faktor yang membuat siswa dropout
- Membangun model prediktif berbasis machine learning untuk memprediksi kemungkinan dropout/graduated siswa
- Deployment ke streamlit cloud agar model prediksi dapat dengan mudah digunakan
- Memberikan rekomendasi yang efektif untuk membantu menurunkan angka dropout

  
### Persiapan

**Sumber data:** [student performance data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

**Setup environment:**
1. Prasyarat Tools
   - Google Colab: [Google Colab](https://colab.research.google.com/)
   - Google Looker Studio: [Looker](https://lookerstudio.google.com/u/0/navigation/reporting)
2. Clone Repository\
   Clone Repository 
   ```
   git clone [https://github.com/dk1781/studentdropoutpredictive]
   cd studentdropoutpredictive
   ```
3. Setup Google Colab
   ```
   Python 3.11.12
   ```
   Penggunaan Google Colab sudah menyediakan versi Python terbaru secara default, dan library yang akan digunakan sudah kompatibel, sehingga tidak perlu menginstall requirements.txt

   Akan tetapi jika diperlukan untuk penggunaan lokal install dependencies yang diperlukan
   ```
   !pip install -r requirements.txt
   ```

5. Setelah seluruh proses setup selesai, Anda bisa menjalankan skrip utama atau mulai melakukan proses prediksi.
   - Untuk menjalankan analisis utama terdapat pada
     ```
     notebook.ipynb
     ```
   - Untuk mencoba prediksi dapat memasukan data siswa dapat melalui cmd
     ```
     streamlit run app.py
     ```



## Business Dashboard
Bussines dashboard dirancang untuk membantu institusi memantau faktor faktor yang menyebabkan dropoutnya mahasiswa

Dashboard ini berisi :

1. Dropdown control untuk mengatur jika ingin memfilter grafik yang dimunculkan. Dropdown ini ada 2 yaitu status siswa dan application mode
2. Distribusi status siswa (Graduated, enrolled, Dropout)
3. Distribusi Gender atau jenis kelamin siswa berdasarkan statusnya
4. Treemap jumlah student perdepartement
5. Debtor atau status hutang siswa berdasarkan status kelulusannya
6. Rata rata grade siswa pada semester 1 dan 2
7. rata rata unit siswa yang disetujui pada semester 1 dan 2
8. Distribusi Pembayaran uang kuliah siswa berdasarkan status
9. Distribusi umur siswa saat pendaftaran berdasarkan status


Dashboard ini sangat dapat membantu pihak Jaya Jaya Institut dalam mengidentifikasi profil mahasiswa berisiko untuk dropout, agar bisa segera diberikan bimbingan lebih awal.
Link Dashboard: [Dashboard Jaya Institut](https://lookerstudio.google.com/reporting/a133f7e7-5004-441c-aff7-e83631532a49)

## Menjalankan Sistem Machine Learning
Untuk membantu institusi meprediksi kemungkina dropout siswa dibangunlah model machine learning, dan untuk mengoperasikan prototipe sistem machine learning yang telah dikembangkan,dapat dilakukan dengan cara  menjalankannya secara lokal atau memanfaatkan layanan Streamlit Cloud.
1. **Menjalankan Secara Lokal**
   - Pastikan seluruh dependensi yang dibutuhkan telah terpasang.
   - Buka terminal atau command prompt, lalu jalankan perintah berikut:
     ```
     streamlit run app.py
     ```
   - File aplikasi utama ditulis dalam berkas Python bernama `app.py.`
2. **Menjalankan Melaui Streamlit Cloud**
   - Sistem prototipe ini juga dapat diakses secara daring melalui tautan berikut:\
     [Student Dropou Prediction ](https://dk1781-studentdropoutpredictive-app-xo95mq.streamlit.app/)

## Conclusion
Diperoleh beberapa faktor yang paling mempengaruhi siswa dropout pada Jaya jaya institut yaitu :
- Faktor Akademis siswa : Siswa yang memiliki unit dan grade yang rendah pada semester 1 dan 2 cenderung dropout dari institusi
- Faktor Ekonomi : Siswa yang memiliki debt atau tunggakan memiliki kemungkina besar untuk dropout dari institusi
- Faktor Lainnya : Yaitu application mode jenis kelamin dan usia siswa. Meskipun faktor ini tidak berpengaruh besar akan tetapi jika digabungkan dengan faktor lainnya akan memudahkan untuk memprediksi status siswa. dilihat siswa laki laki cenderung memiliki potensi untuk dropout lebih besar, begitu pula siswa dengan usia yang lebih muda samapi menengah memiliki kemungkinan untuk dropout lebih besar juga.

Model prediksi berbasis machine learnig yang dibangun dapat dengan akurat memprediksi kemungkinan dropout siswa dengan memasukan data data yang diperlukan, selain itu model telah dideploy ke streamlit cloud agar dapat dengan mudah digunakan. Disamping model prediktif terdapat juga dashboard yang dapat memudahkan intitusi untuk memantau faktor dropout siswa. Kedua hal ini dapat membantu pihak institusi untuk melakuakan langkah preventif yang dapat menurunkan kemungkinan dropout siswa.

### Rekomendasi Action Items
1. Melakukan bimbingan tambahan terhadap mahasiswa yang kurang dalam akademis. Hal ini bisa dilakukan dengan merekomendasikan siswa untuk melkukan tutor sebaya atau jika diperlukan memberikan kelas tambahan
2. Melakukan pendekatan baru untuk siswa dengan permasalahan ekonomi seperti memberi program beasiswa untuk siswa yang berprestasi ataupun memberikan kemudahan pembayaran melalui cicilan atau menurunkan uang pembayarannya dengan timbal balik siswa tersebut ikut membantu di institusi seperti menjadi asisten atau hal lainnya
3. Melakukan pembinaan terhadap siswa dengan umur muda hingga menengah untuk memberikan motivasi lebih dan memberikan rekomendasi arahan untuk mengurangi dropout rate
4. Monitor selalu performa siswa melalui dashboard dan lakukan prediksi pada siswa yang dirasa kurang dalam beberapa faktor yang sebelumnya disebutkan menggunakan model prediktif yang telah dibuat agar dapat melihat kemungkinan dropout atau lulusnya siswa tersebut dan dapat membuat langkah preventif jika siswa tersebut berkemungkinan drropou.
