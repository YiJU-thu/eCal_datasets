import os
import json


def get_dataset_dir(dataset_key=None, out_dir=None, mkdir=False):
    
    
    curr_dir = os.path.dirname(__file__)
    
    if out_dir is None:
        path_file = os.path.join(curr_dir.split("utils")[0], "paths.json")
        assert os.path.exists(path_file), "Cannot find paths.json file, please specify out_dir"
        
        with open(path_file, "r") as f:
            paths = json.load(f)
        try:
            datasets_root = paths["datasets"]
            dataset_rel_dir = paths[dataset_key]
        except KeyError:
            raise KeyError(f"make sure key \"datasets\" AND \"{dataset_key}\" are in paths.json")
        out_dir = os.path.join(datasets_root, dataset_rel_dir)
        assert os.path.exists(datasets_root), "Cannot find dir: {}".format(datasets_root)
    
    if not os.path.exists(out_dir):
        if mkdir:
            os.makedirs(out_dir)
        else:
            print("out_dir does not exist: {}".format(out_dir))
    
    return out_dir
    