<h2>📌 ETL - Pipeline Python Sederhana</h2>

<p>
Project ini saya buat sebagai implementasi dan Cap Stone Project mempelajari <strong>Python</strong>, 
saya membangun sebuah sistem <strong>ETL</strong> sederhana namun fungsional menggunakan <strong>Python</strong>.  
Proyek ini dibuat untuk memberikan gambaran menyeluruh (end-to-end) mengenai proses pengolahan data
mulai dari <strong>mengambil data mentah</strong>, <strong>mentransformasinya</strong> sesuai kebutuhan, 
hingga <strong>menyimpan hasil akhir</strong> dalam format yang siap digunakan untuk analisis dan pengambilan keputusan.
</p>

<hr>

<h2>🛠 Deskripsi Project</h2>

<p>Project ini merupakan hasil implementasi pembelajaran <strong>Data Engineering dengan Python</strong>, yang dirancang untuk:</p>
<ul>
  <li>Membaca dan memproses data dari berbagai sumber seperti <strong>CSV &amp; JSON</strong></li>
  <li>Melakukan <strong>transformasi data</strong> sesuai kebutuhan bisnis atau analisis</li>
  <li>Menyimpan hasil akhir ke <strong>CSV</strong> yang siap digunakan untuk analisis lebih lanjut</li>
</ul>

<p>Selain itu, sistem ini dilengkapi dengan:</p>
<ul>
  <li>📩 <strong>Email Alerts</strong> → Notifikasi otomatis ketika proses ETL mengalami kegagalan</li>
  <li>📊 <strong>Monitoring Log</strong> → Pencatatan detail setiap eksekusi ETL (status, durasi, jumlah data, dan error)</li>
  <li>📨 <strong>Daily Summary Report</strong> → Ringkasan performa ETL harian yang dikirim via email</li>
</ul>

<hr>

<h2>⚡ Fitur Utama</h2>
<p>Fitur-fitur berikut dirancang untuk memastikan proses ETL berjalan efisien, terukur, dan mudah dipantau:</p>
<ul>
  <li><strong>Extract</strong> → Baca data dari CSV &amp; JSON</li>
  <li><strong>Transform</strong> → Bersihkan &amp; gabungkan dataset</li>
  <li><strong>Load</strong> → Simpan hasil akhir ke CSV</li>
  <li><strong>Email Alert</strong> → Notifikasi error dengan format HTML</li>
  <li><strong>Monitoring Log</strong> → CSV berisi histori run ETL</li>
  <li><strong>Daily Report</strong> → Ringkasan jumlah run, sukses/gagal, rata-rata durasi, dan total rows</li>
</ul>

<hr>

<h2>📐 Arsitektur Data</h2>

<p align="center">
  <img src="assets/ETL_ARCITECTURE.png" alt="ETL Architecture Diagram" width="800">
</p>

<hr>

<h2>📊 Output Project</h2>

<h3>1️⃣ <strong>Hasil ETL</strong></h3>
<ul>
  <li>File CSV hasil transformasi tersimpan di folder <code>warehouse/</code></li>
  <li>Format CSV disesuaikan dengan kebutuhan analisis, sudah melalui proses pembersihan &amp; transformasi</li>
</ul>

<hr>

<h3>2️⃣ <strong>Monitoring Log (<code>etl_runs.csv</code>)</strong></h3>
<p>Mencatat setiap eksekusi ETL:</p>

<table>
  <thead>
    <tr>
      <th>time</th>
      <th>status</th>
      <th>stage</th>
      <th>source_rows</th>
      <th>transformed_rows</th>
      <th>loaded_rows</th>
      <th>error_message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-08-16 15:10</td>
      <td>SUCCESS</td>
      <td>Load</td>
      <td>1000</td>
      <td>980</td>
      <td>980</td>
      <td></td>
    </tr>
    <tr>
      <td>2025-08-16 14:55</td>
      <td>FAILED</td>
      <td>Transform</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
      <td>Traceback...</td>
    </tr>
  </tbody>
</table>

<hr>

<h3>3️⃣ <strong>Email Alert</strong></h3>
<p>Notifikasi error langsung ke email:</p>

<pre><code><strong>🚨 ALERT [WARNING] 🚨</strong>

<strong>Job:</strong> ETL_Sederhana_Project
<strong>Stage:</strong> Load
<strong>Time:</strong> 2025-08-16 21:32:30

<strong>Error Message:</strong>
Traceback (most recent call last):
  File "c:\Users\personal\Desktop\ETL-pipeline-sederhana\main.py", line 35, in save_to_csv
    save_to_csv(final_df, OUTPUT_PATH)
  File "c:\Users\personal\Desktop\ETL-pipeline-sederhana\scripts\load.py", line 2, in save_to_csv
    return df.to_csv(path, index=False)
NameError: name 'path' is not defined

<em>Note: Segera periksa log ETL untuk investigasi.</em>
</code></pre>

<hr>

<h3>4️⃣ <strong>Daily Summary Email</strong></h3>
<p><strong>Laporan ringkas setiap hari :</strong></p>
<pre><code><strong>ETL Daily Report —</strong> 2025-08-16
<strong>Total runs :</strong> 5 (4 sukses | 1 gagal)
<strong>Avg duration :</strong> 2.35s
<strong>Total loaded rows :</strong> 4,900
</code></pre>

<hr>

<h2>🛠 Tech Stack</h2>
<p>
<img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python Badge">
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas" alt="Pandas Badge">
<img src="https://img.shields.io/badge/CSV%20%26%20JSON-Data%20Files-orange" alt="CSV JSON Badge">
<img src="https://img.shields.io/badge/SMTP-Gmail-red?logo=gmail" alt="SMTP Badge">
<img src="https://img.shields.io/badge/dotenv-Config%20Manager-lightgrey" alt="dotenv Badge">
</p>

<hr>

<h2>✍️ Tentang Project</h2>
<p>
<p>
Project ini dibuat sebagai implementasi dan capstone <strong>Alfian</strong> sebagai bagian dari perjalanan belajar di bidang <strong>Data Engineering</strong>. Melalui proyek ini, saya berharap dapat menginspirasi rekan-rekan pembelajar lain untuk terus berlatih dan mengembangkan kemampuan teknis di dunia data. Jika Anda menemukan kesalahan, bug, atau memiliki ide pengembangan (improvement), silahkan untuk Contact saya. 
</p>

<p><em>"The biggest risk is not taking any risk." – Mark Zuckerberg</em></p>
<p><em>(Risiko terbesar adalah tidak mengambil risiko sama sekali.)</em></p>

<p>📩 <strong>Contact:</strong> 
<a href="mailto:alfianfebiyanto7@gmail.com">alfianfebiyanto7@gmail.com</a> | 
<a href="https://www.linkedin.com/in/alfianfebiyanto/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
</p>
