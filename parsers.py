"""
for item in ["10","abc","3.5"]:
    try:
        print(float(item))
    except ValueError:
        print("hata:",item)
        """


def main():
    print(parse_price("$1,234.50"))
    print(parse_price("42"))
    try:
        parse_price("abc")
    except ValueError as error:
        print(error)


def parse_price(text):

    cleaned = text.strip().lstrip("$").replace(",","")
    try:
        price = float(cleaned)
    except ValueError:
        raise ValueError("invalid price")
    return price   
    
main()

