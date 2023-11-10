import os, sys
import argparse
import pandas as pd
import json
from datetime import datetime, timedelta


def get_latest_fn(name, fns):
    fns = [fn for fn in fns if name in fn]
    if len(fns) == 0:
        return None, None, None
    else:
        last_update = max([datetime.strptime(fn.split("_")[-1][:-5], "%Y%m%d") for fn in fns])
        last_fn = f"{name}_{last_update.strftime('%Y%m%d')}.xlsx"
    return last_fn, last_update, fns


def download_region_file(url, update_delta=1000, out_dir=None, test=False):
    
    today = datetime.today()
    region_fn = url.split("/")[-1][:-5]

    fns = os.listdir(out_dir)

    _, last_update, exist_fns = get_latest_fn(region_fn, fns)
    if exist_fns is not None:
        if test:
            pass
        elif (today - last_update).days < update_delta:
            print("Region file [{:^8}] already exists, skipping...".format(region_fn.split("_")[-1]))
            return
        else:
            print("Region file [{:^8}] is outdated, updating...".format(region_fn.split("_")[-1]))
            # remove outdated files
            for fn in exist_fns:
                os.remove(os.path.join(out_dir, fn))
    
    save_fn = os.path.join(out_dir, "{}_{}{}.xlsx".format(region_fn, today.strftime("%Y%m%d"), "_test"*test))
    os.system("wget {} -O {}".format(url, save_fn))
    print("Region file [{:^8}] successfully saved".format(region_fn.split("_")[-1]))
    if test:
        # remove test file
        os.remove(save_fn)



if __name__ == "__main__":
    curr_dir = os.path.dirname(__file__)
    utils_dir = os.path.join(curr_dir, "../utils")
    if utils_dir not in sys.path:
        sys.path.append(utils_dir)
    from util_func import get_dataset_dir


    # sample command
    # python dl_eia_grid.py --region all --out_dir ../EIA_grid/data/ --update_delta 30

    parser = argparse.ArgumentParser()
    parser.add_argument("--region", type=str, default="all", help="region name, see EIA_region_url.xlsx ID column")
    parser.add_argument("--out_dir", type=str, default=None, help="output directory")
    parser.add_argument("--update_delta", type=int, default=30, help="update delta in days. If a file of the same region already exists, it will be skipped if the last update is within this delta")
    parser.add_argument("--test", action="store_true", help="download CAL for testing")

    args = parser.parse_args()

    out_dir = get_dataset_dir("eia_grid", args.out_dir, mkdir=True)

    url_fn = os.path.join(curr_dir, "EIA_region_url.xlsx")
    assert os.path.exists(url_fn), "Cannot find EIA_region_url.xlsx"
    url_df = pd.read_excel(url_fn)

    if args.test:
        urls = url_df[url_df["ID"] == "CAL"]["URL"].tolist()
    elif args.region == "all":
        urls = url_df["URL"].tolist()
    else:
        try:
            urls = url_df[url_df["ID"] == args.region]["URL"].tolist()
        except KeyError:
            raise KeyError("Region ID \"{}\" not found".format(args.region))
    

    for url in urls:
        download_region_file(url, args.update_delta, out_dir, args.test)