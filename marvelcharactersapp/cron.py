# # myapp/management/commands/my_cron_job.py

# import logging
# from django.core.management.base import BaseCommand

# logger = logging.getLogger(__name__)

# class Command(BaseCommand):
#     help = 'This command runs the task that needs to be executed by the cron job.'

#     def handle(self, *args, **kwargs):
#         # Setup logging
#         logging.basicConfig(filename='cron_job.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#         try:
#             # Your code to be executed by the cron job
#             logger.info('Cron job started')
            
#             # Your actual task code here
            
#             logger.info('Cron job completed successfully')
#         except Exception as e:
#             logger.error('Error occurred: {}'.format(str(e)))

from django.http import HttpResponse
import os
import logging
from django.core.management import call_command
from django_cron import CronJobBase

logging.basicConfig(filename='/path/to/cron_job.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)




def restart_server():
    # Code to restart the server
    os.system('sudo systemctl restart your_server_service')

class RestartServerCronJob(CronJobBase):
    RUN_EVERY_MINS = 28 * 60  # Run every 28 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'marvelcharactersapp.cron.restart_server'  # Code to execute

    def do(self):
        try:
            logger.info('Cron job started')
            restart_server()
            logger.info('Cron job completed successfully')
        except Exception as e:
            logger.error('Error occurred: {}'.format(str(e)))