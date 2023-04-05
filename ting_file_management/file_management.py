import os
import sys


def txt_importer(path_file):
    if not os.path.exists(path_file):
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []

    _, file_ext = os.path.splitext(path_file)
    if file_ext != ".txt":
        sys.stderr.write("Formato inválido\n")
        return []

    with open(path_file, "r") as f:
        lines = f.read().split("\n")

    return lines
