from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    informations = []
    for index in range(len(instance)):
        data = instance.search(index)
        lines = []
        for position, line in enumerate(data["linhas_do_arquivo"]):
            if word.casefold() in line.casefold():
                lines.append(
                    {
                        "linha": position + 1,
                    }
                )
        if len(lines) > 0:
            informations.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": lines,
                }
            )
    return informations


def search_by_word(word, instance: Queue):
    informations = []
    for index in range(len(instance)):
        data = instance.search(index)
        lines = []
        for position, line in enumerate(data["linhas_do_arquivo"]):
            if word.casefold() in line.casefold():
                lines.append(
                    {
                        "linha": position + 1,
                        "conteudo": line,
                    }
                )
        if len(lines) > 0:
            informations.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": lines,
                }
            )
    return informations
