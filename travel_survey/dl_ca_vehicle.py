import os
import json
import requests
import argparse
import zipfile


def download(year=2019, out_dir=None, zip_name=None):

    nrel_url = "https://www.nrel.gov/transportation/secure-transportation-data/assets/downloads/"

    urls = {
        2019: "tsdc-2019-california-vehicle-survey.zip",
        2017: "cec_17_full_survey.zip",
        2013: "cec_full_survey.zip"
    }

    if year not in urls:
        raise ValueError("Year must be one of {}".format(urls.keys()))
    url = nrel_url + urls[year]
    local_filename = os.path.join(out_dir, zip_name)
    
    if os.path.exists(local_filename):
        print("File already exists: {}".format(local_filename))
        return

    print("Downloading from: {}".format(url))
    
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the local file for writing in binary mode
        with open(local_filename, 'wb') as file:
            # Write the contents of the response to the file
            file.write(response.content)
        print(f'Successfully downloaded {local_filename}')
    else:
        print(f'Failed to download the file. Status code: {response.status_code}')


def unzip(code=1, target_folder=None, zip_path=None):
    """
    code: 0: do not unzip, 1: unzip & keep zip file, 2: unzip & remove zip file
    """
    
    assert code in [0, 1, 2], "code must be one of 0, 1, 2"

    if code == 0:
        return

    # Define the target folder
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f'Created target folder: {target_folder}')

    # Extract the ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_folder)

    # Define the source and destination paths for the "data" and "documentation" folders
    source_data = os.path.join(target_folder, 'data')
    destination_data = target_folder

    # Move files from "data" to "ccc"
    for root, dirs, files in os.walk(source_data):
        for file in files:
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_data)
            destination_path = os.path.join(destination_data, relative_path)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            os.rename(source_path, destination_path)

    # Remove the now-empty "data" and "documentation" folders
    os.rmdir(source_data)

    print('Files extracted and organized successfully.')
    
    
    if code == 2:
        os.remove(zip_path)


def check_exist(out_dir, zip_name):
    # TODO: not implemented yet
    # if the extracted files already exist, return 2
    assert os.path.exists(out_dir), "out_dir does not exist: {}".format(out_dir)
    fns = os.listdir(out_dir)
    if False:
        return 2

    # if the zip file already exists, return 1
    if os.path.exists(os.path.join(out_dir, zip_name)):
        return 1
    
    # if nothing exists, return 0
    return 0


if __name__ == "__main__":
    
    # sample: python dl_ca_vehicle.py --year 2019 --unzip 1 --out_dir /home/ecal_team/datasets
    #           --save_folder ca_vehicle_2019 
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', type=int, default=2019, help='year of the survey, avail: 2013, 2017, 2019')
    parser.add_argument('--unzip', type=int, default=1, help='0: do not unzip, 1: unzip & keep zip file, 2: unzip & remove zip file')
    parser.add_argument('--out_dir', type=str, default=None, help='output directory, if None, look for xxx')
    args = parser.parse_args()

    assert args.year in [2013, 2017, 2019], "year must be one of 2013, 2017, 2019"

    # the following can be reused for other datasets
    if args.out_dir is None:
        curr_dir = os.path.realpath(__file__)
        path_file = os.path.join(curr_dir.split("travel_survey")[0], "paths.json")
        assert os.path.exists(path_file), "Cannot find paths.json file, please specify out_dir"
        
        with open(path_file, "r") as f:
            paths = json.load(f)
        try:
            datasets_dir = paths["datasets"]
            ca_vehicle_dir = paths["ca_vehicle"]
        except KeyError:
            raise KeyError("make sure key \"datasets\" AND \"ca_vehicle\" are in paths.json")
        out_dir = os.path.join(datasets_dir, ca_vehicle_dir)
        assert os.path.exists(datasets_dir), "Cannot find dir: {}".format(datasets_dir)
    else:
        out_dir = args.out_dir
        
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    zip_name = f"ca_vehicle_{args.year}.zip"

    
    download(year=args.year, out_dir=out_dir, zip_name=zip_name)
    target_folder = os.path.join(out_dir, f"ca_vehicle_{args.year}")
    unzip(code=args.unzip, target_folder=target_folder, zip_path=os.path.join(out_dir, zip_name))

    
    """
    # TODO: add overwrite options
    # TODO: do not download if the files already exist
    status = check_exist(out_dir, zip_name)
    if status == 0:
        download(year=args.year, out_dir=out_dir, zip_name=zip_name)
    elif status == 1:
        
    elif status == 2:
        print("Files already exist, skipping download and unzip")
    """
    
    print("DONE", "="*50)
