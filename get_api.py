#import packages
import nasdaqdatalink
import json
import urllib.request


def get_data():
    nasdaqdatalink.ApiConfig.api_key = "FGvUmzE871ZRTSCexcb-" # used nasdaq unique api key 
    countries = ["USA", "NIC", "MDA", "JOR"] #countries list 
    data = [] # get nasdaqdata of the coutries mentionded
    get_burger = [] # get countries flag details, currency and common name here
    for country in countries:
        country_info = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{country}', start_date='2022-01-31', end_date='2022-07-30')
        flagurl = f'https://restcountries.com/v3.1/alpha/{country}' # country details
        request = urllib.request.urlopen(flagurl) 
        result = json.loads(request.read())
        country = {
            "country": country,
            "local_price": country_info.iloc[0, 0],
            "dollar_ex": country_info.iloc[0, 1],
            "dollar_price": country_info.iloc[0, 2],
            "dollar_ppp": country_info.iloc[0, 3],
            "dollar_valuation": country_info.iloc[0, 4],
            "dollar_adj_valuation": country_info.iloc[0, 5],
            "flagurl": result[0]["flags"]["png"],
            "countryname": result[0]["name"]["common"],
            "currencydetail": result[0]["currencies"],
        }
        data.append(country) # info from nasdaq is appended here
        number = float(round(country_info.iloc[0, 3], 2)) #numbers of burger in each country
        burger = str((int(number))) + " 🍔" 
        get_burger.append(burger)
    return data, get_burger
