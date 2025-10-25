import re
import requests
from bs4 import BeautifulSoup


url = "https://fastly.picsum.photos/id/958/200/200.jpg?hmac=WdLUMERHKTLw-sP-eIf1-JlwdIT2ZY12zf4JbnQR_s8"

response = requests.get(url)
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")


pattern = re.compile(r"https?://.*(product).*\.jpg|https?://.*(product).*\.png", re.IGNORECASE)

product_imgs = []
for img_tag in soup.find_all("img", src=True):
    src = img_tag["src"]
    if pattern.search(src):
        product_imgs.append(src)

print("Product Image URLs found:\n")
for img_url in product_imgs:
    print(img_url)


if product_imgs:
    import io
    from PIL import Image

    first_img_url = product_imgs[0]
    img_data = requests.get(first_img_url).content
    image = Image.open(io.BytesIO(img_data))
    image.show()

