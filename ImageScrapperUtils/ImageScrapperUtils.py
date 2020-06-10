from ImageScrapper.ImageScrapper import ImageScrapper
import os
from selenium import webdriver



class ImageScrapperUtils:


    def search_and_download(search_term: str, driver_path: str, target_folder='images', number_images=10):
        scraper_object = ImageScrapper
        # target_folder = os.path.join(target_path, '_'.join(
        #     search_term.lower().split(' ')))  # make the folder name inside images with the search string

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)  # make directory using the target path if it doesn't exist already

        with webdriver.Chrome(executable_path=driver_path) as wd:
            res = scraper_object.fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

        counter = 0
        for elem in res:
            scraper_object.persist_image(target_folder, elem, counter)
            counter += 1

    def list_only_jpg_files(self,target_folder):
        list_of_jpg_files = []
        for file in os.listdir(target_folder):
                list_of_jpg_files.append(file)

        return list_of_jpg_files