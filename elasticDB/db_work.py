from elasticsearch import Elasticsearch


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def elastic_db_works(data):
    # Creat or Update DB
    if es.indices.exists(index='leaks'):
        update_elastic(data)
    else:
        put_elastic_db(data)


def put_elastic_db(data):
    # Creating and filling the base
    i = 1
    for elem in data:
        es.index(index='leaks', doc_type='_doc', id=i, body=elem)
        i += 1
    print('Safe to DB!')


def update_elastic(data):
    # Update data in DB if index already exist
    es_all = es.search(index='leaks', size=10000)
    last_id = es_all['hits']['total']['value']
    in_base = True
    for elem in data:
        for elem2 in es_all['hits']['hits']:
            if elem['title'] == elem2['_source']['title']:
                if elem == elem2['_source']:
                    # If in DB and no changes
                    in_base = True
                    print(f'Already in DB! ID = {elem2["_id"]}')
                    break
                else:
                    # If in DB but change
                    in_base = True
                    es.index(index='leaks', doc_type='_doc', id=elem2['_id'], body=elem)
                    print(f'Update in DB! ID = {elem2["_id"]}')
                    break
            else:
                in_base = False
        if not in_base:
            # New post
            es.index(index='leaks', doc_type='_doc', id=last_id+1, body=elem)
            print(f'Safe to DB New! ID = {last_id+1}')
            last_id += 1
