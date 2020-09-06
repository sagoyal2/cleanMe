# cleanMe

I often find myself overwhelmed with the loose files placed in my Desktop, Documents and Downloads Folders and then my space gets cluttered very quickly. 

The goal of this script is simply to run at 1:15 am and help me the clean the Folders (we will move them to **Trash** which is safer than removing the file all together).


## Desktop

My Desktop Folder usually has stray screenshots, so this script will ask to delete all them.

## Documents

My Documents Folder usually is organized with both files and folders, so the screen will enforce that **only** folders exist and stray files and placed elsewhere. 

## Downloads

My Downloads Folder usually horrendous; filled with images, folders, csv's, pdf's, etc. The script will enforce **everything** is deleted

## Notes
To use this feature you need to add the following cronjob
 `15 1 * * * Documents/cleanMe/run_main.sh` with `crontab -e`

In Mac I had an issue with permission so make sure the cron has [Full Disk Access]([https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/](https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/))

> Written with [StackEdit](https://stackedit.io/).