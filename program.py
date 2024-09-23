def coin_change_greedy(coins, amount): 
  coin_count = 0
  coin_used = []
  
  coins.sort(reverse=True)
  
  for coin in coins:
    while amount >= coin:
      amount -= coin
      coin_count += 1
      coin_used.append(coin)
  
  if amount == 0:
    return coin_count, coin_used
  else:
    return -1, []  #Error jika coin tidak yang tersedia tidak bisa untuk menukar nilai uang

coins = [1, 2, 5, 10]
print(f"Koin yang tersedia: {coins}")
amount = int(input("Nilai uang yang ingin ditukarkan: "))

count, used = coin_change_greedy(coins, amount)
if count != -1:
  print(f"Koin minimum yang dibutuhkan: {count}")
  print(f"Koin yang terpakai: {used}")
else:
  print("Tidak bisa menukar nilai uang dengan nominal koin yang ada.")
