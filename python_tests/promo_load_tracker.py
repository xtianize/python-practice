#dictionary-load and promo tracker

promos={"GIGA50": 50, "ALLDATA99": 99, "UNLI299": 299}
print("Available promos:")
print(list(promos.keys()))
chosen_promo=input("Enter promo name: ").upper()
print("Price: ", promos.get(chosen_promo,"Invalid promo"))
