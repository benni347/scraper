"""
Author  Benni347@github.com
"""
# Misc Imports
import json
import datetime
import time
import random as rnd

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main:
    def __init__(self):
        self.url_list = ["https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8660502/","https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8646333/"]
        self.outfile = f"out-{datetime.datetime.now()}.json"

    def write_to_file(self, content):
        """
        This will write the json data to a file
        :type content: dict
        :param content: a dict with the content
        """
        json_object = json.dumps(content, indent=4)

        with open(self.outfile, "w") as out:
            out.write(json_object)

    def list_to_dict(self, list_param):
        it = iter(list_param)
        res_dct = dict(zip(it, it))
        return res_dct

    @staticmethod
    def flatten(list_param):
        """
        Flattens a list inside a list to a list
        From this post https://stackoverflow.com/a/952952/15410622
        :param list_param: a list which content is a list
        :return: a single list without a list inside.
        """
        return [item for sublist in list_param for item in sublist]

    def go_to_page(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        data_list = []
        for i, data in enumerate(self.url_list):
            driver.get(data)
            # find data
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "attributes")))
            for element in driver.find_elements(By.CLASS_NAME, "attributes"):
                data_list.append(element.text.split("\n"))
                print(datetime.datetime.now())

        driver.close()
        description = self.list_to_dict(self.flatten(data_list))
        self.write_to_file(description)
        print(data_list)



if __name__ == "__main__":
    main_class = Main()
    main_class.go_to_page()
