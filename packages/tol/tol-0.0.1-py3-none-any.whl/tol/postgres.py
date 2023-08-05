ADMIN_USER = 'postgres'


def query(query: str, port=5432, db_name: str=None, user: str=None) -> str:
    return 'psql --host=127.0.0.1{port}{user}{command}{dbname}'.format(
        port=' --port=%s' % port,
        user=' --user=%s' % user if user else '',
        command=' --command="%s"' % query,
        dbname=' %s' % db_name if db_name else '')
