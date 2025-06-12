#!/usr/bin/env python3
"""
ArUco Marker Generator
Bu script ArUco marker'ları oluşturur ve kaydeder.
"""

import cv2
import numpy as np
import os

def generate_aruco_marker(marker_id, marker_size=200, save_path="markers"):
    """
    ArUco marker oluşturur ve kaydeder.
    
    Args:
        marker_id (int): Marker'ın ID'si (0-1023 arası)
        marker_size (int): Marker boyutu (pixel cinsinden)
        save_path (str): Marker'ların kaydedileceği klasör
    """
    
    # Klasör yoksa oluştur
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # ArUco dictionary oluştur (6x6 50 markers)
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
    
    # Marker oluştur
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
    
    # Dosya adı oluştur
    filename = f"{save_path}/aruco_marker_{marker_id}.png"
    
    # Marker'ı kaydet
    cv2.imwrite(filename, marker_image)
    
    print(f"ArUco marker oluşturuldu: {filename}")
    print(f"Marker ID: {marker_id}")
    print(f"Marker boyutu: {marker_size}x{marker_size} pixels")
    
    return filename

def generate_multiple_markers(start_id=0, count=5, marker_size=200):
    """
    Birden fazla ArUco marker oluşturur.
    
    Args:
        start_id (int): Başlangıç marker ID'si
        count (int): Oluşturulacak marker sayısı
        marker_size (int): Marker boyutu
    """
    
    print(f"Toplam {count} adet ArUco marker oluşturuluyor...")
    print("-" * 50)
    
    filenames = []
    for i in range(count):
        marker_id = start_id + i
        filename = generate_aruco_marker(marker_id, marker_size)
        filenames.append(filename)
        print()
    
    print("Tüm marker'lar başarıyla oluşturuldu!")
    print("Bu marker'ları yazdırıp kullanabilirsiniz.")
    
    return filenames

if __name__ == "__main__":
    print("=== ArUco Marker Generator ===")
    print()
    
    # Tek bir marker oluştur
    print("1. Tek marker oluşturuluyor...")
    generate_aruco_marker(marker_id=23, marker_size=400)
    print()
    
    # Birden fazla marker oluştur
    print("2. Çoklu marker'lar oluşturuluyor...")
    generate_multiple_markers(start_id=0, count=3, marker_size=300)
    
    print("\n🎯 Marker'lar hazır! Şimdi bunları yazdırıp telefonla fotoğraflayabilirsiniz.")
