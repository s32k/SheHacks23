from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def getComparision(refText, userText): 
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    #Encoding:
    comp = model.encode([refText, userText])

    #let's calculate cosine similarity:
    return((cosine_similarity([comp[0]], comp[1:])[0][0])*100//10)
