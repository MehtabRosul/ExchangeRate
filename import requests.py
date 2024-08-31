import requests

# Function to fetch exchange rates
def get_exchange_rate(from_currency, to_currency):
    base_url = "https://open.er-api.com/v6/latest/"
    
    response = requests.get(base_url + from_currency)
    data = response.json()

    if response.status_code != 200 or data['result'] != 'success':
        raise Exception(f"Error fetching data: {data.get('error-type', 'Unknown error')}")

    rate = data['rates'].get(to_currency)
    if rate is None:
        raise Exception(f"Conversion rate not found for {to_currency}")
    
    return rate

# Function to perform the currency conversion
def convert_currency(from_currency, to_currency, amount):
    try:
        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount
    except Exception as e:
        print(e)
        return None

# Main function to handle user input and output
def main():
    print("Welcome to the Currency Converter")

    from_currency = input("Enter base currency (e.g., USD): ").upper()
    to_currency = input("Enter target currency (e.g., EUR): ").upper()
    amount = float(input("Enter amount to convert: "))

    converted_amount = convert_currency(from_currency, to_currency, amount)

    if converted_amount:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
