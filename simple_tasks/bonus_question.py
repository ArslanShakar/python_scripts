blue_categories = "25000 MQMs or 30 MQSs"
green_categories = "$3000 MQDs or $2500 Card Spending"
category_count = 1
categories = []

while category_count < 5:
    category = input("Enter category {}:".format(category_count))
    categories.append(category)
    category_count += 1

for cate in categories:
    print(cate)
    cate = cate.lower().replace(',', '')
    if cate in blue_categories.lower() or cate in green_categories.lower():
        print("Delta SkyMiles Member reached Silver Medallion Status")
    else:
        print("Delta SkyMiles Member has not reached Silver Medallion Status")
