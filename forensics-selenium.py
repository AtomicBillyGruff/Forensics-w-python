import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def get_loc_data():
    f = open(os.path.join(location_evidence_path, database_filename))
    latitute = []
    longitute = []
    # get positions 6 and 7 latitude:longitude
    for line in f:
        latitute.append(line.split("|")[5])
        longitute.append(line.split("|")[6])

    return latitute, longitute


def maps():
    # retrieve coordinate data
    coords = get_loc_data()
    lat = coords[0]
    long = coords[1]

    # Clean Data by Removing Index Column
    lat.remove(lat[0])
    long.remove(long[0])
    # print(len(lat), len(long))
    # print(lat[0], long[0])

    # check the len of each list so values correlate
    if len(lat) == len(long):
        # print('[+] data will be correlated')

        # OPEN GOOGLE MAPS
        ser = Service('./geckodriver')
        op = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=ser, options=op)
        driver.get("https://www.google.com/maps")

        for i in range(len(lat) + 1):
            for num in range(0, 90):
                driver.find_element(By.ID, 'searchboxinput').send_keys(Keys.BACKSPACE)

            driver.find_element(By.ID, 'searchboxinput').send_keys(Keys.DELETE)
            driver.find_element(By.ID, 'searchboxinput').send_keys(lat[i] + " " + long[i])
            driver.find_element(By.ID, 'searchboxinput').send_keys(Keys.ENTER)
            sleep(4)
            try:
                local_address = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div/div[1]/span[3]/span[3]').text
            except:
                local_address = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div/div[1]/span[3]/span[3]').text

            for num in range(0, 30):
                driver.find_element(By.ID, 'searchboxinput').send_keys(Keys.BACKSPACE)

            driver.find_element(By.ID, 'searchboxinput').send_keys(local_address)
            driver.find_element(By.ID, 'searchboxinput').send_keys(Keys.ENTER)
            sleep(6)
            # printing the name
            try:
                print(driver.find_element(By.XPATH,
                                          '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text)
            except:
                try:
                    print(driver.find_element(By.XPATH,
                                              '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text)
                except:
                    print(local_address)

            sleep(2)

    else:
        print('[-] Dataframe missing values')


if __name__ == "__main__":
    location_evidence_path = "/home/kali/forensics/evidence/location_evidence"
    database_filename = "CellLocation_filtered2.csv"
    maps()
