chon = 0

while chon != 6:
    print("===== MENU BÀI TOÁN =====")
    print("1. Tính tổng 2 số")
    print("2. Tính bình phương của 1 số")
    print("3. Kiểm tra số chẵn hay lẻ")
    print("4. Tính tổng từ 1 đến n")
    print("5. Tính giai thừa của 1 số")
   
    chon = int(input("Nhập lựa chọn của bạn (1-6): "))

    if chon == 1:
        print("\nBài toán: Tính tổng 2 số")
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("Nhập số thứ hai: "))
        tong = a + b
        print(f"Tổng của {a} và {b} là: {tong}\n")

    elif chon == 2:
        print("\nBài toán: Tính bình phương 1 số")
        n = int(input("Nhập số cần tính bình phương: "))
        bp = n * n
        print(f"Bình phương của {n} là: {bp}\n")

    elif chon == 3:
        print("\nBài toán: Kiểm tra chẵn lẻ")
        n = int(input("Nhập số cần kiểm tra: "))
        if n % 2 == 0:
            print(f"{n} là số chẵn.\n")
        else:
            print(f"{n} là số lẻ.\n")

    elif chon == 4:
        print("\nBài toán: Tính tổng từ 1 đến n")
        n = int(input("Nhập số n: "))
        tong = 0
        i = 1
        while i <= n:
            tong += i
            i += 1
        print(f"Tổng từ 1 đến {n} là: {tong}\n")

    elif chon == 5:
        print("\nBài toán: Tính giai thừa của 1 số")
        n = int(input("Nhập số n: "))
        gt = 1
        i = 1
        while i <= n:
            gt *= i
            i += 1
        print(f"Giai thừa của {n} là: {gt}\n")

    elif chon == 6:
        print("\nCảm ơn bạn đã sử dụng chương trình!\n")

    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn lại.\n")