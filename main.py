from requests import get

def main():
    
    url = "https://finance.yahoo.com/gainers?count=50&offset=0"
    response = get(url)
    print(response.text[:500])






if __name__ == "__main__":
    main()
else: 
    print("Imported main.py")