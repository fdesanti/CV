import os
import sys
from datetime import datetime
from github import Github

# === Configuration ===
if __name__ == "__main__":
    REPO_NAME = "fdesanti/CV"  
    today = datetime.utcnow().strftime("%Y%m%d")
    TAG_NAME = f"cv-{today}"
    RELEASE_NAME = f"CV {today}"
    RELEASE_MESSAGE = f"CV updated @ {today}"

    FILES_TO_UPLOAD = [
        "CV/FedericoDeSanti_fullCV.pdf",
        "CV/FedericoDeSanti_publist.pdf",
        "CV/FedericoDeSanti_shortCV.pdf",
        "CV/FedericoDeSanti_talklist.pdf",
        "CV/FedericoDeSanti_publist.bib"
    ]

    # === Load GitHub token ===

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        try:
            with open("GITHUB_TOKEN", "r") as token_file:
                GITHUB_TOKEN = token_file.read().strip()
        except FileNotFoundError:
            print("Error: GitHub token not found. Set the GITHUB_TOKEN environment variable or create a GITHUB_TOKEN file.")
            sys.exit(1)

    # === Authenticate ===

    g = Github(GITHUB_TOKEN)

    try:
        repo = g.get_repo(REPO_NAME)
    except Exception as e:
        print(f"Error accessing repository: {e}")
        sys.exit(1)

    # === Check if release already exists ===

    release = None
    for r in repo.get_releases():
        if r.tag_name == TAG_NAME:
            release = r
            break

    # === Create release if needed ===

    if not release:
        try:
            release = repo.create_git_release(
                tag=TAG_NAME,
                name=RELEASE_NAME,
                message=RELEASE_MESSAGE,
                draft=False,
                prerelease=False
            )
            print(f"Release '{RELEASE_NAME}' created.")
        except Exception as e:
            print(f"Error creating release: {e}")
            sys.exit(1)
    else:
        print(f"Release '{RELEASE_NAME}' already exists.")

    # === Upload assets (with overwrite) ===

    for file_path in FILES_TO_UPLOAD:
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue

        asset_name = os.path.basename(file_path)

        # Delete asset if it already exists
        for asset in release.get_assets():
            if asset.name == asset_name:
                print(f"Deleting existing asset: {asset_name}")
                asset.delete_asset()
                break

        # Upload the asset
        try:
            release.upload_asset(path=file_path)
            print(f"Uploaded: {file_path}")
        except Exception as e:
            print(f"Error uploading '{file_path}': {e}")