# Lesson 29
# https://www.youtube.com/watch?v=2Rf01wfbQLk&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=29

# we need a URL library:
import urllib.request

# download_jpg(url, file_path, file_name)
def download_image(url, file_path, file_name):
  # oncatenate:
  full_path = file_path + file_name + '.jpg'

  # now let's use the module
  urllib.request.urlretrieve(url, full_path)

url = input('Enter img URL to download:')
file_name = input('Enter file name to save as:')

# add the "/"
download_image(url, 'images/', file_name)
