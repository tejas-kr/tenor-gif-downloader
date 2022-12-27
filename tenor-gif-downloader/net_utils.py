import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import shutil

class InternetUtils:
    """ BS4 Utils for extracting gif links """

    def __init__(self, search_item: str):
        """
            Create LinkExtract object

            Args:
                search_item (str): Search key work in string format
        """
        self.link = "https://tenor.com/en-IN/search/%s-gifs"
        self.html = requests.get(self.link%search_item)
        self.soup = BeautifulSoup(self.html.text, "lxml")

    
    def get_all_img_tags(self) -> list:
        """
            Get all BS4 Tag objects

            Returns:
                img_tag_list (list): List of bs4 IMG Tag objects
        """
        all_img = self.soup.find_all("img")
        gif_srcs = [each_img['src'] for each_img in all_img if each_img['src'][-4:] == ".gif" and each_img['src'].split('/')[3][-1] == "M"]
        final_gifs = []
        for each_gif in gif_srcs:
            temp_gif = each_gif.split('/')
            temp_gif[3] = temp_gif[3][:-1] + "C"
            final_gifs.append('/'.join(temp_gif))

        return final_gifs


    def files_downloader(self, number_of_items: int, folder_path: str, final_gifs: list):
        """
            Downloads the specified number of files to destination folder
        """

        if os.path.exists(folder_path):
            for each_gif in final_gifs[:number_of_items]:
                img_resp = requests.get(each_gif, stream=True)
                if img_resp.status_code == 200:
                    with open(f"{folder_path}/{ str(datetime.now().timestamp()) + each_gif.split('/')[-1] }", "wb") as file_p:
                        img_resp.raw.decode_content = True
                        shutil.copyfileobj(img_resp.raw, file_p)
        else:
            raise ValueError("Folder Path Error")