from datetime import datetime, date
import json
import sys
import os
import zipfile
import logging

def setup_logging(logs_dir):
    # Ensure the _logs directory exists
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Create a log file with the format log_yyyymmdd.txt
    log_filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    log_filepath = os.path.join(logs_dir, log_filename)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()  # Optional: To also print logs to the console
        ]
    )
 

def log(str):
    print(str)

def get_app_name():
    # Get the full path of the script or executable
    exe_full_path = sys.argv[0]

    # Extract the base name (file name or exe name) and remove the extension
    exe_name = os.path.splitext(os.path.basename(exe_full_path))[0]

    return exe_name


# convert to dict
# Using vars() will fail if there are complex types, so we'll handle that
def obj_serializer(obj):
    """Custom JSON serializer for objects not serializable by default."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()  # Convert datetime objects to ISO format
    elif hasattr(obj, "__dict__"):
        # For complex objects, recursively convert their __dict__ attributes
        return vars(obj)
    else:
        return str(obj)  # Convert anything else to a string

def read_json_file(json_file_path):
    # Open and read the JSON file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    return data

def zip_folder(folder_path, filename_prefix, output_folder_path):
    # Generate a zip file name based on timestamp
    zip_filename = f"{filename_prefix}{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_filepath = os.path.join(output_folder_path, zip_filename)
    
    # Create the zip file
    with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Traverse all files and directories within the input folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Create the full file path
                file_path = os.path.join(root, file)
                # Write the file to the zip archive with a relative path
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
                
    return zip_filepath

def datetime_to_string_yyyymmdd_hhmmss(dt):
    return dt.strftime('%Y%m%d_%H%M%S')