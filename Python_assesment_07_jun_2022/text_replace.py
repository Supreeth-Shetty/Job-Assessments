import logging

logging.basicConfig(filename="logs.log",
                    level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')

class ReplaceContent():
    def __init__(self, text_file) -> None:
        self.text_file = text_file

    def replace_string_in_file(self, old_string:str, new_string:str) -> None:
        """
        Replace all occurrences of old_string with new_string in text file
        """
        try:
            with open(self.text_file, 'r') as f: # Open file for reading
                file_data = f.read()
            logging.info(f"The file content before replacement:{file_data}")
            if old_string in file_data.split():
                file_data = file_data.replace(old_string, new_string) # Replace old_string with new_string in file_data
                with open(self.text_file, 'w') as f: # Open file for writing
                    f.write(file_data)
                    logging.info(f"Replaced all occurrences of '{old_string}' with '{new_string}' in file '{self.text_file}'")
                    logging.info(f"The file content after replacement:{file_data}")
            else:
                logging.info(f"No occurrences of '{old_string}' found in file '{self.text_file}'")
        
        except Exception as e:
            logging.error(e)

Content = ReplaceContent("example.txt")
Content.replace_string_in_file("placement", "screening")

print("Please check the logs.log file for more details")