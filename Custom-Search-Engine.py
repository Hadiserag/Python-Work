#Indexer 
import os
import glob
from collections import defaultdict
import re

def create_inverted_index(docs_directory):
    inverted_index = defaultdict(set)
    for doc_path in glob.glob(f"{docs_directory}/*.txt"):
        doc_id = os.path.basename(doc_path)
        with open(doc_path, 'r') as file:
            for line in file:
                words = re.findall(r'\w+', line.lower())
                for word in words:
                    inverted_index[word].add(doc_id)
    return dict(inverted_index)

#Searcher
def search(query, inverted_index):
    words = query.lower().split()
    results = set()
    for word in words:
        if word in inverted_index:
            if not results:
                results = inverted_index[word]
            else:
                results = results.intersection(inverted_index[word])
    return results

#Ranker 
def rank_results(query, results, docs_directory):
    query_terms = set(query.lower().split())
    doc_scores = {}
    for doc_id in results:
        doc_path = f"{docs_directory}/{doc_id}"
        with open(doc_path, 'r') as file:
            text = file.read().lower()
            score = sum(text.count(term) for term in query_terms)
            doc_scores[doc_id] = score
    return sorted(doc_scores.items(), key=lambda item: item[1], reverse=True)

#Main
from indexer import create_inverted_index
from searcher import search
from ranker import rank_results

def main():
    docs_directory = input("Enter the path to the documents directory: ")
    inverted_index = create_inverted_index(docs_directory)
    while True:
        query = input("Enter search query (or 'exit' to quit): ")
        if query == 'exit':
            break
        results = search(query, inverted_index)
        ranked_results = rank_results(query, results, docs_directory)
        print("Search Results:")
        for doc_id, score in ranked_results:
            print(f"{doc_id} with score {score}")

if __name__ == "__main__":
    main()
