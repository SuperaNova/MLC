import os
import subprocess
import json
from datetime import datetime

def get_kaggle_metadata(dataset: str):
    """
    Fetch metadata for a Kaggle dataset using the Kaggle CLI.
    Returns the JSON response as a dict.
    """
    try:
        subprocess.run(
            ["kaggle", "datasets", "metadata", dataset, "-p", "."],
            check=True,
            capture_output=True,
            text=True
        )
        metadata_file = f"{dataset.split('/')[-1]}-dataset-metadata.json"
        if os.path.exists(metadata_file):
            with open(metadata_file, "r") as f:
                metadata = json.load(f)
            os.remove(metadata_file)  # cleanup
            return metadata
    except subprocess.CalledProcessError as e:
        print("Error: Could not fetch dataset metadata:", e)
    return None


def get_local_version(version_file: str):
    """Read the locally saved dataset version date, if available."""
    if os.path.exists(version_file):
        with open(version_file, "r") as f:
            return f.read().strip()
    return None


def save_local_version(version_file: str, last_updated: str):
    """Save the dataset's last updated date locally."""
    with open(version_file, "w") as f:
        f.write(last_updated)


def download_bitcoin_data():
    """
    Downloads the Bitcoin historical dataset from Kaggle into the data/ folder.
    Checks if the local copy is up to date before downloading.
    """
    dataset = "mczielinski/bitcoin-historical-data"
    output_dir = "data"
    version_file = os.path.join(output_dir, "DATA_VERSION.txt")

    os.makedirs(output_dir, exist_ok=True)

    print("Checking dataset metadata...")
    metadata = get_kaggle_metadata(dataset)
    if metadata:
        title = metadata.get("title")
        last_updated = metadata.get("lastUpdated")
        print(f"Dataset: {title}")
        print(f"Latest Kaggle update: {last_updated}")

        local_version = get_local_version(version_file)
        if local_version == last_updated:
            print("Local dataset is already up to date. Skipping download.")
            return
    else:
        print("Warning: Could not fetch metadata. Proceeding with download.")
        last_updated = None

    print("Downloading dataset from Kaggle...")
    try:
        subprocess.run(
            ["kaggle", "datasets", "download", "-d", dataset, "-p", output_dir, "--unzip", "--force"],
            check=True
        )
        print("Download complete. Data saved in 'data/'")
        if last_updated:
            save_local_version(version_file, last_updated)
    except subprocess.CalledProcessError as e:
        print("Error downloading dataset:", e)
        print("Make sure kaggle.json is correctly placed and Kaggle CLI is installed.")


if __name__ == "__main__":
    download_bitcoin_data()
# To run this script, ensure you have the Kaggle CLI installed and configured.  