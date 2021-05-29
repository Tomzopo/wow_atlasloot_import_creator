# Convert Item ID file list to atlasloot import

import os
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
    file_output = open(output_filename, 'x')

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


def fix_export():
    input_filename = "files_to_be_fixed"


def create_from_export(filename):
    fixed_input_filename = "temp_files/to_be_fixed/" + filename
    file_input = open(fixed_input_filename, 'r')

    output_filename = "temp_files/item_lists/" + filename
    if os.path.exists(output_filename):
        os.remove(output_filename)
    file_output = open(output_filename, 'x')

    for line in file_input:
        item_list = line.split(',')
        fixed_ids = {item_id.replace('i:', '') for item_id in item_list}

        for current_id in fixed_ids:
            file_output.write(current_id + '\n')

    file_input.close()
    file_output.close()

    os.remove(fixed_input_filename)


if __name__ == '__main__':

    # file_list_export_fix = get_files("temp_files/to_be_fixed")
    # for file in file_list_export_fix:
    #     create_from_export(file)

    scraper.get_input_files("preraid_pages.txt")
    scraper.get_input_files("phase1_pages.txt")

    file_list_input = get_files("temp_files/item_lists/")
    for file in file_list_input:
        read_item_id_file(file)
