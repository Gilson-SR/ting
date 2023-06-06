from .file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return print(f"Arquivo {path_file} processado com sucesso.")
    lines = txt_importer(path_file)
    data = dict(
            nome_do_arquivo=path_file,
            qtd_linhas=len(lines),
            linhas_do_arquivo=lines
        )
    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return
    data_removed = instance.dequeue()
    name = data_removed["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {name} removido com sucesso\n")


def file_metadata(instance, position):
    data = None
    try:
        data = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
    sys.stdout.write(str(data))
