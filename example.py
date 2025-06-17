import devdraft_sdk
from devdraft_sdk.configuration import Configuration
from devdraft_sdk.api_client import ApiClient
from devdraft_sdk.api.api_health_api import APIHealthApi

def main():
    # Configure API client
    configuration = Configuration()
    configuration.host = "https://admin.devdraft.ai"  # Set the correct API address
    configuration.api_key['x-client-key'] = 'YOUR_CLIENT_KEY'  # Replace with your actual client key
    configuration.api_key['x-client-secret'] = 'YOUR_CLIENT_SECRET'  # Replace with your actual client secret

    # Create API client instance
    api_client = ApiClient(configuration)

    try:
        # Initialize the health check API
        health_api = APIHealthApi(api_client)
        
        # Make a health check request
        health_response = health_api.get_health()
        print("API Health Status:", health_response)
        
        # Example of getting exchange rates
        exchange_rates_api = devdraft_sdk.api.exchange_rates_api.ExchangeRatesApi(api_client)
        rates = exchange_rates_api.get_exchange_rates()
        print("\nExchange Rates:", rates)

    except devdraft_sdk.exceptions.ApiException as e:
        print("API Error:", e)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main() 