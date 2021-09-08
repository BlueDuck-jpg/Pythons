import requests
import json
import urllib


while True:
    print("Type quit to exit.")
    search = str(input("🔎︎: "))
    if search != "quit":
        max_limit = int(input("Max Limit: "))
        print("\n")

        response = requests.get(f"https://shopeeapi.smktd.repl.co/searchitem?keyword={search}%20&max_limit={max_limit}")
        a = json.loads(response.text)

        for index, b in enumerate(a['items'],1):
            i = b['item_basic']
            imageitem = f"{i['image']}_tn"
            link = urllib.parse.quote(i['name'])
            video = i['video_info_list'] or 'None'
            brand = i['brand'] or 'None'
            aja = 'None'
            if video != 'None':
                aja = video[0]['video_id']
            else:
                aja = 'None'
            if aja != 'None':
                print(f"{index}. Item ID: {i['itemid']}\nShop ID: {i['shopid']}\nName: {i['name']}\nImage: https://cf.shopee.com.my/file/{imageitem}\nLink: https://shopee.com.my/{link}-i.{i['shopid']}.{i['itemid']}\nVideo: https://cvf.shopee.com.my/file/{aja}\nPrice: {i['currency'] + ' ' + str(i['price'])[:2] + '.' + str(i['price'])[2:4]}\nStock: {i['stock']}\nBrand: {brand}\nDiscount: {i['discount']}\nSold: {i['sold']}\nRating: {str(i['item_rating']['rating_star'])[:2] +  str(i['item_rating']['rating_star'])[2:4] + '/5 (' + str(float(str(i['item_rating']['rating_star'])[:2] +  str(i['item_rating']['rating_star'])[2:4])/5*100) + '%)'}\n\n")
            else:
                print(f"{index}. Item ID: {i['itemid']}\nShop ID: {i['shopid']}\nName: {i['name']}\nImage: https://cf.shopee.com.my/file/{imageitem}\nLink: https://shopee.com.my/{link}-i.{i['shopid']}.{i['itemid']}\nPrice: {i['currency'] + ' ' + str(i['price'])[0:2] + '.' + str(i['price'])[2:4]}\nStock: {i['stock']}\nBrand: {brand}\nDiscount: {i['discount']}\nSold: {i['sold']}\nRating: {str(i['item_rating']['rating_star'])[:2] +  str(i['item_rating']['rating_star'])[2:4] + '/5 (' + str(float(str(i['item_rating']['rating_star'])[:2] +  str(i['item_rating']['rating_star'])[2:4])/5*100) + '%)'}\n\n")
    else:
        exit()