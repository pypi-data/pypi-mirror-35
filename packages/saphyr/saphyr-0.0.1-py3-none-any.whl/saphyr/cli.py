import click

from saphyr import dev
from yoyo import read_migrations
from yoyo import get_backend


def run_server(config, app, bootstrap):
    bootstrap()
    app.run(
        host=config["endpoint"]['http']['host'],
        port=config["endpoint"]['http']['port'],
        debug=True if config["env"] == "dev" else False
    )


def create_cli(config, app, bootstrap):
    @click.group()
    def main():
        """
        Saphyr Skeleton CLI
        """
        pass

    @main.command()
    @click.option('--server-only', default=0, help='Only start the server without tools')
    def start(server_only):
        if config["env"] == "dev" and not server_only:
            dev.start_watchers(config["endpoint"]["watchers"])
            dev.start_dev_server('./', config["endpoint"]['http']['port'])
        else:
            run_server(config, app, bootstrap)

    @main.command()
    def migrate():
        bootstrap()
        backend = get_backend(config["databases"]['postgres']['url'])
        migrations = read_migrations('./migrations')
        with backend.lock():
            backend.apply_migrations(backend.to_apply(migrations))

    @main.command()
    def rollback():
        bootstrap()
        backend = get_backend(config["databases"]['postgres']['url'])
        migrations = read_migrations('./migrations')
        with backend.lock():
            backend.rollback_migrations(backend.to_rollback(migrations))

    return main()
