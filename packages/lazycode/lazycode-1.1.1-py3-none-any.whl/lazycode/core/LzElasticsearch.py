# pip install elasticsearch==5.5.3
from elasticsearch import Elasticsearch
from typing import List, Union, Dict


class lzElasticsearch(object):
    """
    index -> 数据库
    doc_type -> 数据表
    doc -> 数据行
    """
    ES = None

    def __init__(self, host_port: List[Dict] = [dict(host="127.0.0.1", port=9200)]) -> None:
        self.ES = Elasticsearch(host_port, timeout=60)

    def create_index(self, index: str, doc_type: str, data: Dict):
        self.ES.index(index=index, doc_type=doc_type, body=data)

    def search(self, index: str, doc_type: str, query: Dict):
        self.ES.search(index=index, doc_type=doc_type, body=query)

#
# # connect
# es = Elasticsearch([dict(host="127.0.0.1", port=9200)], timeout=60)
#
# # insert
# data = {
#     "id": 1,
#     "domainName": "tongfu.net",
#     "title": "同福主页 - 首页 - 同福网 - TONGFU.net"
# }
#
# es.index(index="tfse", doc_type="all_type", body=data)
#
# # query
# query = {
#     "query": {
#         "term": {
#             "id": 1
#         }
#     }
# }
# results = es.search(index="tfse", doc_type="all_type", body=query)
# print("查询到：" + str(results['hits']['total']) + "结果")
# for result in results['hits']['hits']:
#     id = result['_id']
#     data = result['_source']
#     print("[" + id + "] " + str(data['id']) + "," + data['domainName'] + "," + data['title'])
#
# es.search
