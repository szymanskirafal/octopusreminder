from celery import shared_task

@shared_task
def task_printing(self):
    print('---------------- hej its celery task here ----------------')
