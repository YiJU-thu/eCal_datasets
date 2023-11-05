import os
import argparse
import numpy as np
import pandas as pd
import json
from acndata_src.data_client import DataClient


def compress_timeseries(ts, eps=1e-1):
    if "pilotSignal" not in ts:
        return ts
    

    def filter_changes(df, key):
        if df.empty:    # ts["pilotSignal/chargingCurrent"] is None
            return None
        p = df[key].values
        keep = (np.abs(p[1:]-p[:-1]) > 0.1)
        keep[-1] = True # Keep the last one
        keep = np.concatenate(([True], keep))  # Keep the first one 
        # print(key, "Keeping %d out of %d samples" % (np.sum(keep), len(keep)))
        return dict(df.loc[keep].values)

    pilot_df = pd.DataFrame(ts["pilotSignal"])
    current_df = pd.DataFrame(ts["chargingCurrent"])
    
    ts["pilotSignal"] = filter_changes(pilot_df, "pilot")
    ts["chargingCurrent"] = filter_changes(current_df, "current")
    # sample:
    # {Timestamp('2018-04-25 04:07:05-0700', tz='America/Los_Angeles'): 0.0,}
    
    return ts


def download_acn_data(api_key, site, test=False, timeseries=False, ts_compress_eps=1e-1, out_dir=None):
    client = DataClient(api_key)
    sites = ["caltech", "jpl", "office001"]
    
    if site == "all":    
        for site in sites:
            download_acn_data(api_key, site, test, timeseries, ts_compress_eps, out_dir)
        return
    
    assert site in sites, "site must be one of caltech, jpl, office001"
    
    if out_dir is not None:
        save_fn = "acn_data_{}{}{}.csv".format(site, "_ts"*timeseries, "_test"*test)
        save_fn = os.path.join(out_dir, save_fn)
        if not test and os.path.exists(save_fn):
            print("{} already exists, skipping...".format(save_fn))
            return
    
    
    gen = client.get_sessions(site, timeseries=timeseries)  # a generator
    
    if test:
        len_test = 20
        data = pd.DataFrame([compress_timeseries(next(gen), eps=ts_compress_eps) for _ in range(len_test)])
    else:
        data = pd.DataFrame([compress_timeseries(s, eps=ts_compress_eps) for s in gen])

    if out_dir is not None:
        data.to_csv(save_fn, index=False)
        print("{} [{}] successfully saved - {} records".format("Testing..."*test, site, len(data)))
        
        if test:
            pass
            # os.remove(os.path.join(out_dir, save_fn))   # remove the test file

    return data



if __name__ == "__main__":
    curr_dir = os.path.realpath(__file__)

    # the following part can be reused for other datasets
    # ================================================
    key = "acn_data"
    def read_apikey_from_keyboard():
        # read API key from keyboark input
        api_key = input(f"Please enter your API key for {key} (\"0\" for skip): ")
        if api_key == "0":
            raise ValueError("API key is not provided")
        else:
            return api_key
        
    try:
        api_fn =  os.path.join(curr_dir.split("ACN_data")[0], "NoTrack.json")
        with open(api_fn, "r") as f:
            api_key = json.load(f)[key]
    except KeyError:
        print("Cannot find API key for acndata in NoTrack.json")
        api_key = read_apikey_from_keyboard()
    except FileNotFoundError:
        print("Cannot find NoTrack.json")
        api_key = read_apikey_from_keyboard()
    # ================================================
    # print(f"API key for {key} is: {api_key}")


    # sample command
    # python dl_acn_data.py --site caltech --timeseries --ts_compress_eps 1e-1 --out_dir /home/ecal_team/datasets

    parser = argparse.ArgumentParser()
    parser.add_argument('--site', type=str, default="caltech", help='site name, avail: caltech, jpl, office001. \"all\" for all sites')
    parser.add_argument('--timeseries', action='store_true', help='whether to download time series data')
    parser.add_argument('--ts_compress_eps', type=float, default=1e-1, help='eps for compressing time series data (keep a record only when it changes >= eps from it previous one)')
    parser.add_argument('--out_dir', type=str, default=None, help='output directory, if None, look for paths.json')
    parser.add_argument('--test', action='store_true', help='whether to run in test mode (download only 20 records)')

    args = parser.parse_args()

    if args.out_dir is None:
        path_file = os.path.join(curr_dir.split("ACN_data")[0], "paths.json")
        assert os.path.exists(path_file), "Cannot find paths.json file, please specify out_dir"
        
        with open(path_file, "r") as f:
            paths = json.load(f)
        try:
            datasets_dir = paths["datasets"]
            acn_data_dir = paths["acn_data"]
        except KeyError:
            raise KeyError("make sure key \"datasets\" AND \"acn_data\" are in paths.json")
        out_dir = os.path.join(datasets_dir, acn_data_dir)
        assert os.path.exists(datasets_dir), "Cannot find dir: {}".format(datasets_dir)
    else:
        out_dir = args.out_dir
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    download_acn_data(api_key, site=args.site, test=args.test, timeseries=args.timeseries, ts_compress_eps=args.ts_compress_eps, out_dir=out_dir)

        