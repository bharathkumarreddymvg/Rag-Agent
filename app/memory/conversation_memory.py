memory = []

def add_memory(q, a):
    memory.append({
        "question": q,
        "answer": a
    })

def get_memory():
    return memory[-5:]