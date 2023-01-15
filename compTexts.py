from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#Write some lines to encode (sentences 0 and 2 are both ideltical):
sen = [
    "Three years later, the coffin was still full of Jello.",
    "The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.",
    "The person box was packed with jelly many dozens of months later.",
    "He found a leprechaun in his walnut shell."
]

model = SentenceTransformer('bert-base-nli-mean-tokens')
#Encoding:
sen_embeddings = model.encode(sen)
sen_embeddings.shape

#let's calculate cosine similarity for sentence 0:
cosine_similarity(
    [sen_embeddings[0]],
    sen_embeddings[1:]
)

para = "In The Sopranos, the mob is besieged as much by inner infidelity as it is by the federal government. Early in the series, the greatest threat to Tony's Family is his own biological family. One of his closest associates turns witness for the FBI, his mother colludes with his uncle to contract a hit on Tony, and his kids click through Web sites that track the federal crackdown in Tony's gangland."
phrase = "In the first season of The Sopranos, Tony Soprano’s mobster activities are more threatened by members of his biological family than by agents of the federal government. This familial betrayal is multi-pronged. Tony’s closest friend and associate is an FBI informant, his mother and uncle are conspiring to have him killed, and his children are surfing the Web for information about his activities."
comp = model.encode([para, phrase])
print((cosine_similarity([comp[0]], comp[1:])[0][0])*100//1)

para = "A man in New Jersey seemed to think leaving the scene of a car crash and being arrested was a better option than listening to his girlfriend yell. He told the police he fled because he didn’t want to listen to her yell at him."
phrase = "A 28 year old man in Austin, Texas didn’t break into a business and run, like most criminals. Instead, he took several sausages then simply fell asleep inside the business."
comp = model.encode([para, phrase])
print((cosine_similarity([comp[0]], comp[1:])[0][0])*100//1)