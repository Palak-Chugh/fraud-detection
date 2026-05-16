memory_store = []

def save_case(case_data):

    memory_store.append(case_data)

def retrieve_similar_cases(query):

    results = []

    for case in memory_store:

        if query.lower() in str(case).lower():
            results.append(case)

    return results[:3]