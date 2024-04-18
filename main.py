import pyautogui
import time
from PIL import Image
import hashlib
from pathlib import Path
import shutil

def screen_book_pages():
    Path("./screenshots").mkdir(parents=True, exist_ok=True)
    print('Focus on the main screen')
    time.sleep(5)
    screenWidth, screenHeight = pyautogui.size()
    previousHash = ''
    i = 0
    files = []
    while True:
        filename = "./screenshots/" + str(i) + ".png"
        image = pyautogui.screenshot(region=(0,0, screenWidth / 2, screenHeight))
        hash = hashlib.md5(image.tobytes()).hexdigest()

        if previousHash == hash:
            print('Complete')
            break

        print('Saving ' + filename)
        image.save(filename)
        files.append(filename)

        print('Hash ' + hash)
        previousHash = hash

        i += 1

        print('Scrolling...')
        pyautogui.scroll(-1)

    create_pdf(files)
    shutil.rmtree('./screenshots')


def create_pdf(files):
    images = [
        Image.open(i)
        for i in files
    ]
    pdf_path = "./book.pdf"
    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen_book_pages()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
