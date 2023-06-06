from .file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return print(f"Arquivo {path_file} já foi processado.")
    lines = txt_importer(path_file)
    data = dict(
            nome_do_arquivo=path_file,
            qtd_linhas=len(lines),
            linhas_do_arquivo=lines
        )
    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
