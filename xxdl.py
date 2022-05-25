import os

url = os.getenv("URL")
audio_only = os.getenv("AUDIO_ONLY")

args = '--threads 8 --wait  -o "output/(%(channel_id)s)_[%(date)s]_%(channel_name)s_%(title)s.%(ext)s" ' + url

if audio_only == 'true':
  download_command = 'sudo fc2-live-dl --quality sound %s ' % (args)
else:
  download_command = 'sudo fc2-live-dl -x --wait-for-quality-timeout 15 %s ' % (args)

os.system(download_command)
