"""Small, explainable retrieval and grounded synthesis core."""
from pathlib import Path
import re

STOP = {"the","and","for","with","that","this","what","does","which","from","are","use"}

def words(text):
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP}

def load_documents(folder="sample_docs"):
    docs=[]
    for path in sorted(Path(folder).glob("*.md")):
        text=path.read_text(encoding="utf-8")
        for index, chunk in enumerate(re.split(r"\n\s*\n", text)):
            if chunk.strip(): docs.append({"source":str(path),"chunk":index+1,"text":chunk.strip()})
    return docs

def retrieve(query, docs, top_k=3):
    q=words(query)
    ranked=[]
    for doc in docs:
        overlap=q & words(doc["text"])
        score=len(overlap) / max(1, len(q))
        ranked.append((score, doc, sorted(overlap)))
    return [(score,doc,terms) for score,doc,terms in sorted(ranked,key=lambda item:item[0],reverse=True)[:top_k] if score>0]

def generate_answer(query, evidence):
    if not evidence:
        return "I could not find supporting evidence in the indexed knowledge base."
    terms=sorted({term for _,_,terms in evidence for term in terms})
    return (f"The indexed knowledge base contains evidence related to: {', '.join(terms)}. "
            "This grounded baseline returns the relevant passages below; an LLM adapter can synthesize a richer answer from the same evidence pack.")

def answer(query):
    docs=load_documents(); evidence=retrieve(query,docs)
    return generate_answer(query,evidence), evidence
