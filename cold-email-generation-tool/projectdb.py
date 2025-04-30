import chromadb
try:
    client = chromadb.Client()
    collection = client.create_collection(name="my_collection")
    print("Connection Established")
except:
  print("An exception occurred")

collection.add(
   documents=[
      'This document is about NewYork',
      'This document is about Delhi'
   ],
   ids=['id1', 'id2']
)
all_docs = collection.get()
#print(all_docs)

results = collection.query(
   query_texts=['Query is about Startups'],
   n_results=2
)
print(results)
try:
   
   collection.delete(ids=all_docs['ids'])
   collection.get()
   print("deleted")

except:
   print("does not exist")

