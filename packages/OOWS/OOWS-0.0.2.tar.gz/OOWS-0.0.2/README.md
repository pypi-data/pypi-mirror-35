# OOWS

**Warning — this project is in early development. Contributions and feedbacks are welcome. Usage in production systems is discouraged**

OOWS (_oh-owls_) is an object-oriented friendly client for Amazon Web Services — AWS. It is based on [boto3](https://github.com/boto/boto3) official client and aims to provide a cleaner and more Pythonic interface to handle AWS resources.

Currently, Boto3 already provides [the Resource Model](https://boto3.readthedocs.io/en/latest/reference/core/resources.html) which is a nicer and more OO-friendly interface over raw JSON, [as explained here](https://github.com/boto/boto3/issues/112#issuecomment-100377492). Although it works, it does not provide an interface for resources I currently need. This project started by a personal need of mine to ease the current state of programmatic access to ECS resources.

## Rationale

Suppose you want to list all of a cluster's services' task definitions. Using pure `boto3`, you'd need to write something like:

```python
session = boto3.Session()
ecs_client = session.client('ecs')
services = ecs_client.list_services(cluster="MyCluster")['serviceArns']
for service in services:
    s = ecs_client.describe_services(cluster="MyCluster", services=[service])
    print("The task definition is {}".format(s['services'][0]['taskDefinition']))
```

But using `oows`, you can rewrite this code to something like:

```python
cluster = Cluster("MyCluster")

for service in cluster.services:
    print("The task definition is {}".format(service.task_definition))
```
