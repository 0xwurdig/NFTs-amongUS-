from bs4 import BeautifulSoup
import requests
from PIL import Image
import random

# WEBSCRAPING


# d = {}
# a = ["Hats", "Skins", "Pets", "Visor_cosmetics", "Nameplates"]
# for j in a:
#     d[j] = []
#     res = requests.get(f"https://among-us.fandom.com/wiki/{j}")
#     soup = BeautifulSoup(res.text, "html.parser")
#     image = soup.select("#mw-content-text > div > table > tbody > tr")
#     for i in range(1, len(image)):
#         x = image[i].select("td.image > div > figure > a > img")
#         # try:
#         #     image_url = x[0]["data-src"]
#         # except:
#         #     image_url = x[0]["src"]
#         # image_url = image_url.split("/revision")[0]
#         print(x[0]["alt"])
#         d[j].append(x[0]["alt"])
#         if(x[0]["alt"]=="Yule Need to Log in.png"):
#             break
#         # img = Image.open(requests.get(image_url, stream=True).raw)
#         # img.save(f'{i}/{x[0]["alt"]}')

# # for cosmicubes
# d["Cosmicubes"]= []
# res = requests.get(f"https://among-us.fandom.com/wiki/Cosmicubes")
# soup = BeautifulSoup(res.text, "html.parser")
# image = soup.select("#mw-content-text > div > table > tbody > tr")
# for i in range(1, len(image)):
#     x = image[i].select("td > div > div > a > img")
#     print(x[0]["alt"])
#     d['Cosmicubes'].append(x[0]["alt"])
#     # try:
#     #     image_url = x[0]["data-src"]
#     # except:
#     #     image_url = x[0]["src"]
#     # image_url = image_url.split("/revision")[0]
#     # print(image_url)
#     # img = Image.open(requests.get(image_url, stream=True).raw)
#     # img.save(f'Cosmicubes/{x[0]["alt"]}')

# # for colors
# res = requests.get(f"https://among-us.fandom.com/wiki/Colors")
# soup = BeautifulSoup(res.text, "html.parser")
# image = soup.find_all("tr")
# d['Colors'] = []
# for i in range(1, 19):
#     x = image[i].find("img")
#     # try:
#     #     image_url = x["data-src"]
#     # except:
#     #     image_url = x["src"]
#     # image_url = image_url.split("/revision")[0]
#     d['Colors'].append(x["alt"])
#     # img = Image.open(requests.get(image_url, stream=True).raw)
#     # img.save(f'Colors/{x["alt"]}')

# for i in d:
#     print(f'{i} = {str(d[i])}')


