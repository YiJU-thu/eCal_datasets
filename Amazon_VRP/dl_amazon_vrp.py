import os, sys
import json
import argparse
import subprocess


def download_amazon_vrp(out_dir=None, test=False):
    
    assert os.path.exists(out_dir), "out_dir does not exist"

    # AWS S3 bucket and object information
    s3_bucket = "amazon-last-mile-challenges"
    s3_object = "almrrc2021"  # Replace with the actual S3 object name

    # Use subprocess to run AWS CLI command to download from S3 to the specified folder
    
    if not test:
        aws_command = [
            "aws","s3","cp","--no-sign-request",f"s3://{s3_bucket}/{s3_object}",out_dir, "--recursive"
        ]
    else:
        aws_command = [
            "aws","s3","ls","--no-sign-request",f"s3://{s3_bucket}/{s3_object}/"
        ]


    if not test:
        try:
            subprocess.run(aws_command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Download successful. File saved to: {out_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Download failed. Error: {e.stderr}")
    else:
        try:
            result = subprocess.run(aws_command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Test successful.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Test failed. Error: {e.stderr}")
    


if __name__ == "__main__":
    curr_dir = os.path.dirname(__file__)
    utils_dir = os.path.join(curr_dir, "../utils")
    if utils_dir not in sys.path:
        sys.path.append(utils_dir)
    from util_func import get_dataset_dir

    # sample command
    # python dl_amazon_vrp.py --out_dir ../amazon_vrp/
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, default=None, help="output directory")
    parser.add_argument("--test", action="store_true", help="test mode")
    args = parser.parse_args()

    out_dir = get_dataset_dir("amazon_vrp", args.out_dir, mkdir=True)
    download_amazon_vrp(out_dir=out_dir, test=args.test)