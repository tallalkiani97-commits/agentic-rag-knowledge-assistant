"""Agentic RAG Knowledge Assistant CLI."""
import sys
from rag_core import answer

def main():
    query=" ".join(sys.argv[1:]).strip() or "What skills and projects are in the portfolio?"
    print("[plan] Identify the user's knowledge request")
    print("[retrieve] Search indexed Markdown sources")
    response,evidence=answer(query)
    print("\nAnswer\n"+response)
    print("\nEvidence")
    if not evidence:
        print("No matching evidence found.")
    for number,(score,doc,terms) in enumerate(evidence,1):
        print(f"[{number}] {doc['source']} · chunk {doc['chunk']} · score {score:.2f}")
        print("    "+doc["text"].replace("\n"," ")[:220])
    print("\n[generate] Answer grounded in retrieved evidence")

if __name__ == "__main__": main()
