📊 Investment Decision Support Dashboard
Dashboard interaktif berbasis Streamlit untuk mendukung pengambilan keputusan investasi pada infrastruktur listrik.
Membantu manajer dan tim operasional mengidentifikasi prioritas investasi berdasarkan pola gangguan (faults), kondisi lingkungan, kesehatan komponen, dan downtime.

sumber data: https://www.kaggle.com/datasets/ziya07/power-system-faults-dataset?resource=download

dashboard: https://if5240-tim-5.streamlit.app/

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

Kolom:	Deskripsi
Fault ID:	ID unik gangguan
Fault Type:	Jenis gangguan (misal: Line Breakage, Transformer Failure)
Fault: Location (Latitude, Longitude)	Koordinat lokasi kejadian
Voltage (V):	Tegangan saat gangguan
Current (A):	Arus saat gangguan
Power Load (MW):	Beban daya
Temperature (°C):	Suhu lingkungan
Wind Speed (km/h):	Kecepatan angin
Weather Condition:	Kondisi cuaca
Maintenance Status:	Status perawatan
Component Health:	Kesehatan komponen
Duration of Fault (hrs):	Durasi fault
Down time (hrs):	Downtime total

Dengan bantuan OpenAI ChatGPT untuk dokumentasi & boilerplate.

