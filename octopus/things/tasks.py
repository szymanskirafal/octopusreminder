from celery import shared_task

@shared_task
def thing_task_print():
    print('---------------- hej its celery task here ----------------')



@shared_task
def thing_second_task():
    print('---------------- hej its second task  ----------------')


@shared_task
def test(one, two):
    print('---------------- hej its test task with nbrs: ', one, two)
