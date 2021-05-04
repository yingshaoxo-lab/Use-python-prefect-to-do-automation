from prefect import task, Flow, Parameter
from datetime import timedelta
from prefect.schedules import IntervalSchedule

@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))

schedule = IntervalSchedule(interval=timedelta(minutes=1))

with Flow("my first flow", schedule) as flow:
    #name = Parameter("person_name")
    say_hello("yingshaoxo")

#flow.run(person_name="yingshaoxo")
flow.register(project_name="test1")
