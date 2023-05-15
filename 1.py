import os
import json


def convert_to_standard_format(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    formatted_data = {
        "image": data["imagePath"],
        "objects": []
    }

    if "vehicle" in data["shapes"]:
        formatted_data["objects"].append(
            {"class": "vehicle", "presence": True})

    if "license plate" in data["shapes"]:
        formatted_data["objects"].append(
            {"class": "license plate", "presence": True})

    if not formatted_data["objects"]:
        formatted_data["objects"].append({"class": "none", "presence": False})

    filename = os.path.basename(json_file)
    output_filename = filename.replace(".json", "_formatted.json")

    with open(output_filename, 'w') as f:
        json.dump(formatted_data, f, indent=4)

    print(f"Formatted JSON saved as {output_filename}")


# Provide the folder path where the JSON files are located
folder_path = "path/to/json/folder"

# Get a list of all JSON files in the folder
json_files = [file for file in os.listdir(
    folder_path) if file.endswith(".json")]

# Process each JSON file
for json_file in json_files:
    json_path = os.path.join(folder_path, json_file)
    convert_to_standard_format(json_path)
