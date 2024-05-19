Açıklama:
Bu Python betiği, belirli bir klasörde bulunan PDF formatındaki yatırım fonu raporlarını analiz etmek için tasarlanmıştır. Her bir PDF dosyası için belirli başlangıç ve bitiş işaretçileri arasındaki metni (örneğin, "FON PORTFÖY DEĞERİ" ve "FON TOPLAM DEĞERİ" arasındaki bölümler) çıkarır ve bu bölümlerdeki hisse senedi dağılımını inceleyerek belirli koşullara uyan hisse senetlerini filtreler.

Kullanım:

Python betiği, belirli bir klasördeki tüm PDF dosyalarını işler.
Her PDF dosyası için belirli metin parçaları aranır ve bu parçalar arasındaki hisse senedi dağılımı çıkarılır.
Belirli koşullara uyan hisse senetleri (örneğin, belirli ülke kodlarına sahip olanlar) ve bunların yüzdelik değerleri hesaplanır.
Sonuçlar, konsola yazdırılır ve toplam yüzde değeri formatlanarak gösterilir.
Kurulum:

Bu projeyi çalıştırmak için Python 3.x ve PyPDF2 kütüphanesinin yüklü olması gerekmektedir.
PyPDF2 kütüphanesi için gereksinimleri yüklemek için pip install PyPDF2 komutunu kullanabilirsiniz.
Örnek Çıktı:

------------------------------
Yapı Kredi FON Dağılımı
------------------------------
Hisse TRA123 Yüzde: 10.50
Hisse KY456 Yüzde: 7.80
Toplam Yüzde: 18.30
Notlar:

Bu betik, belirli PDF dosyalarında belirli metin örüntülerini aramak ve bu örüntüler arasındaki hisse senedi dağılımını analiz etmek için kullanılmaktadır.
Eğer PDF dosyaları farklı formatlarda ise veya beklenmeyen sonuçlar alınıyorsa, betikte değişiklikler yapılması gerekebilir.

Bu README dosyasını README.md olarak projenizin ana dizinine kaydedebilir ve GitHub'a yükleyebilirsiniz. Bu şekilde, projenizi ziyaret edenler nasıl kullanacaklarını ve ne bekleyeceklerini anlayabilirler.
