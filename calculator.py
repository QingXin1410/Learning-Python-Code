def calcu_price(APPLE_PRICE):
	apple_weight = float(input("Nhập số kg Táo: "))
	print(f"Trọng lượng Táo khách hàng mua là: {apple_weight} KG")
	print("---------")
	total_price = int(APPLE_PRICE * apple_weight)
	return total_price

def amount_received(total_price):
	give_by_customer = int(input("Số tiền khách đưa: "))
	while give_by_customer < total_price:
		print("Khách hàng trả thiếu tiền. Vui lòng thanh toán lại. Xin cảm ơn!")
		give_by_customer = int(input("Số tiền khách đưa: "))
		if give_by_customer >= total_price:
			break
	return give_by_customer

def refund(total_price, give_by_customer):
	if total_price < give_by_customer:
		money_back = give_by_customer - total_price
		print(f"Số tiền trả lại khách: {money_back} VND")
		return money_back
	else:
		print("Cảm ơn Quý khách. Hẹn gặp lại!")

def face_value_of_money(money_back):
	amount_500k = money_back // 500000
	surplus = money_back % 500000
	if surplus < 1000:
		print(f"Số tờ tiền 500K: {amount_500k}")
	else:
		amount_200k = surplus // 200000
		surplus = surplus % 200000
		if surplus < 1000:
			print(f"Số tờ tiền 500K: {amount_500k}")
			print(f"Số tờ tiền 200K: {amount_200k}")
		else:
			amount_100k = surplus // 100000
			surplus = surplus % 100000
			if surplus < 1000:
				print(f"Số tờ tiền 500K: {amount_500k}")
				print(f"Số tờ tiền 200K: {amount_200k}")
				print(f"Số tờ tiền 100K: {amount_100k}")
			else:
				amount_50k = surplus // 50000
				surplus = surplus % 50000
				if surplus < 1000:
					print(f"Số tờ tiền 500K: {amount_500k}")
					print(f"Số tờ tiền 200K: {amount_200k}")
					print(f"Số tờ tiền 100K: {amount_100k}")
					print(f"Số tờ tiền 50K: {amount_50k}")
				else:
					amount_20k = surplus // 20000
					surplus = surplus % 20000
					if surplus < 1000:
						print(f"Số tờ tiền 500K: {amount_500k}")
						print(f"Số tờ tiền 200K: {amount_200k}")
						print(f"Số tờ tiền 100K: {amount_100k}")
						print(f"Số tờ tiền 50K: {amount_50k}")
						print(f"Số tờ tiền 20K: {amount_20k}")
					else:
						amount_10k = surplus // 10000
						surplus = surplus % 10000
						if surplus < 1000:
							print(f"Số tờ tiền 500K: {amount_500k}")
							print(f"Số tờ tiền 200K: {amount_200k}")
							print(f"Số tờ tiền 100K: {amount_100k}")
							print(f"Số tờ tiền 50K: {amount_50k}")
							print(f"Số tờ tiền 20K: {amount_20k}")
							print(f"Số tờ tiền 10K: {amount_10k}")
						else:
							amount_5k = surplus // 5000
							surplus = surplus % 5000
							if surplus < 1000:
								print(f"Số tờ tiền 500K: {amount_500k}")
								print(f"Số tờ tiền 200K: {amount_200k}")
								print(f"Số tờ tiền 100K: {amount_100k}")
								print(f"Số tờ tiền 50K: {amount_50k}")
								print(f"Số tờ tiền 20K: {amount_20k}")
								print(f"Số tờ tiền 10K: {amount_10k}")
								print(f"Số tờ tiền 5K: {amount_5k}")
							else:
								amount_2k = surplus // 2000
								surplus = surplus % 2000
								if surplus < 1000:
									print(f"Số tờ tiền 500K: {amount_500k}")
									print(f"Số tờ tiền 200K: {amount_200k}")
									print(f"Số tờ tiền 100K: {amount_100k}")
									print(f"Số tờ tiền 50K: {amount_50k}")
									print(f"Số tờ tiền 20K: {amount_20k}")
									print(f"Số tờ tiền 10K: {amount_10k}")
									print(f"Số tờ tiền 5K: {amount_5k}")
									print(f"Số tờ tiền 2K: {amount_2k}")
								else:
									amount_1k = surplus // 1000
									surplus = surplus % 1000
									if surplus < 1000:
										print(f"Số tờ tiền 500K: {amount_500k}")
										print(f"Số tờ tiền 200K: {amount_200k}")
										print(f"Số tờ tiền 100K: {amount_100k}")
										print(f"Số tờ tiền 50K: {amount_50k}")
										print(f"Số tờ tiền 20K: {amount_20k}")
										print(f"Số tờ tiền 10K: {amount_10k}")
										print(f"Số tờ tiền 5K: {amount_5k}")
										print(f"Số tờ tiền 2K: {amount_2k}")
										print(f"Số tờ tiền 1K: {amount_1k}")
										print(f"Lẻ: {surplus} VND")


def main():
	APPLE_PRICE = 72300 #VND/kg
	total_price = calcu_price(APPLE_PRICE)
	print(f"Thành tiền: {total_price} VND")
	give_by_customer = amount_received(total_price)
	money_back = refund(total_price, give_by_customer)
	if money_back > 0:
		print("Số lượng tờ tiền theo mệnh giá phải trả lại cho khách:")
		face_value_of_money(money_back)


main()