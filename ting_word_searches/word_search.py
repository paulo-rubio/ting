def exists_word(word, instance):
    all = instance.self()
    word = word.lower()
    result = []
    for data in all:
        occurrences = []
        for i, line in enumerate(data["linhas_do_arquivo"]):
            if word in line.lower():
                occurrences.append({"linha": i + 1})
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return result
    
def search_by_word(word, instance):
    """Aqui irá sua implementação"""
