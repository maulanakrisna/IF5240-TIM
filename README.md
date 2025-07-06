📊 Investment Decision Support Dashboard
Dashboard interaktif berbasis Streamlit untuk mendukung pengambilan keputusan investasi pada infrastruktur listrik.
Membantu manajer dan tim operasional mengidentifikasi prioritas investasi berdasarkan pola gangguan (faults), kondisi lingkungan, kesehatan komponen, dan downtime.

🚀 Fitur Utama
✅ Ringkasan KPI:

Jumlah gangguan terdeteksi.

Rata-rata downtime.

Total power load.

✅ Filter interaktif:

Jenis gangguan (Fault Type).

Kondisi cuaca.

Kesehatan komponen.

✅ Visualisasi:

Peta lokasi gangguan.

Bar chart rata-rata downtime per jenis gangguan.

Boxplot downtime berdasarkan cuaca.

✅ Tabel data detail.

📂 Data Input
Format data yang digunakan berbentuk tabular dengan kolom sebagai berikut:

Kolom	Deskripsi
Fault ID	ID unik gangguan
Fault Type	Jenis gangguan (misal: Line Breakage, Transformer Failure)
Fault Location (Latitude, Longitude)	Koordinat lokasi kejadian
Voltage (V)	Tegangan saat gangguan
Current (A)	Arus saat gangguan
Power Load (MW)	Beban daya
Temperature (°C)	Suhu lingkungan
Wind Speed (km/h)	Kecepatan angin
Weather Condition	Kondisi cuaca
Maintenance Status	Status perawatan
Component Health	Kesehatan komponen
Duration of Fault (hrs)	Durasi fault
Down time (hrs)	Downtime total

🖥️ Cara Menjalankan
1️⃣ Clone repositori ini
bash
Salin
Edit
git clone <repo-url>
cd investment-dashboard
2️⃣ Install dependensi
Pastikan Anda memiliki Python >= 3.8
Jalankan:

bash
Salin
Edit
pip install -r requirements.txt
requirements.txt:

nginx
Salin
Edit
streamlit
pandas
plotly
3️⃣ Jalankan dashboard
bash
Salin
Edit
streamlit run app.py
Akses dashboard di browser di alamat yang diberikan (biasanya http://localhost:8501)

📈 Screenshot
Halaman Utama	Peta Lokasi

📄 Struktur File
bash
Salin
Edit
investment-dashboard/
│
├── app.py                # Script utama Streamlit
├── requirements.txt      # Dependensi Python
├── README.md             # Dokumentasi ini
├── docs/
│   └── main_kpi.png      # Contoh screenshot
└── data/
    └── faults.csv        # Dataset (opsional)
📝 Lisensi
MIT License — silakan gunakan, modifikasi, dan distribusikan dengan atribusi.

👨‍💼 Author
Adhitya — Manager IT, Data Science.
Dengan bantuan OpenAI ChatGPT untuk dokumentasi & boilerplate.

