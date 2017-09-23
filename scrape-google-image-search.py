# Baserad på denna: https://gist.github.com/kekeblom/204a609ee295c81c3cc202ecbe68752c

# Copyright (c) 2016 Kenneth Blomqvist
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

############################
## How to use
############################
# To scrape images run e.g. python scrape.py <Search keyword> --count 200 --label <label>
# The images will be saved in a subfolder called "images" and it will contain another folder called whatever
# you passed in as the label parameter. This enables you to easily scrape a bunch of different searches while still
# keeping the images organized. The image files will be saved as jpeg images and named by the image contents sha1 hash.

import os
import re
import time
import argparse
import requests
import io
import hashlib
import itertools
import base64
from PIL import Image
from multiprocessing import Pool
from selenium import webdriver

argument_parser = argparse.ArgumentParser(description='Download images using google image search')
argument_parser.add_argument('query', metavar='query', type=str, help='The query to download images from')
argument_parser.add_argument('--count', metavar='count', default=100, type=int, help='How many images to fetch')
argument_parser.add_argument('--label', metavar='label', type=str, help="The directory in which to store the images (images/<label>)", required=True)


def ensure_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)

def largest_file(dir_path):
    def parse_num(filename):
        match = re.search('\d+', filename)
        if match:
            return int(match.group(0))

    files = os.listdir(dir_path)
    if len(files) != 0:
        return max(filter(lambda x: x, map(parse_num, files)))
    else:
        return 0

def fetch_image_data(query, images_to_download):
    image_data = []

    search_url = "https://www.google.se/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    #browser = webdriver.Firefox()
    browser.get(search_url.format(q=query))
    #def scroll_to_bottom():
    #    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #    time.sleep(2)

    print("Found:", len(image_data), "images")
    #scroll_to_bottom()

    images = browser.find_elements_by_css_selector("img.rg_ic")
    #number = len(images)
    #print(number) #100 bilder
    for img in images:
        image_data.append(img.get_attribute('src'))
    #delta = len(image_data) - image_count
    #image_count = len(image_data)



        #fetch_more_button = browser.find_element_by_css_selector(".ksb._kvc")
        #if fetch_more_button:
        #    browser.execute_script("document.querySelector('.ksb._kvc').click();")
        #    scroll_to_bottom()

    #browser.quit()
    #print(image_data)
    #image_data=list(image_data)
    #print(image_data[0])
    return image_data[0]



if __name__ == '__main__':
    args = argument_parser.parse_args()

    #ensure_directory('./images/')

    query_directory = './images/'
    ensure_directory(query_directory)
    browser = webdriver.Firefox()
    image_url = fetch_image_data(args.query, args.count)
    browser.quit()


    values=[query_directory,image_url]
    #values = [item for item in zip(itertools.cycle([query_directory]), image_url)]
    #print (values)

    try:
        image_content = requests.get(image_url).content
    except requests.exceptions.InvalidSchema:
        # image is probably base64 encoded
        image_data = re.sub('^data:image/.+;base64,', '', image_url)
        image_content = base64.b64decode(image_data)
    except Exception as e:
        print("could not read", e, image_src)
        #return False



    #print (image_content)
    #print("image count", len(image_data))
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert('RGB')
    #resized = image.resize(size)
    with open(query_directory + args.label + '_' + args.query + ".jpg", 'wb')  as f:
        image.save(f, "JPEG", quality=85)

    #pool = Pool(12)
    #results = pool.map(persist_image, values)
    #print("Images downloaded: ", len([r for r in results if r]))
