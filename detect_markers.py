#!/usr/bin/env python3
"""
ArUco Marker Detector
Bu script laptop kamerasından ArUco marker'ları detect eder.
"""

import cv2
import numpy as np
import time

class ArUcoDetector:
    def __init__(self):
        """ArUco detector'ı başlatır."""
        
        # ArUco dictionary oluştur (6x6 50 markers)
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
        
        # ArUco parametreleri oluştur
        self.aruco_params = cv2.aruco.DetectorParameters()
        
        # Kamera başlatılacak
        self.cap = None
        
        print("ArUco Detector hazır!")
        print("Kullanılan dictionary: DICT_6X6_50")
    
    def start_camera(self, camera_index=0):
        """Kamerayı başlatır."""
        
        self.cap = cv2.VideoCapture(camera_index)
        
        if not self.cap.isOpened():
            print(f"❌ Kamera açılamadı! (index: {camera_index})")
            return False
        
        # Kamera çözünürlüğünü ayarla
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        print(f"✅ Kamera başlatıldı (index: {camera_index})")
        return True
    
    def detect_markers(self, frame):
        """Frame'de ArUco marker'ları detect eder."""
        
        # Gri tonlamaya çevir
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # ArUco marker'ları detect et
        detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.aruco_params)
        corners, ids, rejected = detector.detectMarkers(gray)
        
        return corners, ids, rejected
    
    def draw_markers(self, frame, corners, ids):
        """Detect edilen marker'ları frame üzerine çizer."""
        
        if ids is not None and len(ids) > 0:
            # Marker'ları çiz
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            
            # Her marker için ID ve pozisyon bilgisini yazdır
            for i, marker_id in enumerate(ids.flatten()):
                # Marker köşelerini al
                corner = corners[i][0]
                
                # Marker merkezini hesapla
                center_x = int(np.mean(corner[:, 0]))
                center_y = int(np.mean(corner[:, 1]))
                
                # ID'yi yazdır
                cv2.putText(frame, f"ID: {marker_id}", 
                           (center_x-30, center_y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Pozisyon bilgisini yazdır
                cv2.putText(frame, f"({center_x}, {center_y})", 
                           (center_x-30, center_y+20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        
        return frame
    
    def add_info_text(self, frame, marker_count):
        """Frame'e bilgi metni ekler."""
        
        # Üst kısma bilgi metni
        info_text = f"ArUco Detector | Bulunan marker: {marker_count}"
        cv2.putText(frame, info_text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Alt kısma kontrol bilgileri
        control_text = "Cikis icin 'q' tusuna basin"
        cv2.putText(frame, control_text, (10, frame.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        
        return frame
    
    def run_detection(self):
        """Ana detection döngüsünü çalıştırır."""
        
        if self.cap is None:
            print("❌ Önce kamerayı başlatın!")
            return
        
        print("\n🎯 ArUco detection başladı!")
        print("Marker'ınızı kameraya gösterin...")
        print("Çıkmak için 'q' tuşuna basın\n")
        
        fps_counter = 0
        start_time = time.time()
        
        while True:
            # Frame oku
            ret, frame = self.cap.read()
            
            if not ret:
                print("❌ Frame okunamadı!")
                break
            
            # ArUco marker'ları detect et
            corners, ids, rejected = self.detect_markers(frame)
            
            # Marker sayısını hesapla
            marker_count = len(ids) if ids is not None else 0
            
            # Marker'ları çiz
            frame = self.draw_markers(frame, corners, ids)
            
            # Bilgi metni ekle
            frame = self.add_info_text(frame, marker_count)
            
            # FPS hesapla ve göster
            fps_counter += 1
            if fps_counter % 30 == 0:
                end_time = time.time()
                fps = 30 / (end_time - start_time)
                start_time = end_time
                print(f"FPS: {fps:.1f} | Marker sayısı: {marker_count}")
            
            # Frame'i göster
            cv2.imshow('ArUco Marker Detection', frame)
            
            # 'q' tuşuna basılırsa çık
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        print("\n🔴 Detection durduruldu.")
        self.stop()
    
    def stop(self):
        """Kamerayı kapatır ve kaynakları temizler."""
        
        if self.cap is not None:
            self.cap.release()
        
        cv2.destroyAllWindows()
        print("✅ Kaynaklar temizlendi.")

def main():
    """Ana fonksiyon."""
    
    print("=== ArUco Marker Detector ===")
    print()
    
    # Detector oluştur
    detector = ArUcoDetector()
    
    # Kamerayı başlat
    if not detector.start_camera(camera_index=0):
        print("Farklı kamera index'i deneyin (1, 2, vs.)")
        return
    
    try:
        # Detection'ı başlat
        detector.run_detection()
        
    except KeyboardInterrupt:
        print("\n⏹️ Kullanıcı tarafından durduruldu.")
        
    finally:
        # Temizlik
        detector.stop()

if __name__ == "__main__":
    main()
