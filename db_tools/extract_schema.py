import argh
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
import json


@argh.arg('uri', help='<dialect>://[<user>:<password>@]<host>/<db>')
@argh.arg('table', help='table name')
def extract_table(args):
    table_name = args.table
    engine = create_engine(args.uri)
    conn = engine.connect()
    insp = reflection.Inspector.from_engine(engine)
    table_info = insp.get_columns(table_name)
    [(c['name'], c['type'], c['type']) for c in table_info]
    schema = {}
    for c in table_info:
        s = str(c['type'])
        type_string = None
        if s.startswith('INTEGER'):
            type_string = 'count'
        elif s.startswith('DECIMAL'):
            type_string = 'real'
        elif s.startswith('VARCHAR') or s.startswith('TEXT'):
            type_string = 'categorical'
        if type_string:
            schema[c['name']] = {'type': type_string}
        else:
            print c['type'], 'not recognized'
    print json.dumps(schema, indent=2)


def main():
    parser = argh.ArghParser()
    parser.add_commands([extract_table])
    parser.dispatch()


if __name__ == '__main__':
    main()
