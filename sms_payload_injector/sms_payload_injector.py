import requests
from twilio.rest import Client
from time import sleep
import sys
from colorama import Fore, init

# Initialize colorama for colored terminal output
init()

# Banner
def display_banner():
    banner = f"""
{Fore.RED} 
  _____ __  __ _______ 
 |  ___|  \\/  |__   __|
 | |___| \\  / |  | |   
 |  ___| |\\/| |  | |   
 | |___| |  | |  | |   
 |_____|_|  |_|  |_|   
{Fore.GREEN}
 SMS Payload Injector
 Coded by indin White Hat Hacker: Mr White
{Fore.RESET}
    """
    print(banner)

# Twilio SMS function
def send_sms(to_number, from_number, message, account_sid, auth_token):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"{Fore.GREEN}[+] SMS sent successfully to {to_number}! SID: {message.sid}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error sending SMS: {str(e)}{Fore.RESET}")

# Main function
def main():
    display_banner()
    
    # Replace with your Twilio credentials
    account_sid = "your_twilio_account_sid"
    auth_token = "your_twilio_auth_token"
    from_number = "your_twilio_phone_number"
    
    print(f"{Fore.YELLOW}[*] SMS Payload Injector Started{Fore.RESET}")
    to_number = input(f"{Fore.CYAN}[?] Enter target phone number (e.g., +1234567890): {Fore.RESET}")
    message = input(f"{Fore.CYAN}[?] Enter message payload: {Fore.RESET}")
    count = int(input(f"{Fore.CYAN}[?] Enter number of SMS to send: {Fore.RESET}"))
    
    print(f"{Fore.YELLOW}[*] Sending {count} SMS to {to_number}...{Fore.RESET}")
    for i in range(count):
        send_sms(to_number, from_number, message, account_sid, auth_token)
        sleep(1)  # Delay to avoid API rate limits
        print(f"{Fore.YELLOW}[*] Sent {i+1}/{count} SMS{Fore.RESET}")
    
    print(f"{Fore.GREEN}[+] Operation completed!{Fore.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Exiting...{Fore.RESET}")
        sys.exit(0)
