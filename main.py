import requests

# Function to send a message to a Discord webhook
def send_message_to_discord(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(f"Response: {response.text}")

# Main function
def main():
    # Your actual Discord webhook URL
    webhook_url = 'PUT YOUR WEBHOOK URL HERE'

    # Prompt user for input
    message = input("Enter the message to send to Discord: ")

    # Send the message to the Discord webhook
    send_message_to_discord(webhook_url, message)

if __name__ == "__main__":
    main()
