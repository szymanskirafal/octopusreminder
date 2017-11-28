from celery import shared_task

@shared_task
def thing_task_print():
    print('---------------- hej its celery task here ----------------')



@shared_task
def thing_second_task():
    print('---------------- hej its second task  ----------------')


@shared_task
def task_numbers(one, two):
    print('---------------- hej its test task with nbrs: ', one, two)
    numbers = [one, two]
    return numbers
