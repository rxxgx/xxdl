import os
url = os.getenv("URL")
args = '--threads 8 --wait  -o "DL/(%(channel_id)s)_[%(date)s]_%(channel_name)s_%(title)s.%(ext)s" ' + url
download_command = 'sudo fc2-live-dl -x --wait-for-quality-timeout 15 %s ' % (args)
os.system(download_command)
