import urllib.request
def get_page(url):
    page = urllib.request(url)
    page = page.content
    page = page.decode('utf-8')
    return page
print(get_page("https://nfulist.herokuapp.com/?semester=1091&courseno=0776"))