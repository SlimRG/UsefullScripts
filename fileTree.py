import os

def print_tree(directory, indent=""):
    """
    Выводит содержимое директории в древовидном формате.

    :param directory: Путь к директории.
    :param indent: Отступ для вложенных элементов.
    """
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        print(f"{indent}[Недоступно: {directory}]")
        return

    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = index == len(entries) - 1

        # Определяем символы для веток
        branch = "└── " if is_last else "├── "
        continuation = "    " if is_last else "│   "

        # Печатаем текущий элемент
        print(f"{indent}{branch}{entry}")

        # Если это директория, рекурсивно вызываем функцию
        if os.path.isdir(path):
            print_tree(path, indent + continuation)


# Пример использования
if __name__ == "__main__":
    root_directory = input("Введите путь к директории: ").strip() or "."
    print(f"Содержимое директории '{root_directory}':")
    print_tree(root_directory)
