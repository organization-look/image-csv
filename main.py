import requests
import bs4
import re

header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36 '
}

url = 'https://store.steampowered.com/explore/new/'
r = requests.get(url, header)
soup = bs4.BeautifulSoup(r.text,"html.parser")
rilis_baru = soup.find('div',{'id':'tab_newreleases_content'})
rilis_barus = soup.findAll('a', {'class':'tab_item'})
for barusan in rilis_barus:
    image = barusan.find('img',{'class':'tab_item_cap_img'})['src']
    title = barusan.find('div',{'class':'tab_item_name'}).text
    respon = requests.get(image,header,stream=True)
    filename= image.split("/")[-1].split("?")[0]
    ext = filename[-4:]
    if respon.ok:
        with open('images'+ re.sub(r'(?u)[^-\w.]','_',title) + ext,'wb') as a:
            a.write(respon.content)



