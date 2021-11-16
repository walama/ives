import requests
# from bs4 import BeautifulSoup

def main():
    page = requests.get("https://shop.bigskyresort.com/s/winter-tickets-and-passes/lift-tickets/c/lift-ticket")
    # soup = BeautifulSoup(page.content, 'html.parser')
    with open("content.html", "wb") as f:
        f.write(page.content)

if __name__ == "__main__":
    main()