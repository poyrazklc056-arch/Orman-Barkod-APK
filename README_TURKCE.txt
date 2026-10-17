ORMAN BARKOD KAYIT - ANDROID APK HAZIRLAMA

ÖNEMLİ:
Bu paket, Windows Tkinter programının Android/Kivy arayüzüne uyarlanmış kaynak projesidir. Bu ortamda Android SDK/NDK ve Buildozer kurulu olmadığı için APK dosyası derlenmedi. Bu nedenle henüz hazır APK değildir.

APK üretmek için (en kolay yol Ubuntu/Linux veya WSL2):
1. Bu ZIP dosyasını Ubuntu/WSL içine çıkarın.
2. Python 3, pip, Java JDK ve Buildozer kurun.
3. Proje klasöründe terminal açıp şu komutları çalıştırın:
   python3 -m pip install --user buildozer
   buildozer android debug
4. İlk derlemede Android araçları indirileceğinden internet gerekir ve işlem uzun sürebilir.
5. Başarılı derleme sonunda bin/ klasöründe .apk dosyası oluşur.
6. APK dosyasını telefona aktarın ve kurulum izni vererek yükleyin.

NOTLAR:
- Uygulama kayıtlarını kendi uygulama veri klasöründe JSON olarak yedekler.
- Excel raporu da uygulamanın özel klasörüne kaydedilir. Android İndirilenler klasörüne doğrudan kaydetme/paylaşım özelliği henüz ekli değildir.
- Barkod alanı metin girişidir; telefon kamerasıyla barkod tarama henüz entegre edilmemiştir.
- APK derlenmeden önce Android ortamında test edilmelidir.
