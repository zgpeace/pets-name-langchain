import os
import pinecone

# get api key from app.pinecone.io
api_key = os.environ.get('PINECONE_API_KEY') or 'YOUR_PINECONE_API_KEY'
# find your environment next to the api key in pinecone console
env = os.environ.get('PINECONE_ENVIRONMENT') or 'YOUR_PINECONE_ENVIRONMENT'

pinecone.init(api_key=api_key, environment=env)

# Giving our index a name
index_name = "quickstart"
# Delete the index, if an index of the same name already exists
if index_name in pinecone.list_indexes():
    pinecone.delete_index(index_name)
    
pinecone.create_index(index_name, dimension=8, metric="euclidean")
describe_index = pinecone.describe_index(index_name)
print('describe_index >> ', describe_index)

index = pinecone.Index(index_name)

index.upsert(
  vectors=[
    {"id": "vec1", "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},
    {"id": "vec2", "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]},
    {"id": "vec3", "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
    {"id": "vec4", "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]}
  ],
  namespace="ns1"
)

index.upsert(
  vectors=[
    {"id": "vec5", "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]},
    {"id": "vec6", "values": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
    {"id": "vec7", "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]},
    {"id": "vec8", "values": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]}
  ],
  namespace="ns2"
)

index_response = index.describe_index_stats()
print('index_response >> ', index_response)

# Returns:
# {'dimension': 8,
#  'index_fullness': 8e-05,
#  'namespaces': {'ns1': {'vector_count': 4}, 'ns2': {'vector_count': 4}},
#  'total_vector_count': 8}

query_ns1 = index.query(
  namespace="ns1",
  vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
  top_k=3,
  include_values=True
)
print('query_ns1 >> ', query_ns1)

query_ns2 = index.query(
  namespace="ns2",
  vector=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
  top_k=3,
  include_values=True
)
print('query_ns2 >> ', query_ns2)

# Returns:
# {'matches': [{'id': 'vec3',
#               'score': 0.0,
#               'values': [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
#              {'id': 'vec4',
#               'score': 0.0799999237,
#               'values': [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
#              {'id': 'vec2',
#               'score': 0.0800000429,
#               'values': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]}],
#  'namespace': 'ns1'}
# {'matches': [{'id': 'vec7',
#               'score': 0.0,
#               'values': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]},
#              {'id': 'vec6',
#               'score': 0.0799999237,
#               'values': [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
#              {'id': 'vec8',
#               'score': 0.0799999237,
#               'values': [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]}],
#  'namespace': 'ns2'}

pinecone.delete_index(index_name)