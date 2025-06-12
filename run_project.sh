#!/bin/bash

# ArUco Marker Project - Ana Script

echo "=== ArUco Marker Project ==="
echo ""

# Renkli çıktı için
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

show_menu() {
    echo -e "${BLUE}Seçenekler:${NC}"
    echo "1. Yeni marker'lar oluştur"
    echo "2. Marker gallery'sini aç"
    echo "3. Kamera detection'ı başlat"
    echo "4. Proje hakkında bilgi"
    echo "5. Çıkış"
    echo ""
}

generate_markers() {
    echo -e "${YELLOW}Marker'lar oluşturuluyor...${NC}"
    python3 generate_markers.py
    echo ""
}

open_gallery() {
    echo -e "${YELLOW}Marker gallery açılıyor...${NC}"
    if command -v firefox >/dev/null 2>&1; then
        firefox marker_gallery.html &
    elif command -v google-chrome >/dev/null 2>&1; then
        google-chrome marker_gallery.html &
    elif command -v chromium-browser >/dev/null 2>&1; then
        chromium-browser marker_gallery.html &
    else
        echo -e "${RED}Web tarayıcı bulunamadı. Gallery'yi manuel olarak açın:${NC}"
        echo "file://$(pwd)/marker_gallery.html"
    fi
    echo ""
}

start_detection() {
    echo -e "${YELLOW}Kamera detection başlatılıyor...${NC}"
    echo -e "${GREEN}Marker'ınızı kameraya gösterin. Çıkmak için 'q' tuşuna basın.${NC}"
    echo ""
    python3 detect_markers.py
    echo ""
}

show_info() {
    echo -e "${BLUE}=== Proje Bilgileri ===${NC}"
    echo ""
    echo "🎯 ArUco Marker Detection Projesi"
    echo "📁 Proje klasörü: $(pwd)"
    echo ""
    echo "Dosyalar:"
    ls -la *.py *.html *.txt 2>/dev/null
    echo ""
    if [ -d "markers" ]; then
        echo "Marker'lar:"
        ls -la markers/ 2>/dev/null
    fi
    echo ""
    echo "Kullanım:"
    echo "1. Marker'ları oluştur"
    echo "2. Gallery'den marker seç"
    echo "3. Telefonla fotoğrafla"
    echo "4. Detection'ı başlat"
    echo ""
}

# Ana döngü
while true; do
    show_menu
    read -p "Seçiminiz (1-5): " choice
    
    case $choice in
        1)
            generate_markers
            ;;
        2)
            open_gallery
            ;;
        3)
            start_detection
            ;;
        4)
            show_info
            ;;
        5)
            echo -e "${GREEN}Görüşürüz! 👋${NC}"
            break
            ;;
        *)
            echo -e "${RED}Geçersiz seçim! Lütfen 1-5 arası bir sayı girin.${NC}"
            echo ""
            ;;
    esac
done
