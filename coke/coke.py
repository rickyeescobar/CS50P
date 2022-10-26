def main():
    coke_price = 50
    coins_in = 0
    balance = coke_price
    logic(balance, coins_in)

def logic(balance, coins_in):
    coins = 0
    while balance > 0:
        print("Amount Due: ", balance)
        coins_in = int(input("Insert Coin: "))

        while coins_in == 5 or coins_in == 10 or coins_in == 25:
            coins += coins_in
            balance -= coins_in
            if balance <= 0:
                break
            print("Amount Due: ", balance)
            coins_in = int(input("Insert Coin: "))


    change = balance * -1
    print("Change owed:", change)







main()
