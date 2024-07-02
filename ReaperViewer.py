from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyfiglet
import time

# Function to save URLs to a file
def save_urls(urls):
    with open('urls.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

# Function to load URLs from a file
def load_urls():
    urls = []
    try:
        with open('urls.txt', 'r') as file:
            urls = file.read().splitlines()
    except FileNotFoundError:
        pass
    return urls

def choose_url(urls):
    print("Saved URLs:")
    for i, url in enumerate(urls, 1):
        print(f"{i}. {url}")
    print("A. Add a new URL")
    while True:
        print("")
        choice = input("Choose a number to use the corresponding URL or 'A' to add a new URL: ").strip().lower()
        if choice == 'a':
            new_url = input("Enter the new URL you want to bot and save it: ").strip()
            urls.append(new_url)
            save_urls(urls)
            return new_url
        else:
            try:
                index = int(choice) - 1
                if 0 <= index < len(urls):
                    return urls[index]
                else:
                    print("Invalid choice. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number or 'A'.")

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")  
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--window-size=1920,1080")
#chrome_options.add_argument("--headless")   

text = "Reaper Viewer V.7"



chosen_font = "slant"  # You can choose any font from the available fonts
ascii_art = pyfiglet.figlet_format(text, font=chosen_font)
print(ascii_art)
print("\n")

urls = load_urls()

#choice = str(input("Do you want to [1] save a new url or [2] use an existing saved one? Input 1 or 2"))
'''
if choice == 1: 
    urls = []
    urls.append(input("Enter the URL you want to bot and save it: ").strip())
    save_urls(urls)
if choice == 2:
    print(urls)
    print("Choose a saved URL:")
    chosen_url = choose_url(urls)
'''

if not urls:
    print("No saved URLs found.")
    urls = []
    urls.append(input("Enter the URL you want to bot and save it: ").strip())
    save_urls(urls)
    chosen_url = choose_url(urls)
else:
    print("Choose a saved URL or add a new one")
    print("")
    chosen_url = choose_url(urls)



#url = str(input("Enter the url you want to bot: "))




print("")
num1 = int(input("How many views do you want: "))
print("")
sleeptime = int(input("Input Interval Between Views (1 Minimum): "))
print("")
scroll = int(input("Do you want Reaper Bot to scroll on the page, scrolling will make it look more human which might effect viewage on some websites [1] Yes [2] No: "))
print("")
option2 = int(input("Do you want Reaper Bot to make the viewing window off screen? This might effect viewage [1] Yes [2] No: "))
if option2 == 1:
    chrome_options.add_argument("--window-position=-2000,2000")
print("")
option3 = int(input("Do you want Reaper Bot to make the viewing window automaticlly minimize? This might effect viewage [1] Yes [2] No: "))

for i in range(num1):

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    if option3 == 1:
        driver.minimize_window()
    driver.get(chosen_url)
    time.sleep(sleeptime)
    if scroll == 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    print("Bot View succeeded X" + str(i+1))

    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")

    driver.quit()


# Close the browser after all iterations


text2 = "Reaper Viewer Success"
ascii_art = pyfiglet.figlet_format(text2, font=chosen_font)
print(ascii_art)
print("\n")
print("Press Ctrl^C to quit")
time.sleep(999)
