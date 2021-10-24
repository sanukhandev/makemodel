# ++++++++++++++++++++++++++++++++++++++++++++
#
# Author: Sanu Khan
# Scrapping web to get make models list
# various operations
#
# ++++++++++++++++++++++++++++++++++++++++++++


# Essential imports
import cloudscraper
from bs4 import BeautifulSoup
import xlsxwriter

#Declarations
scraper = cloudscraper.create_scraper()
url = "https://oman.yallamotor.com/car_makes"
workbook = xlsxwriter.Workbook('cars.xlsx')
worksheet = workbook.add_worksheet()

# Opening Workbook and start writing data 
#Headers
worksheet.write(0, 0, "Make")
worksheet.write(0, 1, "Model")

# Api call to fetch Models
makeOption = BeautifulSoup(scraper.get(url+"/find_all_makes?force_locale=en").text, "html.parser").findAll("option")
row = 1

# Loop through the makes name and fetch Models
for make in makeOption:
    # Getting Models based on makes name 
    modeOptions = BeautifulSoup(scraper.get(url+"/find_all_models?id="+make['value']+"&force_locale=en&all=true").text, "html.parser").findAll("option")
    for model in modeOptions:
        print(make.text,'->', model.text)
        # Writing data to sheet 
        worksheet.write(row, 0, make.text)
        worksheet.write(row, 1, model.text)
        row +=1

workbook.close()
    
