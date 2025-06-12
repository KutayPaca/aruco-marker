# ArUco Marker Project

Bu proje ArUco marker'larını oluşturmak ve detect etmek için geliştirilmiştir.

## Hızlı Başlangıç

Projeyi kolayca çalıştırmak için:

```bash
./run_project.sh
```

## Manuel Kurulum

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

### 1. ArUco Marker Oluşturma

```bash
python3 generate_markers.py
```

Bu komut:
- `markers/` klasöründe ArUco marker'ları oluşturur
- Farklı ID'lerde marker'lar üretir
- PNG formatında kaydeder

### 2. Marker Gallery

Marker'ları görmek için:
- `marker_gallery.html` dosyasını tarayıcıda açın
- Veya `./run_project.sh` ile menüden seçin

### 3. Marker Detection

```bash
python3 detect_markers.py
```

Bu komut:
- Laptop kamerasını açar
- Gerçek zamanlı ArUco marker detection yapar
- Bulunan marker'ların ID'sini ve pozisyonunu gösterir

## Özellikler

- **ArUco Dictionary**: DICT_6X6_50 kullanılır
- **Real-time Detection**: Kameradan canlı görüntü işleme
- **Marker Information**: ID ve pozisyon bilgileri
- **FPS Counter**: Performans takibi
- **Web Gallery**: Marker'ları görüntüleme arayüzü

## Kullanım Adımları

1. `generate_markers.py` ile marker'ları oluşturun
2. `marker_gallery.html` ile marker'ları görüntüleyin
3. Marker'ları yazdırın veya ekranda gösterin
4. Telefonla marker'ın fotoğrafını çekin
5. `detect_markers.py` ile detection'ı başlatın
6. Telefondaki marker fotoğrafını kameraya gösterin
7. Çıkmak için 'q' tuşuna basın

## Dosya Yapısı

```
aruco_marker/
├── generate_markers.py    # Marker oluşturma
├── detect_markers.py      # Marker detection
├── view_markers.py        # Marker görüntüleme
├── marker_gallery.html    # Web tabanlı gallery
├── run_project.sh         # Ana script
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Bu dosya
└── markers/              # Oluşturulan marker'lar
    ├── aruco_marker_0.png
    ├── aruco_marker_1.png
    ├── aruco_marker_2.png
    └── aruco_marker_23.png
```

## Troubleshooting

- Kamera açılmıyorsa farklı index değerleri deneyin (0, 1, 2...)
- Marker detect edilmiyorsa ışık koşullarını iyileştirin
- Marker'ın net ve düz olduğundan emin olun
- Telefon ekranının parlaklığını artırın
# aruco-marker
