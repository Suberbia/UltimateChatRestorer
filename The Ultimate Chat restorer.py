import json

def convert_telegram_to_whatsapp(telegram_export_path, whatsapp_output_path):
    # Load the Telegram export JSON file
    with open(telegram_export_path, 'r', encoding='utf-8') as file:
        telegram_data = json.load(file)
    
    # Open the output file where the WhatsApp-like chat will be saved
    with open(whatsapp_output_path, 'w', encoding='utf-8') as output_file:
        # Iterate through each message in the Telegram export
        for message in telegram_data.get('messages', []):
            # Extract the necessary information
            date = message.get('date', '')
            from_user = message.get('from', '')
            text = message.get('text', '')
            
            # WhatsApp doesn't use the exact same date format, but we'll simplify it
            # Telegram format: 2020-01-01T00:00:00
            # Simplified for our purposes: [01/01/2020, 00:00:00]
            date_parts = date.split('T')
            if len(date_parts) == 2:
                date_formatted = date_parts[0].replace('-', '/')
                time_formatted = date_parts[1]
                date = f"[{date_formatted}, {time_formatted}]"
            
            # Prepare the message in a WhatsApp-like format
            whatsapp_message = f"{date} - {from_user}: {text}\n"
            
            # Handle non-string messages (e.g., media messages)
            if not isinstance(text, str):
                whatsapp_message = f"{date} - {from_user}: <Media omitted>\n"
            
            # Write the formatted message to the output file
            output_file.write(whatsapp_message)

# Calling the function
convert_telegram_to_whatsapp('result.json', '_chat.txt')
