def replacer(input, output, relpace, rwith):
    with open(input, "r", encoding="utf-8") as input_file, open(output, "w", encoding="utf-8") as output_file:
        # Loop through each line in the input file
        for line in input_file:
            # Replace any capital T with a comma and a space
            line = line.replace(relpace, rwith)
        
            # Write the modified line to the output file
            output_file.write(line)
    
def deletesEverythingExceptFrom_Date():
    # Open the input file for reading and an output file for writing
    with open("telegram.txt", "r", encoding="utf-8") as input_file, open("from_q&date_q.txt", "w", encoding="utf-8") as output_file:
        # Loop through each line in the input file
        for line in input_file:
            # Check if the line contains "from:" or "date:"
            if "\"from\"" in line.lower() or "date" in line.lower():
                # If it does, write the line to the output file
                output_file.write(line)

def merger():
    # Open the input file for reading and an output file for writing
    with open('mergable.txt', "r", encoding="utf-8") as input_file, open('merged.txt', "w", encoding="utf-8") as output_file:
        # Loop through each line in the input file
        lines = input_file.readlines()
        for i in range(0, len(lines), 2):
            # Check if the current line is odd-numbered and has another line following it
            if i + 1 < len(lines):
                # Merge the current line with the next line and write the result to the output file
                merged_line = lines[i].strip() + " " + lines[i+1].strip() + "\n"
                output_file.write(merged_line)

def eraser(input_file, output_file, word_to_remove):
    # Define the word to search for

    # Open the input file for reading and the output file for writing
    with open(input_file, "r", encoding="utf-8") as input_file, open(output_file, "w", encoding="utf-8") as output_file:

        # Loop through each line in the input file
        for line in input_file:
            # If the line contains the word to remove, skip it
            if word_to_remove in line:
                continue
            
            # Otherwise, write the line to the output file
            output_file.write(line)

def repeatedFirstWordChecker():
    # Open the input file for reading and an output file for writing
    with open("from&date.txt", "r", encoding="utf-8") as input_file, open("mergablefd.txt", "w", encoding="utf-8") as output_file:
        # Read the first line of the file
        prev_line = input_file.readline().strip()
        
        # Loop through each line in the input file starting from the second line
        for i, line in enumerate(input_file, start=2):
            # Check if the current line starts with the same word as the previous line
            curr_word = line.strip().split()[0]
            
            if prev_line:
                prev_word = prev_line.split()[0]
                
                if curr_word == prev_word:
                    print(f"Anomaly found at line {i-1} and {i}: {prev_line.strip()} - {line.strip()}")
                    
                    # Determine which line comes second and delete it
                    if prev_line < line:
                        line = ""
                    else:
                        prev_line = ""
                
                # Write the previous line to the output file, unless it was deleted
                output_file.write(prev_line + "\n")
            
            # Set the current line as the previous line for the next iteration
            prev_line = line.strip()
        
        # Write the last line to the output file after the loop finishes, unless it was deleted
        if prev_line:
            output_file.write(prev_line + "\n")

def replaceUnknown():
    # Open the input files for reading and an output file for writing
    with open("nicer_2.txt", "r", encoding='utf-8') as origin_file, open("whatsappfinal.txt", "r", encoding='utf-8') as insertion_file, open("semifinal.txt", "w", encoding='utf-8') as output_file:
        # Read the lines of the origin file into a list
        origin_lines = origin_file.readlines()
        
        # Loop through each line in the insertion file
        for insertion_line in insertion_file:
            # Find the text in between [] in the current line
            start_index = insertion_line.find("[")
            end_index = insertion_line.find("]")
            if start_index != -1 and end_index != -1:
                search_text = insertion_line[start_index+1:end_index]
                
                # Search for the text in origin file
                found = False
                for origin_line in origin_lines:
                    if search_text in origin_line:
                        # If the text is found, extract the word between two commas in the same line 
                        comma_indexes = [i for i, char in enumerate(origin_line) if char == ',']
                        if len(comma_indexes) >= 2:
                            origin_word = origin_line[comma_indexes[0]+1:comma_indexes[1]]
                            
                            # Replace "Unknown" with the extracted word in the current line of insertion file
                            insertion_line = insertion_line.replace("Unknown", origin_word)
                            
                            # Mark the search as successful
                            found = True
                            break
                
                # If the search was unsuccessful, write the original line to the output file
                if not found:
                    output_file.write(insertion_line)
            else:
                # If the current line doesn't contain [], write it to the output file as is
                output_file.write(insertion_line)
            
            # Write the modified or original line to the output file
            output_file.write(insertion_line)



