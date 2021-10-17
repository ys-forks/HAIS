import os

from urllib import request
from urllib.parse import urlparse

# train_scans https://raw.githubusercontent.com/ScanNet/ScanNet/master/Tasks/Benchmark/scannetv2_train.txt
# val_scans https://raw.githubusercontent.com/ScanNet/ScanNet/master/Tasks/Benchmark/scannetv2_val.txt
# test_scans https://raw.githubusercontent.com/ScanNet/ScanNet/master/Tasks/Benchmark/scannetv2_test.txt

def download_data_split(url, filename):
    request.urlretrieve(url, filename)

def symlink_data(scans_filename, src, dest, extensions):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    with open(scans_filename, 'r') as fp:
        for line in fp:
            scan_id = line.strip()
            for ext in extensions:
                os.symlink(os.path.join(src, scan_id, scan_id+ext), os.path.join(dest, scan_id+ext))

if __name__ == "__main__":
    train_scans_url = "https://raw.githubusercontent.com/ScanNet/ScanNet/master/Tasks/Benchmark/scannetv2_train.txt"
    val_scans_url = "https://raw.githubusercontent.com/ScanNet/ScanNet/master/Tasks/Benchmark/scannetv2_val.txt"
    test_scans_url = "https://raw.githubusercontent.com/ScanNet/ScanNet/master/Tasks/Benchmark/scannetv2_test.txt"

    train_scans_filename = os.path.basename(urlparse(train_scans_url).path)
    val_scans_filename = os.path.basename(urlparse(val_scans_url).path)
    test_scans_filename = os.path.basename(urlparse(test_scans_url).path)

    download_data_split(train_scans_url, train_scans_filename)
    download_data_split(val_scans_url, val_scans_filename)
    download_data_split(test_scans_url, test_scans_filename)

    dataset_dir = '/local-scratch/localhome/yma50/Development/HAIS/dataset/scannetv2'
    train_folder = 'train'
    val_folder = 'val'
    test_folder = 'test'

    source_data_dir = '/cs/3dlg-datasets/released/scannet/public/v2/scans'
    extensions1 = ['_vh_clean_2.ply', '_vh_clean_2.labels.ply', '_vh_clean_2.0.010000.segs.json', '.aggregation.json']
    extensions2 = ['_vh_clean_2.ply']

    symlink_data(train_scans_filename, source_data_dir, os.path.join(dataset_dir, train_folder), extensions1)
    symlink_data(val_scans_filename, source_data_dir, os.path.join(dataset_dir, val_folder), extensions1)
    symlink_data(test_scans_filename, source_data_dir, os.path.join(dataset_dir, test_folder), extensions2)
    


