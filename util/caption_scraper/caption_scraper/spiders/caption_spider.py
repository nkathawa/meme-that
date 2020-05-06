import scrapy
from lxml import html
import json
import os
import urllib.parse

class CaptionSpider(scrapy.Spider):
    name = "Caption"
    start_urls = []
    with open("../../meme_scraper/json_memes.json") as json_file:
        data = json.load(json_file)
    for key in data:
        url = "https://imgflip.com/meme/" + data[key]["name"].replace(' ', '-')
        start_urls.append(url)
        
    def parse(self, response):
        if not response:
                self.log("Failed to fetch page")
                return None
        url_parts = urllib.parse.urlparse(str(response.url))
        path_parts = url_parts[2].rpartition('/')
        title = path_parts[2].replace('-', ' ')
        #title = str(response.url).rsplit('/', 1)[-1].replace('-', ' ')
        parser = html.fromstring(response.text)
        # Get results from the first page
        search_results = parser.xpath("//img[@class='base-img']")
        img_id = '0'
        for caption in search_results:
            temp_title = caption.xpath("./@alt")[0]
            title_arr = temp_title.split('|')
            #title = title[0:len(title)-1]
            caption = title_arr[1]
            # Find what image id we are adding the captions to
            if img_id == '0':
                for name, img in self.data.items():
                    name_img = img['name']
                    if name_img == title:
                        img_id = str(name)
                        break
            if img_id != '0' and 'caption' not in self.data[img_id].keys():
                self.data[img_id]['caption'] = []
            elif img_id != '0':
                self.data[img_id]['caption'].append(caption)

        json_dict = {}
        if img_id != '0':
            if 'count' not in self.data[img_id].keys():
                self.data[img_id]['caption_count'] = len(self.data[img_id]['caption'])
            else:
                self.data[img_id]['caption_count'] = len(self.data[img_id]['caption'])
            json_dict = {img_id: self.data[img_id]}

        # Follows the link to the page, makes sure you get all of the properties
        next_page = parser.xpath(".//div[@class='pager']//a[@class='pager-next l but']/@href")
        next_page_url = "https://imgflip.com" + next_page[0] if next_page else None
        
        if next_page_url:
            page_number = next_page_url.split('=')[1]
            if float(page_number) < 500.0:
                yield scrapy.Request(next_page_url, callback=self.parse)
            else:
                yield json_dict
        else:
            yield json_dict
        