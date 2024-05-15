import pandas
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

with open("graph.html") as f:
  page = f.read()

soup = BeautifulSoup(page, "html")

years = []
for year in soup.find_all("g", class_="highcharts-xaxis-labels")[0].children:
  print(year.text)
  years.append(int(year.text))

print(years)

sales = []
for sale in soup.find_all("g", class_="highcharts-yaxis-labels")[0].children:
  print(sale.text)
  sales.append(int(sale.text))

print(sales)

# # the years are <text> tags underneath this <g> tag:
x_axis_html_class_name = "highcharts-xaxis-labels"

data_dictonary = {
  "year" : years,
  "sale" : sales
}

df = pandas.DataFrame(data_dictonary)
print(df)

df.plot(kind="bar", x = "year", y = "sale")
plt.show()