Hats = {
    "A Real Wiz": {"height": 102, "width": 137, "left": -1180, "top": -603, "bool": 0},
    "Abominal Head": {
        "height": 145,
        "width": 168,
        "left": -1185.099365234375,
        "top": -611.2332763671875,
        "bool": 0,
    },
    "Aquatic Apparatus": {
        "height": 108,
        "width": 131,
        "left": -1135.424072265625,
        "top": -609.0374755859375,
        "bool": 0,
    },
    "Arrow'd": {
        "height": 350,
        "width": 350,
        "left": -1261.204833984375,
        "top": -653.8182983398438,
        "bool": 0,
    },
    "Batbean": {
        "height": 72,
        "width": 110,
        "left": -1141.7076416015625,
        "top": -579.70654296875,
        "bool": 0,
    },
    "Batty": {
        "height": 350,
        "width": 350,
        "left": -1259.0048828125,
        "top": -669.5680541992188,
        "bool": 0,
    },
    "Beanie": {
        "height": 77,
        "width": 118,
        "left": -1149.095458984375,
        "top": -580.2584838867188,
        "bool": 0,
    },
    "Bein Cheesy": {
        "height": 89,
        "width": 111,
        "left": -1140.44580078125,
        "top": -612.0060424804688,
        "bool": 0,
    },
    "Bighead": {
        "height": 114,
        "width": 74,
        "left": -1127.0010986328125,
        "top": -656.1422119140625,
        "bool": 1,
    },
    "Blondie": {
        "height": 98,
        "width": 127,
        "left": -1149.633056640625,
        "top": -584.9761352539062,
        "bool": 0,
    },
    "C4": {
        "height": 77,
        "width": 145,
        "left": -1140.633056640625,
        "top": -582.97607421875,
        "bool": 0,
    },
    "Caitlyn's Cap": {
        "height": 183,
        "width": 140,
        "left": -1160.00244140625,
        "top": -618.99658203125,
        "bool": 0,
    },
    "Can'tdy Cane": {
        "height": 75,
        "width": 114,
        "left": -1137.0009765625,
        "top": -611.5283203125,
        "bool": 0,
    },
    "Candycorny": {
        "height": 350,
        "width": 350,
        "left": -1258.599365234375,
        "top": -671.0546875,
        "bool": 0,
    },
    "Cap-tain": {
        "height": 84,
        "width": 125,
        "left": -1142.633056640625,
        "top": -600.9762573242188,
        "bool": 0,
    },
    "Cherry on Top": {
        "height": 80,
        "width": 78,
        "left": -1129.0010986328125,
        "top": -610.2828369140625,
        "bool": 0,
    },
    "Chocolate Scoop": {
        "height": 83,
        "width": 92,
        "left": -1136,
        "top": -604.168701171875,
        "bool": 0,
    },
    "Chomper": {
        "height": 98,
        "width": 127,
        "left": -1153.5,
        "top": -611.2076416015625,
        "bool": 0,
    },
    "Chop-chop": {
        "height": 137,
        "width": 206,
        "left": -1190.9237060546875,
        "top": -639.2180786132812,
        "bool": 0,
    },
    "Claggor's Goggles": {
        "height": 62,
        "width": 122,
        "left": -1135.6331787109375,
        "top": -555.9761962890625,
        "bool": 0,
    },
    "Clogged": {
        "height": 121,
        "width": 73,
        "left": -1121.5714111328125,
        "top": -651.6500854492188,
        "bool": 0,
    },
    "Clown Town": {
        "height": 106,
        "width": 210,
        "left": -1189.6328125,
        "top": -608.003173828125,
        "bool": 0,
    },
    "Cold One": {
        "height": 107,
        "width": 138,
        "left": -1147.633056640625,
        "top": -593.976318359375,
        "bool": 0,
    },
    "Comfy Pom": {
        "height": 120,
        "width": 155,
        "left": -1169.4473876953125,
        "top": -620.37109375,
        "bool": 0,
    },
    "Cool Katie": {
        "height": 175,
        "width": 147,
        "left": -1170.194580078125,
        "top": -622.3665771484375,
        "bool": 0,
    },
    "Corrupted Official": {
        "height": 108,
        "width": 129,
        "left": -1159.9698486328125,
        "top": -610.1731567382812,
        "bool": 1,
    },
    "Crack-a-lacking": {
        "height": 350,
        "width": 350,
        "left": -1260.00244140625,
        "top": -670.4246215820312,
        "bool": 0,
    },
    "Crane Operator": {
        "height": 122,
        "width": 159,
        "left": -1161.4241943359375,
        "top": -618.19775390625,
        "bool": 0,
    },
    "Crewmate Suit": {
        "height": 99,
        "width": 67,
        "left": -1125.9176025390625,
        "top": -618.2642211914062,
        "bool": 0,
    },
    "Crowned": {
        "height": 86,
        "width": 96,
        "left": -1155.29736328125,
        "top": -602.7946166992188,
        "bool": 0,
    },
    "Daisy Me Rollin'": {
        "height": 86,
        "width": 120,
        "left": -1160.4036865234375,
        "top": -577.5993041992188,
        "bool": 0,
    },
    "Deck The Halls": {
        "height": 106,
        "width": 141,
        "left": -1180.8370361328125,
        "top": -599.3421020507812,
        "bool": 0,
    },
    "Digging Helmet": {
        "height": 96,
        "width": 132,
        "left": -1162.9241943359375,
        "top": -597.0379028320312,
        "bool": 0,
    },
    "Done D": {
        "height": 99,
        "width": 163,
        "left": -1178.001220703125,
        "top": -604.8623046875,
        "bool": 1,
    },
    "Drill": {"height": 115, "width": 109, "left": -1144.5, "top": -610.5, "bool": 0},
    "Drinking_Cap": {
        "height": 63,
        "width": 80,
        "left": -1085.080078125,
        "top": -553,
        "bool": 0,
    },
    "Eggscellent": {
        "height": 77,
        "width": 102,
        "left": -1137.0447998046875,
        "top": -578.003662109375,
        "bool": 0,
    },
    "Enforcer Helmet": {
        "height": 157,
        "width": 160,
        "left": -1154.4234619140625,
        "top": -603.7573852539062,
        "bool": 2,
    },
    "Eruptive": {
        "height": 77,
        "width": 108,
        "left": -1137.1986083984375,
        "top": -571.2647094726562,
        "bool": 0,
    },
    "Evergreen": {
        "height": 103,
        "width": 66,
        "left": -1119.7171630859375,
        "top": -638.0543212890625,
        "bool": 0,
    },
    "Exotic Flower": {
        "height": 161,
        "width": 160,
        "left": -1190.7972412109375,
        "top": -628.8882446289062,
        "bool": 0,
    },
    "Fairy Flutters": {
        "height": 350,
        "width": 350,
        "left": -1265,
        "top": -680.8622436523438,
        "bool": 0,
    },
    "Fedorable": {
        "height": 79,
        "width": 162,
        "left": -1159.2015380859375,
        "top": -584.0812377929688,
        "bool": 0,
    },
    "Fez up": {
        "height": 91,
        "width": 95,
        "left": -1157.8397216796875,
        "top": -596.8623046875,
        "bool": 1,
    },
    "Fish Hed": {
        "height": 146,
        "width": 119,
        "left": -1157.68310546875,
        "top": -622.37646484375,
        "bool": 0,
    },
    "Floaty Flamingo": {
        "height": 115,
        "width": 141,
        "left": -1165,
        "top": -627.30712890625,
        "bool": 0,
    },
    "Folded": {
        "height": 103,
        "width": 118,
        "left": -1144.0748291015625,
        "top": -614.4351806640625,
        "bool": 0,
    },
    "Franken's Spouse": {
        "height": 182,
        "width": 149,
        "left": -1165,
        "top": -636,
        "bool": 0,
    },
    "Frankenbolts": {
        "height": 350,
        "width": 350,
        "left": -1259.0966796875,
        "top": -670.8065795898438,
        "bool": 0,
    },
    "Freshly Showered": {
        "height": 125,
        "width": 121,
        "left": -1143.25732421875,
        "top": -626.0375366210938,
        "bool": 0,
    },
    "Frosted": {
        "height": 112,
        "width": 103,
        "left": -1146.14208984375,
        "top": -631.2635498046875,
        "bool": 0,
    },
    "Funky Fusion": {
        "height": 132,
        "width": 127,
        "left": -1146.4093017578125,
        "top": -626.4390258789062,
        "bool": 0,
    },
    # "Gartner": {
    #     "height": 163,
    #     "width": 181,
    #     "left": -1172.4595947265625,
    #     "top": -600.7638549804688,
    #     "bool": 0,
    # },
    "Generally Speaking": {
        "height": 84,
        "width": 125,
        "left": -1143.6353759765625,
        "top": -600.0523681640625,
        "bool": 0,
    },
    "Gift Wrapped": {
        "height": 102,
        "width": 112,
        "left": -1140.718994140625,
        "top": -629.23291015625,
        "bool": 0,
    },
    "Gingercrew": {
        "height": 128,
        "width": 112,
        "left": -1146,
        "top": -647.3731689453125,
        "bool": 0,
    },
    "Goggles Up": {
        "height": 71,
        "width": 118,
        "left": -1136.924072265625,
        "top": -572.0374755859375,
        "bool": 0,
    },
    "Greatest Headset MIRA": {
        "height": 350,
        "width": 350,
        "left": -1259.2393798828125,
        "top": -670.9484252929688,
        "bool": 0,
    },
    "Greh": {
        "height": 89,
        "width": 156,
        "left": -1171.2930908203125,
        "top": -537.1453247070312,
        "bool": 0,
    },
    "Haunted Hotel Hat": {
        "height": 84,
        "width": 146,
        "left": -1148.14599609375,
        "top": -585,
        "bool": 0,
    },
    "Head in the Clouds": {
        "height": 58,
        "width": 112,
        "left": -1146,
        "top": -607.7651977539062,
        "bool": 0,
    },
    "Header": {
        "height": 100,
        "width": 104,
        "left": -1138.69970703125,
        "top": -625.2400512695312,
        "bool": 0,
    },
    "Headslug hat": {
        "height": 109,
        "width": 104,
        "left": -1131.333740234375,
        "top": -630.751708984375,
        "bool": 0,
    },
    "Heimerdinger's Hair": {
        "height": 350,
        "width": 350,
        "left": -1265,
        "top": -663.614013671875,
        "bool": 0,
    },
    "Headcrab": {
        "height": 35,
        "width": 53,
        "left": -1110.9927978515625,
        "top": -570.5,
        "bool": 0,
    },
    "Hole in One": {
        "height": 92,
        "width": 92,
        "left": -1133.924560546875,
        "top": -620.228515625,
        "bool": 0,
    },
    "Hooded Figure": {
        "height": 87,
        "width": 118,
        "left": -1155.71435546875,
        "top": -594.6673583984375,
        "bool": 0,
    },
    "I heart u": {
        "height": 61,
        "width": 71,
        "left": -1119.0399169921875,
        "top": -611.0792236328125,
        "bool": 0,
    },
    "I'm Burt": {
        "height": 350,
        "width": 350,
        "left": -1258.85498046875,
        "top": -670.0975341796875,
        "bool": 0,
    },
    "Ice Cap": {
        "height": 76,
        "width": 107,
        "left": -1139.2843017578125,
        "top": -569.8998413085938,
        "bool": 0,
    },
    "Imp-ressive": {
        "height": 350,
        "width": 350,
        "left": -1265,
        "top": -680.8622436523438,
        "bool": 0,
    },
    "Important Documents": {
        "height": 81,
        "width": 137,
        "left": -1158.5,
        "top": -593.5,
        "bool": 0,
    },
    "Innocence": {
        "height": 41,
        "width": 111,
        "left": -1140.1331787109375,
        "top": -592.3560180664062,
        "bool": 0,
    },
    "Jayce's Hair": {
        "height": 83,
        "width": 116,
        "left": -1145.925537109375,
        "top": -570.7579956054688,
        "bool": 0,
    },
    "Jinx's Hair": {
        "height": 201,
        "width": 143,
        "left": -1168.3671875,
        "top": -570.1347045898438,
        "bool": 0,
    },
    "Kiss me": {
        "height": 350,
        "width": 350,
        "left": -1244.0301513671875,
        "top": -742.5090942382812,
        "bool": 0,
    },
    "Knighted": {
        "height": 125,
        "width": 146,
        "left": -1161,
        "top": -626.850830078125,
        "bool": 0,
    },
    "Krampus": {
        "height": 350,
        "width": 350,
        "left": -1258.2877197265625,
        "top": -669.7598266601562,
        "bool": 0,
    },
    "Light_bulb": {
        "height": 42,
        "width": 27,
        "left": -1097.00390625,
        "top": -580.4382934570312,
        "bool": 0,
    },
    "Lit Up": {
        "height": 105,
        "width": 165,
        "left": -1158.123291015625,
        "top": -607.3241577148438,
        "bool": 0,
    },
    "Magical 'Corn": {
        "height": 350,
        "width": 350,
        "left": -1265,
        "top": -680.8622436523438,
        "bool": 0,
    },
    "Mask, the Monster Mask": {
        "height": 122,
        "width": 142,
        "left": -1154.9259033203125,
        "top": -630.7569580078125,
        "bool": 0,
    },
    "Militant": {
        "height": 89,
        "width": 133,
        "left": -1145.923583984375,
        "top": -603.2717895507812,
        "bool": 0,
    },
    "Miner Setback": {
        "height": 78,
        "width": 125,
        "left": -1136.7093505859375,
        "top": -583.0811767578125,
        "bool": 0,
    },
    "Mini Crewmate Hat": {
        "height": 107,
        "width": 96,
        "left": -1130.616943359375,
        "top": -624.5881958007812,
        "bool": 0,
    },
    "MoRawk": {
        "height": 350,
        "width": 350,
        "left": -1265,
        "top": -680.8621826171875,
        "bool": 0,
    },
    "Mr. Macbeth": {
        "height": 137,
        "width": 141,
        "left": -1168.3555908203125,
        "top": -642.8623657226562,
        "bool": 1,
    },
    "Muenster": {
        "height": 141,
        "width": 134,
        "left": -1165,
        "top": -636.1092529296875,
        "bool": 1,
    },
    "Muffs for the Ears": {
        "height": 350,
        "width": 350,
        "left": -1259.7811279296875,
        "top": -670.6216430664062,
        "bool": 0,
    },
    "Mummy Mood": {
        "height": 80,
        "width": 135,
        "left": -1155.4246826171875,
        "top": -559.2643432617188,
        "bool": 0,
    },
    "Museum Security": {
        "height": 88,
        "width": 145,
        "left": -1137.310302734375,
        "top": -581.1110229492188,
        "bool": 0,
    },
    "My Name Chef": {
        "height": 119,
        "width": 113,
        "left": -1173.6826171875,
        "top": -626.6939086914062,
        "bool": 1,
    },
    "Mysterious Vagabond": {
        "height": 130,
        "width": 139,
        "left": -1147.4232177734375,
        "top": -566.0375366210938,
        "bool": 2,
    },
    "Nimrod": {
        "height": 133,
        "width": 161,
        "left": -1162.9234619140625,
        "top": -637.5877075195312,
        "bool": 0,
    },
    "Noire Evening": {
        "height": 76,
        "width": 166,
        "left": -1160.9237060546875,
        "top": -583.7572021484375,
        "bool": 0,
    },
    "OSHA Compliant": {
        "height": 81,
        "width": 137,
        "left": -1140.0455322265625,
        "top": -583.7098388671875,
        "bool": 0,
    },
    "Oh Dear, Rain": {
        "height": 123,
        "width": 151,
        "left": -1166.0006103515625,
        "top": -655.2328491210938,
        "bool": 0,
    },
    "One in the Hand": {
        "height": 93,
        "width": 150,
        "left": -1142.4566650390625,
        "top": -599.5001220703125,
        "bool": 0,
    },
    "P Hat": {
        "height": 105,
        "width": 97,
        "left": -1143.25390625,
        "top": -624.2640380859375,
        "bool": 0,
    },
    "Peach Drink": {
        "height": 127,
        "width": 84,
        "left": -1141.34228515625,
        "top": -647.9039916992188,
        "bool": 0,
    },
    "Peeled": {
        "height": 106,
        "width": 143,
        "left": -1152.3460693359375,
        "top": -606,
        "bool": 0,
    },
    "Pining for you": {
        "height": 109,
        "width": 97,
        "left": -1133.5711669921875,
        "top": -628.2639770507812,
        "bool": 0,
    },
    "Plagued hat": {
        "height": 93,
        "width": 107,
        "left": -1152.8138427734375,
        "top": -595.3162841796875,
        "bool": 0,
    },
    "Planted": {
        "height": 136,
        "width": 92,
        "left": -1150.6171875,
        "top": -660.640869140625,
        "bool": 0,
    },
    "Policeman-Officer": {
        "height": 89,
        "width": 133,
        "left": -1148,
        "top": -597.5,
        "bool": 0,
    },
    "Pompous Pompadour": {
        "height": 109,
        "width": 131,
        "left": -1146,
        "top": -590.9456787109375,
        "bool": 0,
    },
    "Poor Reception": {
        "height": 89,
        "width": 54,
        "left": -1137.62646484375,
        "top": -615.4427490234375,
        "bool": 0,
    },
    "Presents Dude": {
        "height": 107,
        "width": 158,
        "left": -1178.51171875,
        "top": -606.5,
        "bool": 0,
    },
    "Prototype Helmet": {
        "height": 86,
        "width": 177,
        "left": -1178.5,
        "top": -561.9254150390625,
        "bool": 2,
    },
    "Punkin": {
        "height": 108,
        "width": 130,
        "left": -1152.9232177734375,
        "top": -609.0375366210938,
        "bool": 0,
    },
    "RIP in Pieces": {
        "height": 115,
        "width": 105,
        "left": -1142.5,
        "top": -633.807861328125,
        "bool": 0,
    },
    "Rammed": {
        "height": 350,
        "width": 350,
        "left": -1265,
        "top": -680.8622436523438,
        "bool": 0,
    },
    "Ratchet ears": {
        "height": 133,
        "width": 210,
        "left": -1177.9583740234375,
        "top": -595.5321044921875,
        "bool": 0,
    },
    "Records Recorder": {
        "height": 144,
        "width": 135,
        "left": -1164.3553466796875,
        "top": -644.2564086914062,
        "bool": 1,
    },
    "Recruited Ellie": {
        "height": 125,
        "width": 125,
        "left": -1167.4254150390625,
        "top": -621.4193725585938,
        "bool": 1,
    },
    "Recruited Henry": {
        "height": 125,
        "width": 125,
        "left": -1165.878662109375,
        "top": -623.1407470703125,
        "bool": 1,
    },
    "Red-headed Outlaw": {
        "height": 117,
        "width": 157,
        "left": -1148.57373046875,
        "top": -571,
        "bool": 0,
    },
    "Right Hand Hat": {
        "height": 178,
        "width": 185,
        "left": -1195.949462890625,
        "top": -636.2130126953125,
        "bool": 1,
    },
    "Rupert": {
        "height": 136,
        "width": 134,
        "left": -1153.0166015625,
        "top": -601.026611328125,
        "bool": 0,
    },
    "Safety Second": {
        "height": 76,
        "width": 120,
        "left": -1142.84814453125,
        "top": -570.3228149414062,
        "bool": 0,
    },
    "Serengetti Outta Here": {
        "height": 79,
        "width": 140,
        "left": -1146.1861572265625,
        "top": -573.0278930664062,
        "bool": 0,
    },
    "Shrine to the Deities": {
        "height": 107,
        "width": 113,
        "left": -1148.517578125,
        "top": -614.2111206054688,
        "bool": 0,
    },
    "Siberia James": {
        "height": 112,
        "width": 167,
        "left": -1177.7509765625,
        "top": -608.9996337890625,
        "bool": 1,
    },
    "Sir Wilford IV": {
        "height": 179,
        "width": 176,
        "left": -1193.933349609375,
        "top": -658.0625,
        "bool": 1,
    },
    "Slippery When Wet": {
        "height": 350,
        "width": 350,
        "left": -1259.2392578125,
        "top": -668.4832153320312,
        "bool": 0,
    },
    "Smitten'd & Mitten'd": {
        "height": 350,
        "width": 350,
        "left": -1259.80126953125,
        "top": -671.6043701171875,
        "bool": 0,
    },
    "Snowflake": {
        "height": 119,
        "width": 168,
        "left": -1165,
        "top": -620.1115112304688,
        "bool": 0,
    },
    "Snowmate hat": {
        "height": 91,
        "width": 86,
        "left": -1125.9171142578125,
        "top": -610.2637329101562,
        "bool": 0,
    },
    "Spacewalk": {
        "height": 111,
        "width": 121,
        "left": -1155.5579833984375,
        "top": -619.8966064453125,
        "bool": 0,
    },
    "Spiked": {
        "height": 98,
        "width": 96,
        "left": -1135.9228515625,
        "top": -623.2456665039062,
        "bool": 0,
    },
    "Splitting Headache": {
        "height": 121,
        "width": 152,
        "left": -1179.946044921875,
        "top": -616.8914184570312,
        "bool": 0,
    },
    "Stickmin Brows": {
        "height": 28,
        "width": 72,
        "left": -1097.1507568359375,
        "top": -580.9995727539062,
        "bool": 0,
    },
    "Stickmin Rider": {
        "height": 90,
        "width": 123,
        "left": -1121.858642578125,
        "top": -619.6389770507812,
        "bool": 0,
    },
    "Strike": {
        "height": 92,
        "width": 91,
        "left": -1129.9278564453125,
        "top": -618.7564086914062,
        "bool": 0,
    },
    "Surveillance Joe": {
        "height": 136,
        "width": 131,
        "left": -1157.3519287109375,
        "top": -630.4970092773438,
        "bool": 1,
    },
    "Sven Svensson": {
        "height": 140,
        "width": 146,
        "left": -1165.0015869140625,
        "top": -623.6249389648438,
        "bool": 0,
    },
    "Swarshburgalor": {
        "height": 85,
        "width": 156,
        "left": -1182.0599365234375,
        "top": -558.6304321289062,
        "bool": 0,
    },
    "Take Cover": {
        "height": 107,
        "width": 142,
        "left": -1154.9234619140625,
        "top": -568.5301513671875,
        "bool": 0,
    },
    "Ten Gallons": {
        "height": 125,
        "width": 172,
        "left": -1183.442626953125,
        "top": -635.4122314453125,
        "bool": 1,
    },
    "That Old Top Hat we Found": {
        "height": 145,
        "width": 158,
        "left": -1173.0010986328125,
        "top": -639.9660034179688,
        "bool": 1,
    },
    "The Last Wipe": {
        "height": 79,
        "width": 95,
        "left": -1146.6895751953125,
        "top": -604.4635009765625,
        "bool": 0,
    },
    "The New Chief": {
        "height": 115,
        "width": 141,
        "left": -1160.501220703125,
        "top": -625.110595703125,
        "bool": 1,
    },
    "The Ol' Ball Game": {
        "height": 76,
        "width": 113,
        "left": -1149.2432861328125,
        "top": -579.09521484375,
        "bool": 0,
    },
    "The Wall Cap": {
        "height": 93,
        "width": 114,
        "left": -1144.924072265625,
        "top": -597.4133911132812,
        "bool": 0,
    },
    "Third Eye": {
        "height": 350,
        "width": 350,
        "left": -1265,
        "top": -680.8622436523438,
        "bool": 0,
    },
    "Thomas Top": {
        "height": 158,
        "width": 144,
        "left": -1172.40380859375,
        "top": -652.4885864257812,
        "bool": 1,
    },
    "Tightened Security": {
        "height": 65,
        "width": 147,
        "left": -1138.3524169921875,
        "top": -581.8648071289062,
        "bool": 0,
    },
    "Tiny Jim": {
        "height": 69,
        "width": 120,
        "left": -1147.9234619140625,
        "top": -580.257080078125,
        "bool": 0,
    },
    "Toppat Chief": {
        "height": 141,
        "width": 143,
        "left": -1176.2757568359375,
        "top": -652.3603515625,
        "bool": 1,
    },
    "Toppat Grunt": {
        "height": 113,
        "width": 136,
        "left": -1165.0008544921875,
        "top": -625.3406982421875,
        "bool": 1,
    },
    "Toppat White Edition": {
        "height": 113,
        "width": 136,
        "left": -1159.44091796875,
        "top": -623.794189453125,
        "bool": 1,
    },
    "Toy Dude": {
        "height": 105,
        "width": 168,
        "left": -1186.534423828125,
        "top": -620.385498046875,
        "bool": 0,
    },
    "Traffic Jam - Purple": {
        "height": 122,
        "width": 86,
        "left": -1144.762939453125,
        "top": -635.8108520507812,
        "bool": 0,
    },
    "Traffic Jam": {
        "height": 122,
        "width": 86,
        "left": -1144.762939453125,
        "top": -635.8108520507812,
        "bool": 0,
    },
    "Two Eggs in a Nest": {
        "height": 65,
        "width": 111,
        "left": -1141.37841796875,
        "top": -585.509521484375,
        "bool": 0,
    },
    "Unbearable": {
        "height": 55,
        "width": 112,
        "left": -1137.03857421875,
        "top": -578.0782470703125,
        "bool": 0,
    },
    "Unique Specimin": {
        "height": 105,
        "width": 145,
        "left": -1158.4073486328125,
        "top": -612.0009765625,
        "bool": 0,
    },
    "Up All Night Raving": {
        "height": 124,
        "width": 198,
        "left": -1194.3309326171875,
        "top": -615,
        "bool": 0,
    },
    "Vi King": {
        "height": 350,
        "width": 350,
        "left": -1314.980224609375,
        "top": -677.3927001953125,
        "bool": 0,
    },
    "Vi's Hair": {
        "height": 100,
        "width": 163,
        "left": -1178.00146484375,
        "top": -602.2832641601562,
        "bool": 0,
    },
    "Vine just Vine": {
        "height": 350,
        "width": 350,
        "left": -1259.3250732421875,
        "top": -670.3245239257812,
        "bool": 0,
    },
    "Visor Hat": {
        "height": 48,
        "width": 156,
        "left": -1145.9990234375,
        "top": -543.0003662109375,
        "bool": 0,
    },
    "Walk the Plank": {
        "height": 110,
        "width": 141,
        "left": -1158.4222412109375,
        "top": -620.6312866210938,
        "bool": 0,
    },
    "Wall Ushanka": {
        "height": 93,
        "width": 114,
        "left": -1144.924072265625,
        "top": -597.4133911132812,
        "bool": 0,
    },
    "We All Float Here": {
        "height": 114,
        "width": 74,
        "left": -1127.0010986328125,
        "top": -656.1422119140625,
        "bool": 0,
    },
    "Wearwolf": {
        "height": 98,
        "width": 136,
        "left": -1154.3516845703125,
        "top": -602,
        "bool": 0,
    },
    "What is up, Doc?": {
        "height": 68,
        "width": 101,
        "left": -1132.8310546875,
        "top": -579.7571411132812,
        "bool": 0,
    },
    "Winter Arrives": {
        "height": 179,
        "width": 142,
        "left": -1152.4310302734375,
        "top": -601.8453369140625,
        "bool": 0,
    },
    "Witch One": {
        "height": 121,
        "width": 209,
        "left": -1182.423828125,
        "top": -622.03759765625,
        "bool": 0,
    },
    "You Glove to See it": {
        "height": 104,
        "width": 129,
        "left": -1154.5,
        "top": -605,
        "bool": 0,
    },
    "You're Boned": {
        "height": 124,
        "width": 65,
        "left": -1122.501953125,
        "top": -655.2009887695312,
        "bool": 0,
    },
    "You're Out!": {
        "height": 92,
        "width": 92,
        "left": -1130.00341796875,
        "top": -620.0028686523438,
        "bool": 0,
    },
    "Young Sprout": {
        "height": 79,
        "width": 109,
        "left": -1144.5,
        "top": -619.4862060546875,
        "bool": 0,
    },
    "Yule Need to Log in": {
        "height": 104,
        "width": 169,
        "left": -1174.5,
        "top": -615.477294921875,
        "bool": 0,
    },
}
Skins = {
    "Abominal Snowmate": {
        "height": 119,
        "width": 136,
        "left": -1151.267333984375,
        "top": -476.17803955078125,
    },
    "Airship Mechanic": {
        "height": 112,
        "width": 125,
        "left": -1140,
        "top": -469.4835510253906,
    },
    "Astronaught": {
        "height": 112,
        "width": 123,
        "left": -1141.4998779296875,
        "top": -470.39990234375,
    },
    "Big Ol' Pumpkin Pants": {
        "height": 97,
        "width": 220,
        "left": -1207.9010009765625,
        "top": -489.3841857910156,
    },
    "Bling Bling": {
        "height": 102,
        "width": 137,
        "left": -1152,
        "top": -486.17034912109375,
    },
    "Business Skirt": {
        "height": 131,
        "width": 125,
        "left": -1142.28759765625,
        "top": -486,
    },
    "Caitlyn's Uniform": {
        "height": 126,
        "width": 134,
        "left": -1148.263916015625,
        "top": -481.8416442871094,
    },
    "Chaos Containment Crewmate": {
        "height": 115,
        "width": 127,
        "left": -1143.2637939453125,
        "top": -475.4498596191406,
    },
    "Claus, Mrs. Claus": {
        "height": 126,
        "width": 228,
        "left": -1204.5,
        "top": -496.12933349609375,
    },
    "Cozy Sweater": {
        "height": 118,
        "width": 142,
        "left": -1152.2637939453125,
        "top": -476.4403991699219,
    },
    "Crewbo the Clown": {
        "height": 130,
        "width": 170,
        "left": -1168.0521240234375,
        "top": -484.0605773925781,
    },
    "Dark Scientist": {
        "height": 114,
        "width": 133,
        "left": -1144.023193359375,
        "top": -474.3773193359375,
    },
    "Digging Kid": {
        "height": 112,
        "width": 123,
        "left": -1140.8934326171875,
        "top": -471.54388427734375,
    },
    "Doctor": {
        "height": 114,
        "width": 133,
        "left": -1144.842041015625,
        "top": -473.9208679199219,
    },
    "Enforcer Armor": {
        "height": 123,
        "width": 134,
        "left": -1150.2637939453125,
        "top": -477.0604248046875,
    },
    "Fairy Godcrewmate": {
        "height": 141,
        "width": 173,
        "left": -1170.14892578125,
        "top": -500.4877624511719,
    },
    "Flashy": {
        "height": 114,
        "width": 123,
        "left": -1140.4761962890625,
        "top": -474.7463073730469,
    },
    "General Galeforce": {
        "height": 113,
        "width": 131,
        "left": -1143.392578125,
        "top": -475.0684509277344,
    },
    "Guarding the Wall": {
        "height": 113,
        "width": 130,
        "left": -1146.2635498046875,
        "top": -474.67730712890625,
    },
    "Hazmate": {
        "height": 130,
        "width": 126,
        "left": -1144.2635498046875,
        "top": -489.991943359375,
    },
    "Heeeere's Santa!": {
        "height": 129,
        "width": 150,
        "left": -1158.34375,
        "top": -489.06341552734375,
    },
    "Heimerdinger's Suit": {
        "height": 123,
        "width": 159,
        "left": -1163.5924072265625,
        "top": -482.4066467285156,
    },
    "I Vant to Keel": {
        "height": 142,
        "width": 213,
        "left": -1187.763671875,
        "top": -497.8416442871094,
    },
    "I Want my Mummy": {
        "height": 120,
        "width": 125,
        "left": -1142,
        "top": -475,
    },
    "I'll Fix It": {
        "height": 120,
        "width": 123,
        "left": -1141.0263671875,
        "top": -473.503173828125,
    },
    "Ice to Meet You": {
        "height": 129,
        "width": 148,
        "left": -1157.417724609375,
        "top": -487.6576843261719,
    },
    "Inmate 2112": {
        "height": 112,
        "width": 123,
        "left": -1141.0263671875,
        "top": -471.43182373046875,
    },
    "Jacket Up": {
        "height": 127,
        "width": 140,
        "left": -1148.703125,
        "top": -487.0050354003906,
    },
    "Janitorial Duties": {
        "height": 114,
        "width": 142,
        "left": -1158.2635498046875,
        "top": -472.64697265625,
    },
    "Jayce's Council Suit": {
        "height": 123,
        "width": 137,
        "left": -1148.2781982421875,
        "top": -476.7568359375,
    },
    "Jinx's Clothes": {
        "height": 134,
        "width": 122,
        "left": -1142.263671875,
        "top": -492.6495361328125,
    },
    "Keepin it Secure": {
        "height": 115,
        "width": 127,
        "left": -1143.263671875,
        "top": -474.8356018066406,
    },
    "Land Here": {
        "height": 112,
        "width": 123,
        "left": -1142.763671875,
        "top": -471.24005126953125,
    },
    "Officer Outfit": {
        "height": 114,
        "width": 126,
        "left": -1145.8597412109375,
        "top": -474.1445617675781,
    },
    "Pilot's License": {
        "height": 113,
        "width": 124,
        "left": -1143.263671875,
        "top": -473.78411865234375,
    },
    "Policeman Officer": {
        "height": 113,
        "width": 130,
        "left": -1146.263671875,
        "top": -473.44476318359375,
    },
    "Rain Dear": {
        "height": 124,
        "width": 134,
        "left": -1145.8338623046875,
        "top": -477.5469055175781,
    },
    "Right Hand Man - Reborn": {
        "height": 191,
        "width": 92,
        "left": -1101.64208984375,
        "top": -558.7765502929688,
    },
    "Rock Solid": {
        "height": 129,
        "width": 148,
        "left": -1158.01318359375,
        "top": -487.5930480957031,
    },
    "Santa's Helper": {
        "height": 134,
        "width": 169,
        "left": -1168.4049072265625,
        "top": -487.8922119140625,
    },
    "Scientific Theory": {
        "height": 112,
        "width": 129,
        "left": -1144.0001220703125,
        "top": -471.53753662109375,
    },
    "Sneaky": {
        "height": 91,
        "width": 166,
        "left": -1166.263671875,
        "top": -469.5472106933594,
    },
    "Snowmate skin": {
        "height": 146,
        "width": 221,
        "left": -1193.794677734375,
        "top": -497.6346740722656,
    },
    "Sports Team BLUE": {
        "height": 83,
        "width": 123,
        "left": -1140.619140625,
        "top": -469.60382080078125,
    },
    "Sports Team RED": {
        "height": 83,
        "width": 123,
        "left": -1140.619140625,
        "top": -469.60382080078125,
    },
    "Suited Up": {
        "height": 114,
        "width": 123,
        "left": -1140.2735595703125,
        "top": -473.0409240722656,
    },
    "The Fishmonger": {
        "height": 126,
        "width": 129,
        "left": -1141.3076171875,
        "top": -478.7189636230469,
    },
    "The Nutcracker": {
        "height": 120,
        "width": 137,
        "left": -1146.70458984375,
        "top": -479.33245849609375,
    },
    "Toppat Skirt": {
        "height": 114,
        "width": 122,
        "left": -1141.001220703125,
        "top": -472.701171875,
    },
    "Toppat Uniform": {
        "height": 121,
        "width": 128,
        "left": -1145.8338623046875,
        "top": -475.99993896484375,
    },
    "Underminer": {
        "height": 121,
        "width": 124,
        "left": -1142.0006103515625,
        "top": -479.23297119140625,
    },
    "Unearthed Wonders": {
        "height": 115,
        "width": 126,
        "left": -1141.001220703125,
        "top": -473.9871826171875,
    },
    "Vested Interest": {
        "height": 119,
        "width": 128,
        "left": -1145.9443359375,
        "top": -470.4541320800781,
    },
    "Vi's Clothes": {
        "height": 126,
        "width": 130,
        "left": -1145.001220703125,
        "top": -478.150634765625,
    },
    "Whimsy Witch": {
        "height": 148,
        "width": 178,
        "left": -1175.059814453125,
        "top": -507.4597473144531,
    },
    "Your Boughs so Green": {
        "height": 120,
        "width": 192,
        "left": -1180.3341064453125,
        "top": -479.383056640625,
    },
}
Pets = {
    "Squig": {
        "height": 144,
        "width": 106,
        "left": -1201.500732421875,
        "top": -464,
    },
    "Bedcrab": {
        "height": 78,
        "width": 107,
        "left": -1197,
        "top": -417.4201965332031,
    },
    "Headslug pet": {
        "height": 110,
        "width": 94,
        "left": -1191.000244140625,
        "top": -445.0894470214844,
    },
    "UFO": {
        "height": 85,
        "width": 146,
        "left": -1217.5,
        "top": -440,
    },
    "Doggy": {
        "height": 103,
        "width": 121,
        "left": -1203.5,
        "top": -432.36474609375,
    },
    "Hampton": {
        "height": 119,
        "width": 119,
        "left": -1202.559814453125,
        "top": -448.097412109375,
    },
    "Mini Crewmate pet": {
        "height": 111,
        "width": 91,
        "left": -1188.6990966796875,
        "top": -440.01104736328125,
    },
    "Ro-Bot": {
        "height": 125,
        "width": 81,
        "left": -1177,
        "top": -454,
    },
    "H. Stickmin": {
        "height": 125,
        "width": 51,
        "left": -1170.52880859375,
        "top": -450.4597473144531,
    },
    "E. Rose": {
        "height": 129,
        "width": 58,
        "left": -1168,
        "top": -454,
    },
    "Glitch Pet": {
        "height": 56,
        "width": 47,
        "left": -1165,
        "top": -417.2100830078125,
    },
    "Bushfriend": {
        "height": 105,
        "width": 158,
        "left": -1217.5,
        "top": -438.45587158203125,
    },
    "Magmate": {
        "height": 112,
        "width": 146,
        "left": -1226,
        "top": -439.9701232910156,
    },
    "Snowball": {
        "height": 101,
        "width": 90,
        "left": -1180,
        "top": -443.5429382324219,
    },
    "Charles Chopper": {
        "height": 105,
        "width": 158,
        "left": -1217.5,
        "top": -438.45587158203125,
    },
    "Toppat Chopper": {
        "height": 84,
        "width": 138,
        "left": -1207.9195556640625,
        "top": -418.2156066894531,
    },
    "Heimerdinger's Poro": {
        "height": 117,
        "width": 116,
        "left": -1203,
        "top": -444.28289794921875,
    },
    "Frankendog": {
        "height": 103,
        "width": 126,
        "left": -1206,
        "top": -432.36474609375,
    },
    "Deitied Guy": {
        "height": 141,
        "width": 94,
        "left": -1192.366943359375,
        "top": -464.478759765625,
    },
    "Clank pet": {
        "height": 149,
        "width": 83,
        "left": -1177,
        "top": -477.478759765625,
    },
}
Visors = {
    "A Beard": {
        "height": 92,
        "width": 98,
        "left": -1103.00146484375,
        "top": -494.49920654296875,
    },
    "A n g e r y": {
        "height": 37,
        "width": 80,
        "left": -1098.1473388671875,
        "top": -542.3524169921875,
    },
    "Among Us Cracked 2021": {
        "height": 33,
        "width": 59,
        "left": -1084.8819580078125,
        "top": -512.1499633789062,
    },
    # "Blocks Toxics": {
    #     "height": 105,
    #     "width": 151,
    #     "left": -1142.0394287109375,
    #     "top": -549.4515380859375,
    # },
    "Bombastic": {
        "height": 35,
        "width": 54,
        "left": -1084.65185546875,
        "top": -506.96820068359375,
    },
    "Carrot Nose": {
        "height": 41,
        "width": 82,
        "left": -1068.0726318359375,
        "top": -505.01397705078125,
    },
    "Clownin' Around": {
        "height": 37,
        "width": 38,
        "left": -1068.0009765625,
        "top": -500.0433044433594,
    },
    "Crack-a-stache": {
        "height": 33,
        "width": 112,
        "left": -1112.096435546875,
        "top": -492.7366027832031,
    },
    "Dadgum": {
        "height": 34,
        "width": 86,
        "left": -1052.3411865234375,
        "top": -486.615478515625,
    },
    "Dig Down": {
        "height": 54,
        "width": 135,
        "left": -1141.3663330078125,
        "top": -528,
    },
    "Dot dot dot": {
        "height": 14,
        "width": 51,
        "left": -1080.0003662109375,
        "top": -498.4666442871094,
    },
    "Double Monocles": {
        "height": 73,
        "width": 87,
        "left": -1093.2928466796875,
        "top": -515.7996826171875,
    },
    "Galeforce Whiskers": {
        "height": 99,
        "width": 99,
        "left": -1102.936279296875,
        "top": -500.99993896484375,
    },
    "Ghostly Moustache": {
        "height": 87,
        "width": 117,
        "left": -1112.1695556640625,
        "top": -494.9998779296875,
    },
    "Got My Eye on You": {
        "height": 98,
        "width": 110,
        "left": -1113.4007568359375,
        "top": -557.603759765625,
    },
    # "Great Goalie": {
    #     "height": 108,
    #     "width": 122,
    #     "left": -1137.0003662109375,
    #     "top": -554.9999389648438,
    # },
    # "HAPPY NEW YEAR - 2021": {
    #     "height": 77,
    #     "width": 176,
    #     "left": -1158.646240234375,
    #     "top": -550.0791625976562,
    # },
    "Happeh": {
        "height": 44,
        "width": 59,
        "left": -1086.4564208984375,
        "top": -530.9453125,
    },
    "Heimerdinger's Moustache": {
        "height": 85,
        "width": 108,
        "left": -1112.3724365234375,
        "top": -532.6825561523438,
    },
    "Helmelted": {
        "height": 56,
        "width": 73,
        "left": -1106,
        "top": -535,
    },
    "Hit the Slopes": {
        "height": 63,
        "width": 148,
        "left": -1154.00048828125,
        "top": -531.0186157226562,
    },
    "Icicle Tears": {
        "height": 71,
        "width": 51,
        "left": -1098.1463623046875,
        "top": -480.2265625,
    },
    "Jinx's Goggles": {
        "height": 57,
        "width": 138,
        "left": -1140.7410888671875,
        "top": -527.0540771484375,
    },
    "Krieghaus": {
        "height": 14,
        "width": 59,
        "left": -1082.1063232421875,
        "top": -489.7245178222656,
    },
    "Lollipop": {
        "height": 52,
        "width": 74,
        "left": -1052.000732421875,
        "top": -479.7521667480469,
    },
    "Masque'd Up blue": {
        "height": 113,
        "width": 169,
        "left": -1151.0177001953125,
        "top": -560.7263793945312,
    },
    "Mr. G": {
        "height": 26,
        "width": 59,
        "left": -1083.5606689453125,
        "top": -490.47845458984375,
    },
    # "My Name Geoff": {
    #     "height": 136,
    #     "width": 146,
    #     "left": -1153.000732421875,
    #     "top": -573.210205078125,
    # },
    "Note 2 Self": {
        "height": 64,
        "width": 87,
        "left": -1087.0728759765625,
        "top": -526.9993286132812,
    },
    "Oh You": {
        "height": 23,
        "width": 92,
        "left": -1107,
        "top": -490.1771240234375,
    },
    "Blue Passcard": {
        "height": 58,
        "width": 85,
        "left": -1090.5,
        "top": -522.9835205078125,
    },
    "Patched Eye": {
        "height": 75,
        "width": 113,
        "left": -1142.9365234375,
        "top": -534.0790405273438,
    },
    "Pierced": {
        "height": 26,
        "width": 28,
        "left": -1043,
        "top": -529,
    },
    "Plagued mask": {
        "height": 94,
        "width": 132,
        "left": -1105.738037109375,
        "top": -541.9996948242188,
    },
    "Reginald Stache": {
        "height": 46,
        "width": 112,
        "left": -1109.3851318359375,
        "top": -500.5,
    },
    "Riding Shotgun": {
        "height": 48,
        "width": 103,
        "left": -1111.949462890625,
        "top": -494.9996643066406,
    },
    "Right Hand Stache": {
        "height": 93,
        "width": 132,
        "left": -1122.6395263671875,
        "top": -500.4997253417969,
    },
    "Safe Not Sorry": {
        "height": 69,
        "width": 134,
        "left": -1141.7451171875,
        "top": -529.4996948242188,
    },
    "Safety First": {
        "height": 62,
        "width": 143,
        "left": -1143.3289794921875,
        "top": -525.9996948242188,
    },
    "Santa's Beard": {
        "height": 93,
        "width": 112,
        "left": -1115.00048828125,
        "top": -504.6495361328125,
    },
    "Scarred": {
        "height": 34,
        "width": 32,
        "left": -1086.7838134765625,
        "top": -506.85308837890625,
    },
    "Shades": {
        "height": 48,
        "width": 134,
        "left": -1145.1436767578125,
        "top": -520.8534545898438,
    },
    "Shop Here": {
        "height": 40,
        "width": 124,
        "left": -1133.7869873046875,
        "top": -519.240966796875,
    },
    "Spectacles": {
        "height": 35,
        "width": 103,
        "left": -1113.0711669921875,
        "top": -510.39849853515625,
    },
    "That's a Wrap": {
        "height": 68,
        "width": 93,
        "left": -1104.5723876953125,
        "top": -531.1813354492188,
    },
    "Tiny Specs": {
        "height": 29,
        "width": 90,
        "left": -1109.50439453125,
        "top": -509.3038024902344,
    },
    "Wash Me": {
        "height": 39,
        "width": 62,
        "left": -1094.83740234375,
        "top": -508.3755187988281,
    },
    "Wurm": {
        "height": 39,
        "width": 66,
        "left": -1088.00146484375,
        "top": -509.999267578125,
    },
}
# bg = ["bg1.png", "bg4.png", "bg3.png"]
# bg = ["bg4.png", "bg1.png", "bg6.png", "bg7.png", "bg3.png", "bg9.png"]
bg = [
    # "21.png",
    # "22.png",
    # "23.png",
    # "24.png",
    # "25.png",
    # "26.png",
    # "27.png",
    # "28.png",
    "transparent_image.png",
    "bg4.png",
    # "7.png",
    # "8.png",
    # "9.png",
    # "10.png",
]
cx = -1265.5
cy = -661.62
x = -1166
y = -554
# Nameplates = ['Above the Clouds.png', 'Airship Hull.png', 'Airship Toppat.png', 'Backyard.png', 'By The Chimney with Care.png', 'C4 Plate.png', 'Candy Time.png', 'Colors of Polus.png', 'Diamonds!.png', 'Dig2China.png', 'Emeralds!.png', 'Ghosts.png', 'Greenery.png', 'Ground Polus.png', 'Hive got to do Weapons.png', 'Jack-o-Pumkpin.png', 'Lavaly.png', 'Polus Horizon.png', 'Polus Planet.png', 'Rubies!.png', 'SPORTS.png', 'Sandstone.png', 'SimSong Stan.png', 'Snow is Glistening.png', 'Snowmates of Polus.png', 'Snowy Lands.png', 'Specimen blue.png', 'Spooky Woods.png', 'The Greatest Nameplate.png', 'The Sky Below.png', 'The Stars are Brightly Shining.png', 'The Vault Above.png', "Today's Menu - Pizza Juice.png", 'Trees.png', 'Whose Vine Is It Anyway?.png', 'Wood you look at that.png']
# Cosmicubes = ['MIRA Cosmicube cover.png', 'Polus Cosmicube cover.png', 'Airship Cosmicube cover.png', 'Arcane Cosmicube cover.png', 'Treat Cosmicube cover.png', 'Trick Cosmicube cover.png', 'Innersloth Cosmicube cover.png', 'Snowflake Cosmicube cover.png', 'Snowbean Cosmicube cover.png']
Colors = [
    "Red.png",
    "Blue.png",
    "Green.png",
    "Pink.png",
    "Orange.png",
    "Yellow.png",
    "Black.png",
    "White.png",
    "Purple.png",
    "Brown.png",
    "Cyan.png",
    "Lime.png",
    "Maroon.png",
    "Rose.png",
    "Banana.png",
    "Gray.png",
    "Tan.png",
    "Coral.png",
]
# Colors = ["Red.png"]
count = 0
print(len(Colors))
print(len(Hats))
print(len(Visors))
print(len(Skins))
print(len(Pets))
errorList = []
# for b in bg:
#     for c in Colors:
#         for s in Skins:
#             for v in Visors:
#                 for h in Hats:
#                     for p in Pets:
#                         try:
#                             base = Image.open(b)
#                             color = Image.open(f"Colors/{c}")
#                             skin = Image.open(f"Skins/{s}.png")
#                             hat = Image.open(f"Hats/{h}.png")
#                             pet = Image.open(f"Pets/{p}.png")
#                             visor = Image.open(f"Visors/{v}.png")
#                             # print(color.getdata)
#                             offset_color=((int(x-cx)),(int(y-cy)))
#                             offset_skin = ((int(x-Skins[s]["left"])),(int(y-Skins[s]["top"])))
#                             offset_hat = ((int(x-Hats[h]["left"])),(int(y-Hats[h]["top"])))
#                             offset_visor = ((int(x-Visors[v]["left"])),(int(y-Visors[v]["top"])))
#                             offset_pet = ((int(x-Pets[p]["left"])),(int(y-Pets[p]["top"])))
#                             base.paste(color, (99,107), mask=color)
#                             base.paste(skin,offset_skin, mask=skin)
#                             base.paste(visor,offset_visor, mask=visor)
#                             base.paste(hat,offset_hat, mask=hat)
#                             base.paste(pet,offset_pet, mask=pet)
#                             base.save(f"Test1/{count}.png")
#                             print(count)
#                         except:
#                             errorList.append(v+c+s+v+h+p)
#                             print(v,c,s,v,h,p)
#                         count= count+1
#                         break
#                     break
#                 break
#             break
#         break
#     break
Alist = []
i = 0
# for i in Hats:
#     try:
#         if Hats[i]["bool"] == 1 or Hats[i]["bool"] == 2:
#             Alist.append(i)
#     except:
#         Hats[i]["bool"] = 0
# print(Alist)
# print(Hats)
# while len(Alist) <= 100:
b = random.choice(bg)
c = random.choice(Colors)
s = random.choice(list(Skins.keys()))
h = random.choice(list(Hats.keys()))
p = random.choice(list(Pets.keys()))
v = random.choice(list(Visors.keys()))
qwe = v + c + s + v + h + p
if qwe not in Alist:
    try:

        base = Image.open(f"Colors/{c}")
        skin = Image.open(f"Skins/{s}.png")
        hat = Image.open(f"Hats/{h}.png")
        pet = Image.open(f"Pets/{p}.png")
        visor = Image.open(f"Visors/{v}.png")
        # print(color.getdata)
        offset_color = ((-1 * int(x - cx)), (-1 * int(y - cy)))
        offset_skin = (
            (-1 * int(x - Skins[s]["left"])),
            (-1 * int(y - Skins[s]["top"])),
        )
        offset_hat = (
            (-1 * int(x - Hats[h]["left"])),
            (-1 * int(y - Hats[h]["top"])),
        )
        offset_visor = (
            (-1 * int(x - Visors[v]["left"])),
            (-1 * int(y - Visors[v]["top"])),
        )
        offset_pet = (
            (-1 * int(x - Pets[p]["left"])),
            (-1 * int(y - Pets[p]["top"])),
        )
        if Hats[h]["bool"] == 1:
            base.paste(hat, offset_hat, mask=hat)
            # base.paste(color, (99, 107), mask=color)
            if v != "Patched Eye":
                base.paste(skin, offset_skin, mask=skin)
                if Hats[h]["bool"] != 2:
                    base.paste(visor, offset_visor, mask=visor)
            else:
                if Hats[h]["bool"] != 2:
                    base.paste(visor, offset_visor, mask=visor)
                base.paste(skin, offset_skin, mask=skin)
        else:
            # base.paste(color, (99, 107), mask=color)
            base.paste(skin, offset_skin, mask=skin)
            if v != "Patched Eye":
                base.paste(skin, offset_skin, mask=skin)
                if Hats[h]["bool"] != 2:
                    base.paste(visor, offset_visor, mask=visor)
            else:
                if Hats[h]["bool"] != 2:
                    base.paste(visor, offset_visor, mask=visor)
                base.paste(skin, offset_skin, mask=skin)
            base.paste(hat, offset_hat, mask=hat)
        base.paste(pet, offset_pet, mask=pet)
        base.save(f"Test1/{len(Alist)}.png")
        Alist.append(v + c + s + v + h + p)
        print(len(Alist))
        base.show()
    except:
        errorList.append(v + c + s + v + h + p)
        print(v, c, s, v, h, p)
print(i)

print(errorList)
# print(Alist)
# base.paste(img2, ((bg_w - color_w)//2 -15,20), mask=img2)

# # Displaying the image
# base.show()¸
# for i in Visor_cosmetics:
#     print(f'"{i.split(".png")[0]}" :  ' + " { \n\n }, ")
# print(len(Visor_cosmetics))
# for i in Colors:
#     img = Image.open(f"Colors/{i}")
#     # img = img.convert("RGBA")

#     pixdata = img.load()

#     # Clean the background noise, if color != white, then set to black.
#     for y in range(0,img.size[1]):
#         for x in range(0,img.size[0]):
#             if pixdata[x, y] == (55, 59, 60, 255):
#                 pixdata[x, y] = (0, 0, 0, 0)
#     img.save(f"Colors/{i}")
