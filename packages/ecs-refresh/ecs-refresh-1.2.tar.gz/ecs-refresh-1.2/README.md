# ecs-refresh
Python tool for kicking off blue/green deploys on Amazon ECS 
(Fargate support added 06.15.2018)

# Usage

To Install:

```
pip install ecs-refresh
```

Example of usage:

```
user@host:/$ ecs-refresh
Usage: ecs-refresh [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  deploy
  rollback

```

To deploy a refresh of "MyService" on ECS Cluster "MyCluster" for example:
```
user@host:/$ ecs-refresh deploy --cluster MyCluster --service MyService
```

