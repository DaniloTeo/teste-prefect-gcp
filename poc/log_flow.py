from prefect.task_runners import ConcurrentTaskRunner
from prefect import flow, task, get_run_logger


@task
def extract():
    return [1, 2, 3]


@task
def transform(x):
    return [i * 10 for i in x]


@task
def load(y):
    logger = get_run_logger()
    logger.info("Received y: {}".format(y))

@flow(task_runner=ConcurrentTaskRunner)
def etl():
    e = extract()
    t = transform(e)
    l = load(t)
