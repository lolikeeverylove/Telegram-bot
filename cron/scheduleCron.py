from crontab import CronTab

my_cron = CronTab(user='roy')
job = my_cron.new(command='python /home/roy/writeDate.py')
job.minute.every(1)

my_cron.write()