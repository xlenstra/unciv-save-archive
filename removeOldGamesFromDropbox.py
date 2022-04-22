import dropbox
from datetime import datetime

LAST_YEAR_TO_REMOVE = 2021
LAST_MONTH_TO_REMOVE = 9
LAST_DAY_TO_REMOVE = 30


last_date_to_remove = datetime(LAST_YEAR_TO_REMOVE, LAST_MONTH_TO_REMOVE, LAST_DAY_TO_REMOVE)

dbx = dropbox.Dropbox("LTdBbopPUQ0AAAAAAAACxh4_Qd1eVMM7IBK3ULV3BgxzWZDMfhmgFbuUNF_rXQWb")

stop = False

i = 0
while True:
    # We can just use the list_folder and ignore the cursor
    # as we delete all files anyway
    folderList = dbx.files_list_folder('/MultiplayerGames')

    print("Starting with page {0}, containing {1} save games".format(i, len(folderList.entries)))

    i += 1

    for entry in folderList.entries:
        print("Found file {0}".format(entry.name))
        metadata = dbx.files_download_to_file("./saveFiles/{0}".format(entry.name), "/MultiplayerGames/{0}".format(entry.name))
        print("Downloaded file {0}".format(entry.name))

        if (metadata.client_modified <= last_date_to_remove and metadata.server_modified <= last_date_to_remove and entry.name != ""):
            dbx.files_delete("/MultiplayerGames/{0}".format(entry.name))
            print("Deleted file {0}".format(entry.name))
        else:
            stop = True
            break

    if (stop):
        break
