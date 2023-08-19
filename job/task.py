#
#
from time import sleep
import traceback
import random
from celery import current_task
from celery import states
from celery.exceptions import Ignore

from celery_app import celery_app
from conf.conf_celery import TIME_LIMIT, SOFT_TIME_LIMIT



def dummy_random_process():
    """Background task that runs a long function with progress reports."""
    verb = ['scanning', 'checking', 'analyzing', 'loading', 'verifying']
    adjective = ['very-far', 'far', 'near', 'reference']
    noun = ['tensorflow', 'segy', 'well']
    msg = '... {0} {1} {2} ...'.format(random.choice(verb), random.choice(adjective), random.choice(noun))

    if (len(msg)) <= 0 :
        msg = '... processing inference fraud ...'

    return msg


@celery_app.task(name='hello.task', bind=True, soft_time_limit=SOFT_TIME_LIMIT, time_limit=TIME_LIMIT)
def hello_world(self, num, name):
    try:
        msg = dummy_random_process()
        print(msg)
        for i in range(num):
            sleep(1)
            self.update_state(
                state='PROGRESS',
                meta={
                    'done': i,
                    'total': num,
                    'msg': msg
                }
            )

        return {
            "result": "hello {}".format(str(name)),
            "msg": msg
        }
    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n')
            })
        raise ex
