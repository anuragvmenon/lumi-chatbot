import os
import subprocess
import sys

def download_dataset():
    """
    Downloads the NLP Mental Health Conversations dataset from Kaggle.
    """
    dataset_name = "msjordan/nlp-mental-health-conversations"
    download_dir = "data"

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Check if the dataset is already downloaded
    if os.path.exists(os.path.join(download_dir, "train.csv")):
        print("Dataset already downloaded.")
        return

    print("Downloading dataset...")
    try:
        python_executable = sys.executable
        scripts_dir = os.path.join(os.path.dirname(python_executable), "Scripts")
        kaggle_exe = os.path.join(scripts_dir, "kaggle.exe")

        if not os.path.exists(kaggle_exe):
             # fall back to just kaggle
             kaggle_exe = "kaggle"

        subprocess.run([kaggle_exe, "datasets", "download", "-d", dataset_name, "-p", download_dir, "--unzip"], check=True)
        print("Dataset downloaded and unzipped successfully.")
    except FileNotFoundError:
        print("Kaggle CLI not found. Please ensure it is installed and in your PATH.")
        print("You can install it with: pip install kaggle")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading dataset: {e}")
        print("Please ensure your Kaggle API credentials are set up correctly.")
        print("See: https://www.kaggle.com/docs/api")

if __name__ == "__main__":
    download_dataset()
