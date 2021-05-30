# Convert Item ID file list to atlasloot import

import os
import shutil

import item_scraper as scraper


def get_files(file_path):
    files_list = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]

    return files_list


def read_item_id_file(filename):
    input_filename = "temp_files/item_lists/" + filename
    file_input = open(input_filename, 'r')

    output_filename = "atlas_loot_imports/" + filename
    if os.path.exists(output_filename):
        os.remove(output_filename)
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    file_output = open(output_filename, 'x', encoding="utf-16")

    file_output.write('i:10052,')
    file_output.write('i:28788,')

    item_seen = set()
    item_seen.add('10052')
    item_seen.add('28788')

    for line in file_input:
        if line.strip() not in item_seen:
            item_seen.add(line.strip())
            file_output.write('i:' + line.strip() + ',')

    file_input.close()
    file_output.close()

    print("Completed: " + output_filename)


if __name__ == '__main__':
    if os.path.exists('temp_files'):
        shutil.rmtree('temp_files')

    if os.path.exists('atlas_loot_imports'):
        shutil.rmtree('atlas_loot_imports')

    scraper.get_input_files("preraid_pages.txt")
    scraper.get_input_files("phase1_pages.txt")

    file_list_input = get_files("temp_files/item_lists/")

    for file in file_list_input:
        read_item_id_file(file)
