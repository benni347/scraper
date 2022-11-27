#!/usr/bin/env python3
"""
This is the file to execute
Author  Benni347@github.com
"""
import datetime

# Misc Imports
import json

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Main:
    def __init__(self):
        self.url_list = [
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8660502/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8646333/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8648002/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8630787/",
            "https://www.troostwijkauctions.com/de/whiteboard-mit-schiene/03-43350-33214-8649744/",
            "https://www.troostwijkauctions.com/de/whiteboard-mit-schiene/03-43350-33214-8649753/",
            "https://www.troostwijkauctions.com/de/whiteboard-mit-schiene/03-43350-33214-8649761/",
            "https://www.troostwijkauctions.com/de/whiteboard-mit-schiene/03-43350-33214-8649762/",
            "https://www.troostwijkauctions.com/de/whiteboard-mit-schiene/03-43350-33214-8657044/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8654018/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8654092/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8654198/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8654207/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8654211/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8660458/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8660502/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8677618/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8630973/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8646320/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8646333/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8646353/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8646363/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8648002/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8648016/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8648019/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8649295/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8649322/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8649368/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8659580/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8659586/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8659600/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8672608/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8672638/",
            "https://www.troostwijkauctions.com/de/whiteboard/03-43350-33214-8672685/",
        ]
        self.outfile = f"out-{datetime.datetime.now()}.json"

    def write_to_file(self, content):
        """
        This will write the json data to a file
        :type content: dict
        :param content: a dict with the content
        """
        json_object = json.dumps(content, indent=4)

        with open(self.outfile, "w", encoding="UTF-8") as out:
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
        for _, data in enumerate(self.url_list):
            driver.get(data)
            # find data
            wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "attributes")))
            for element in driver.find_elements(By.CLASS_NAME, "attributes"):
                split_element = element.text.split("\n")
                element_dict = self.list_to_dict(split_element)
                element_dict["url"] = data
                data_list.append(element_dict)
                print(datetime.datetime.now())

        driver.close()
        self.write_to_file(data_list)
        print(data_list)


if __name__ == "__main__":
    main_class = Main()
    main_class.go_to_page()
