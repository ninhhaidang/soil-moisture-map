#!/usr/bin/env python3
"""
Script để tách các file CYGNSS theo độ phân giải 9km và 36km
Tác giả: GitHub Copilot
"""

import os
import shutil
from pathlib import Path

def organize_cygnss_files():
    """
    Tách các file CYGNSS thành 2 thư mục theo độ phân giải:
    - 9km: chứa các file có độ phân giải 9km
    - 36km: chứa các file có độ phân giải 36km
    """
    
    # Đường dẫn thư mục gốc chứa dữ liệu CYGNSS
    source_dir = Path("Data/CYGNSS/cygnss_data")
    
    # Tạo đường dẫn thư mục đích
    dir_9km = source_dir / "9km"
    dir_36km = source_dir / "36km"
    
    # Tạo thư mục nếu chưa tồn tại
    dir_9km.mkdir(exist_ok=True)
    dir_36km.mkdir(exist_ok=True)
    
    print(f"Bắt đầu tổ chức các file trong: {source_dir}")
    print(f"Thư mục 9km: {dir_9km}")
    print(f"Thư mục 36km: {dir_36km}")
    print("-" * 60)
    
    # Đếm số file được di chuyển
    count_9km = 0
    count_36km = 0
    count_skipped = 0
    
    # Duyệt qua tất cả file trong thư mục gốc
    for file_path in source_dir.iterdir():
        # Chỉ xử lý file (không phải thư mục)
        if file_path.is_file() and file_path.suffix == '.nc':
            filename = file_path.name
            
            # Kiểm tra độ phân giải dựa trên tên file
            if '-9km.' in filename:
                # Di chuyển file 9km
                destination = dir_9km / filename
                shutil.move(str(file_path), str(destination))
                print(f"[9km]  {filename}")
                count_9km += 1
                
            elif '-36km.' in filename:
                # Di chuyển file 36km
                destination = dir_36km / filename
                shutil.move(str(file_path), str(destination))
                print(f"[36km] {filename}")
                count_36km += 1
                
            else:
                # File không khớp với pattern
                print(f"[SKIP] {filename} - Không xác định được độ phân giải")
                count_skipped += 1
    
    # In thống kê
    print("-" * 60)
    print("THỐNG KÊ:")
    print(f"✓ File 9km được di chuyển:  {count_9km}")
    print(f"✓ File 36km được di chuyển: {count_36km}")
    print(f"⚠ File bị bỏ qua:          {count_skipped}")
    print(f"📁 Tổng cộng:              {count_9km + count_36km + count_skipped}")
    
    if count_skipped == 0:
        print("\n🎉 Hoàn thành! Tất cả file đã được tổ chức thành công.")
    else:
        print(f"\n⚠️  Có {count_skipped} file không được di chuyển. Vui lòng kiểm tra lại.")

def main():
    """Hàm chính"""
    try:
        organize_cygnss_files()
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
