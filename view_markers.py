#!/usr/bin/env python3
"""
ArUco Marker Viewer
Bu script oluşturulan marker'ları görüntüler.
"""

import cv2
import os
import glob

def show_markers(markers_folder="markers"):
    """Oluşturulan marker'ları gösterir."""
    
    if not os.path.exists(markers_folder):
        print(f"❌ Marker klasörü bulunamadı: {markers_folder}")
        return
    
    # PNG dosyalarını bul
    marker_files = glob.glob(os.path.join(markers_folder, "*.png"))
    
    if not marker_files:
        print(f"❌ {markers_folder} klasöründe marker bulunamadı!")
        return
    
    print(f"✅ {len(marker_files)} adet marker bulundu:")
    
    for marker_file in sorted(marker_files):
        filename = os.path.basename(marker_file)
        print(f"  - {filename}")
        
        # Marker'ı oku
        marker_img = cv2.imread(marker_file)
        
        if marker_img is None:
            print(f"❌ {filename} okunamadı!")
            continue
        
        # Marker'ı büyüt (daha iyi görünüm için)
        scale_factor = 2
        height, width = marker_img.shape[:2]
        resized = cv2.resize(marker_img, (width * scale_factor, height * scale_factor), 
                           interpolation=cv2.INTER_NEAREST)
        
        # Başlık ekle
        title_height = 50
        titled_img = cv2.copyMakeBorder(resized, title_height, 0, 0, 0, 
                                      cv2.BORDER_CONSTANT, value=(255, 255, 255))
        
        # Başlık metni ekle
        cv2.putText(titled_img, filename, (10, 35), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        
        # Pencere göster
        cv2.imshow(f"ArUco Marker: {filename}", titled_img)
        
        print(f"📱 {filename} gösteriliyor - Devam için herhangi bir tuşa basın...")
        cv2.waitKey(0)
        cv2.destroyWindow(f"ArUco Marker: {filename}")
    
    print("✅ Tüm marker'lar gösterildi!")
    print("\n🎯 Şimdi bu marker'lardan birini telefonla fotoğraflayabilirsiniz.")
    print("📷 Marker'ı ekranda açık bırakıp telefonla fotoğraf çekin.")

if __name__ == "__main__":
    print("=== ArUco Marker Viewer ===")
    print()
    show_markers()
