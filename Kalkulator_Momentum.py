# mencari kecepatan dan momentum

def speed(distance, time):
    return distance / time

def momentum(mass, distance, time):
    return mass * (distance / time)

print("Pilihlah operasi yang kamu inginkan!")
print("1. Menghitung kecepatan")
print("2. Menghitung Momentum")

while True:
    # input dari user
    choice = input("Masukkan pilihamu(1/2): ")

    # aksi dari pilhan user
    if choice in ('1'):
        distance = float(input("Masukkan nilai jarak: "))
        time = float(input("Masukkan nilai waktu: "))

        if choice == '1':
            print(distance, "/", time, "=", speed(distance, time))
    
    elif choice in ('2'):
        mass = float(input("Masukkan nilai massa: "))
        distance = float(input("Masukkan nilai jarak: "))
        time = float(input("Masukkan nilai waktu: "))

        if choice == '2':
            print(distance, "/", time, "*", mass, "=", momentum(mass, distance, time))

        # user diberikan pilihan untuk menghitung lagi atau tidak
        next_calculation = input("Apakah kamu ingin menghitung lagi? (ya/tidak): ")
        if next_calculation == "tidak":
            break
