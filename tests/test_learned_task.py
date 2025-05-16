from axiomcore.task_learner import learn_task
from axiomcore.task_dispatcher import dispatch_task

# Step 1: Learn a new task dynamically
learn_task(
    name="say_hello",
    description="Prints a hello message.",
    code="""
def say_hello():
    print('Hello from a learned task!')
"""
)

# Step 2: Dispatch it to validate execution
dispatch_task("say_hello")
