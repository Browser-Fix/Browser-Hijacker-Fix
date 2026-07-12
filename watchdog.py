import os
import shutil
import time
import subprocess
from datetime import datetime


# Known built-in extensions
SAFE_EXTENSIONS = {
    # Google built-in
    "ghbmnnjooekpmoecnnnilnnbdlolhkhi",  # Google apps/payment integration
    "nmmhkkegccagdldgiimedpiccmgmieda",  # Google Payments

    # Microsoft built-in
    "jmjflgjpcpepeafmmgdpfkogkghcpiha",  # Edge text feature
}


BACKUP_FOLDER = os.path.expanduser(
    r"~\Desktop\Extension_Backup"
)


def close_browsers():
    print("[*] Closing browsers...")

    subprocess.call(
        "taskkill /f /im chrome.exe",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True
    )

    subprocess.call(
        "taskkill /f /im msedge.exe",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True
    )

    time.sleep(2)


def clean_extensions(extension_path):

    if not os.path.exists(extension_path):
        return

    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    print("\nChecking:")
    print(extension_path)

    for ext in os.listdir(extension_path):

        full_path = os.path.join(extension_path, ext)

        if ext in SAFE_EXTENSIONS:
            print("[KEEP]", ext)
            continue

        if os.path.isdir(full_path):

            backup = os.path.join(
                BACKUP_FOLDER,
                ext + "_" + datetime.now().strftime("%H%M%S")
            )

            print("[REMOVE]", ext)

            try:
                shutil.move(full_path, backup)
                print("  backed up ->", backup)

            except Exception as e:
                print("  error:", e)


def main():

    print("""
=============================
 Extension Cleanup Tool
=============================
""")

    close_browsers()

    chrome = os.path.expanduser(
        r"~\AppData\Local\Google\Chrome\User Data\Default\Extensions"
    )

    edge = os.path.expanduser(
        r"~\AppData\Local\Microsoft\Edge\User Data\Default\Extensions"
    )

    clean_extensions(chrome)
    clean_extensions(edge)

    print("""
=============================
Finished.
Removed extensions were backed up
to Desktop\Extension_Backup
=============================
""")


if __name__ == "__main__":
    main()