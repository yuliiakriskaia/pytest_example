from .postgres_operations import PostgresClient


def hello_world_write(sentence):
    sentence = sentence.capitalize()
    pgs_client = PostgresClient()

    pgs_client.write_data(sentence)


def hello_world_read():
    pgs_client = PostgresClient()
    return pgs_client.list_data()
