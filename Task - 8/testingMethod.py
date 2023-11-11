import chromadb
 
client = chromadb.HttpClient(host='184.72.120.65',port=8080)
chat_news_collection = client.get_collection(name='news')
 
def get_relevant_docs(search_query):
    chroma_db_result = chat_news_collection.query(query_texts=search_query,n_results=8,)
    return chroma_db_result
 
search_query = " "
chroma_result = get_relevant_docs(search_query)
print(chroma_result)
