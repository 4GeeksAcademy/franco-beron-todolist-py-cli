import csv
import os

tasks = []
FILE_NAME = "todos.csv"


def add_one_task(title):
    title = title.strip()

    if title:
        tasks.append(title)


def print_list():
    if not tasks:
        print("No hay tareas pendientes.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(number_to_delete):
    try:
        number = int(number_to_delete)
    except (ValueError, TypeError):
        print("Posición inválida.")
        return

    if number < 1 or number > len(tasks):
        print("Posición inválida.")
        return

    deleted = tasks.pop(number - 1)
    print(f"Tarea eliminada: {deleted}")


def save_todos():
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for task in tasks:
            writer.writerow([task])

    print(f"Tareas guardadas en {FILE_NAME}.")


def load_todos():
    tasks.clear()

    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if row:
                tasks.append(row[0])


def show_help():
    print("Comandos disponibles:")
    print("  add <tarea>     Agregar una tarea")
    print("  list            Mostrar tareas")
    print("  delete <n>      Eliminar tarea por posición")
    print("  save            Guardar tareas")
    print("  load            Cargar tareas")
    print("  help            Mostrar ayuda")
    print("  exit            Salir")


def main():
    load_todos()

    print("Gestor de tareas")
    print("Escribe 'help' para ver los comandos.")

    while True:
        try:
            command = input("> ").strip()
        except EOFError:
            print()
            break

        if not command:
            continue

        parts = command.split(maxsplit=1)
        action = parts[0].lower()

        if action == "add":
            if len(parts) < 2 or not parts[1].strip():
                print("Debes indicar el título de la tarea.")
                continue

            add_one_task(parts[1])
            print("Tarea agregada.")

        elif action == "list":
            print_list()

        elif action == "delete":
            if len(parts) < 2:
                print("Debes indicar la posición de la tarea.")
                continue

            delete_task(parts[1])

        elif action == "save":
            save_todos()

        elif action == "load":
            load_todos()
            print("Tareas cargadas.")

        elif action == "help":
            show_help()

        elif action in ("exit", "quit"):
            break

        else:
            print("Comando desconocido. Escribe 'help' para ver las opciones.")


if __name__ == "__main__":
    main()
