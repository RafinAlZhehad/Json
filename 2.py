import os
import json


def combine_and_convert(json_folder):
    combined_data = {
        "images": [],
        "objects": []
    }

    json_files = [file for file in os.listdir(
        json_folder) if file.endswith(".json")]

    for json_file in json_files:
        with open(os.path.join(json_folder, json_file), 'r') as f:
            data = json.load(f)

        combined_data["images"].append(data["image"])

        for obj in data["objects"]:
            class_name = obj["class"]

            if class_name == "vehicle":
                class_name = "car"
            elif class_name == "license plate":
                class_name = "number"

            combined_data["objects"].append(
                {"class": class_name, "presence": obj["presence"]})

    combined_output = {
        "combined_images": combined_data["images"],
        "combined_objects": combined_data["objects"]
    }

    with open("combined_data.json", 'w') as f:
        json.dump(combined_output, f, indent=4)

    print("Combined JSON saved as combined_data.json")


# Provide the folder path where the JSON files are located
json_folder_path = "path/to/json/folder"

combine_and_convert(json_folder_path)
