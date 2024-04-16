import pyautogui
import time
from PIL import Image


def screen_book_pages():
    print('Focus on the main screen')
    time.sleep(5)
    screenWidth, screenHeight = pyautogui.size()
    for i in range(10):
        filename = "./screenshots/" + str(i) + ".png"
        image = pyautogui.screenshot(region=(0,0, screenWidth / 2, screenHeight))
        print('Saving ' + filename)
        image.save(filename)
        print('Scrolling...')
        pyautogui.scroll(-1)


def create_pdf():
    images = [
        Image.open("./screenshots/" + str(i) + ".png")
        for i in range(10)
    ]
    pdf_path = "./book.pdf"
    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen_book_pages()
    create_pdf()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
