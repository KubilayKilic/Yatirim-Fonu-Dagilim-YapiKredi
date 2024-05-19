import os
import PyPDF2

# PDF dosyalarının bulunduğu klasör yolu
pdf_folder = r'C:\Users\khubi\Desktop\Pyton_PDF\Yapı Kredi FON'

# Klasördeki tüm PDF dosyalarını listele
pdf_files = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

# Her bir PDF dosyası için işlemleri yap
for pdf_file_path in pdf_files:
    print(f"------------------------------")
    print(f"{os.path.basename(pdf_file_path)} Dağılımı")
    print(f"------------------------------")

    # PDF dosyasını aç
    with open(pdf_file_path, 'rb') as pdf_file:
        # PdfReader nesnesini oluştur
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Tüm sayfaları dolaşarak metni birleştir
        full_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            full_text += page_text + "\n\n"  # Sayfa sonlarına iki yeni satır ekleyerek ayırabilirsiniz

        # Başlangıç ve bitiş işaretçilerini belirle
        start_phrase = "III- FON PORTFÖY DEĞERİ"
        end_phrase = "IV- FON TOPLAM DEĞERİ"

        # Başlangıç işaretçisini bul
        start_index = full_text.find(start_phrase)
        if start_index == -1:
            print(f"'{start_phrase}' bulunamadı.")
        else:
            # Bitiş işaretçisini bul
            end_index = full_text.find(end_phrase, start_index)
            if end_index == -1:
                print(f"'{end_phrase}' bulunamadı.")
            else:
                # Başlangıç ve bitiş işaretçileri arasındaki kısmı al
                text = full_text[start_index:end_index + len(end_phrase)]

                # Her bir satırı işleyerek yüzdelik değeri ve hisse kodunu bulalım
                lines = text.strip().split('\n')  # Metni satırlara bölelim, baştaki ve sondaki boşlukları temizleyelim

                toplam_yuzde = 0.0  # Toplam yüzdelik değerler için başlangıç değeri

                for line in lines:
                    # Satırı boşluklarla bölelim
                    parts = line.split()

                    # Eğer satırda en az 6 parça varsa, yüzdelik değeri ve hisse kodunu alalım
                    if len(parts) >= 6:
                        yüzde = parts[-3]  # Yüzdelik değer
                        hisse_kod = parts[-1]   # En sondaki hisse kodu
                        hisse_check = parts[-2]

                        # Hisse kodunun başındaki "TRA-TRE" kontrolü
                        if hisse_check.startswith("TRA") or hisse_check.startswith("TRE") or hisse_check.startswith("US") or hisse_check.startswith("KY") or hisse_check.startswith("FR") or hisse_check.startswith("NL") or hisse_check.startswith("GB") or hisse_check.startswith("IE"):
                            # Yüzdelik değeri float'a çevirip toplam değere ekle
                            try:
                                yuzde_float = float(yüzde.replace(',', '.'))  # Virgülle ayrılmışsa noktaya çevir
                                toplam_yuzde += yuzde_float
                                # Sonuçları yan yana yazdıralım
                                print(f"Hisse {hisse_kod} Yüzde: {yüzde}")
                            except ValueError:
                                print(f"Geçersiz yüzdelik değer: {yüzde}")
                    else:
                        pass

                # Toplam yüzde değerini formatlayarak yazdır
                print(f"Toplam Yüzde: {toplam_yuzde:.2f}")
