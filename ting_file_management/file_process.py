import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for result in instance.queue:
        if result["nome_do_arquivo"] == path_file:
            return

    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    instance.enqueue(result)
    print(result)


def remove(instance):
    if instance.empty():
        print("Não há elementos")
        return
    data = instance.dequeue()
    print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
