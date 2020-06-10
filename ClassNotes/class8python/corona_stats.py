# selenium
# https://selenium-python.readthedocs.io/

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.worldometers.info/coronavirus/")

# total_row_world odd

cases = driver.find_element_by_class_name("total_row_world.odd").text.split(' ')
#print(cases)
total_world = cases[1]
total_new_world = cases[2][1:]

total_world_deaths = cases[3]
total_new_world_deaths = cases[4][1:]

print("Total Cases Worldwide: " + total_world)
print("New Cases Worldwide Today: " + total_new_world)
print("Total Deaths Worldwide: " + total_world_deaths)
print("New Deaths Worldwide Today: " + total_new_world_deaths)

print()

driver.get("https://www.worldometers.info/coronavirus/country/us")

usa_cases = driver.find_element_by_class_name("total_row_usa.odd").text.split(' ')

total_usa = usa_cases[2]
total_new_usa = usa_cases[3][1:]

total_usa_deaths = usa_cases[4]
total_new_usa_deaths = usa_cases[5][1:]

print("Total Cases in the US: " + total_usa)
print("New Cases in the US Today: " + total_new_usa)
print("Total Deaths in the US: " + total_usa_deaths)
print("New Deaths in the US Today: " + total_new_usa_deaths)

