__version__ = '2'
import faiss
import math


memory = {}


def add_vecs(vecs, indexed = True):
    d = len(vecs[0])
    if indexed:
        num_centroids = int(math.log(len(vecs), 2))
        memory['index'] = faiss.IndexIVFFlat(
            faiss.IndexFlatL2(d), d, num_centroids)
        memory['index'].train(vecs)
    else:
        memory['index'] = faiss.IndexFlatL2(d)
    memory['index'].add(vecs)


def add_ids(ids):
    memory['ids'] = ids


def search(vec, num_results=25):
    if num_results == -1:
        num_results = len(memory['ids'].keys())
    Dists, Ids = memory['index'].search(vec, num_results)
    results = []
    if 'ids' in memory:
        for i in range(num_results):
            results.append([
                memory['ids'][Ids[0][i]],
                Dists[0][i]
            ])
    else:
        for i in range(num_results):
            results.append([
                Ids[0][i],
                Dists[0][i]
            ])
    return results
