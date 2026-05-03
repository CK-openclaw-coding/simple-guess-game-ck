import random

def guess_number():
    print("=== 猜數字遊戲 ===")
    target = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("請輸入一個 1 到 100 之間的數字: "))
            attempts += 1
            
            if guess < target:
                print("太小了！再試一次。")
            elif guess > target:
                print("太大了！再試一次。")
            else:
                print(f"恭喜你！你猜對了！目標數字就是 {target}。")
                print(f"你總共嘗試了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入有效的整數。")

if __name__ == "__main__":
    guess_number()