import json

# Open the Telegram chat export file for reading
with open('telegram.txt', 'r', encoding='utf-8') as telegram_file:
    # Parse the JSON data from the Telegram file
    telegram_data = json.loads(telegram_file.read())

# Create a new WhatsApp chat export file for writing
with open('whatsapp.txt', 'w', encoding='utf-8') as whatsapp_file:
    # Loop through each message in the Telegram data
    for message in telegram_data['messages']:
        # Extract the relevant attributes from the Telegram message
        from_field = message.get('from', {})
        if isinstance(from_field, dict):
            sender = from_field.get('username', '')
            if not sender:
                sender = from_field.get('print_name', '')
        else:
            sender = ''
        sender = sender or 'Unknown'
        timestamp = str(message['date'])
        content = message.get('text', '')

        # Check if the content includes media attachments
        if isinstance(content, list):
            content = '[Media]'
        elif not content:
            content = '[No text]'

        # Reformat the data into the format used by WhatsApp
        whatsapp_message = '[' + timestamp + '] ' + sender + ': ' + content + '\n'

        # Write the reformatted message to the WhatsApp file
        whatsapp_file.write(whatsapp_message)

deletesEverythingExceptFrom_Date()

replacer('from_q&date_q.txt', 'from&date_q.txt', '   "from"', "from" )
replacer('from&date_q.txt', 'from&date.txt', '   "date"', 'date')

repeatedFirstWordChecker()

replacer('mergablefd.txt', 'mergablef.txt', 'date: ', '')
replacer('mergablef.txt', 'mergable.txt', 'from: ', '')

merger()


firstUsername = input('''
                                            




                                            FIRST username in telegram.txt file:


                                              ''')
messyName ='"' +  firstUsername + '"'

secondUsername = input('''
                                            SECOND username in telegram.txt file:


                                              ''')
messyName2 ='"' +  secondUsername + '"'


replacer('merged.txt', 'nicer1.txt', messyName, firstUsername)
replacer('nicer1.txt', 'nicer_2.txt', messyName2, secondUsername)


eraser('whatsapp.txt', 'whatsappMedia.txt', '[No text]')
eraser('whatsappMedia.txt', 'whatsappfinal.txt', '[Media]')

replaceUnknown()

replacer('semifinal.txt', '_chat.txt', 'T', ', ')


import os

# deletes unwanted files
filenames = 'from&date.txt,from&date_q.txt,from_q&date_q.txt,mergable.txt,mergablef.txt,mergablefd.txt,merged.txt,nicer_2.txt,nicer1.txt,semifinal.txt,whatsapp.txt,whatsappfinal.txt,whatsappMedia.txt'
filenames = filenames.split(",")

# get the directory of the Python program
directory = os.path.dirname(os.path.abspath(__file__))

# loop through each filename to delete
for filename in filenames:
    # strip any leading/trailing whitespace from the filename
    filename = filename.strip()
    
    # create a list of all files in the directory
    all_files = os.listdir(directory)

    # loop through each file in the directory
    for file in all_files:
        # check if the current file matches the filename to delete
        if file == filename:
            # construct the full path to the file
            filepath = os.path.join(directory, file)

            # delete the file
            os.remove(filepath)

            print(f"File {filename} deleted successfully.")


print('_chat.txt was generated. Mission acomplished ')