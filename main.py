import pandas as pd
import argparse
import json

from google.cloud import spanner


def run_bash_query(db, table_id, batch_file):
    with db.batch() as batch:
        batch.insert(
            table=table_id,
            columns=batch_file.columns,
            values=batch_file.values.tolist()
        )


def get_file(file_path, format_path=None, chunksize=None):
    format_file = json.load(open(format_path, "r")) if format_path else None
    return pd.read_csv(file_path, dtype=format_file, chunksize=chunksize)


def initialize_spanner(instance_id, database_id):
    return spanner.Client().instance(instance_id).database(database_id)


def main(instance_id, database_id, table_id, file_path, format_path=None, chunksize=None):

    db = initialize_spanner(instance_id, database_id)

    if chunksize < 0:
        file = get_file(file_path, format_path)
        run_bash_query(db, table_id, file)
    else:
        for file in get_file(file_path, format_path, chunksize):
            run_bash_query(db, table_id, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--instance_id', help='Cloud Spanner instance-id.')
    parser.add_argument(
        '--database_id', help='Cloud Spanner database-id.')
    parser.add_argument(
        '--table_id', help='Cloud Spanner table-id.')
    parser.add_argument(
        '--file_path', help='CSV file containing data.')
    parser.add_argument(
        '--format_path', help='JSON containing the configuration of dtypes.')
    parser.add_argument(
        '--chunksize', help='Number of row per chunk.', type=int, default=-1)

    args = parser.parse_args()

    main(
        instance_id=getattr(args, "instance_id"),
        database_id=getattr(args, "database_id"),
        table_id=getattr(args, "table_id"),
        file_path=getattr(args, "file_path"),
        format_path=getattr(args, "format_path"),
        chunksize=getattr(args, "chunksize")
    )
