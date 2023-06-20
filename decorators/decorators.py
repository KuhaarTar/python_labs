import logging
from lab8.exception.exceptions import NotMatchingModeException


def registerer(method):
    file_path = "C:\\Users\\taras\\PycharmProjects\\pythonProject\\reg_file.txt"

    def wrapper(*args, **kwargs):
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            found = False
            for i in range(len(lines)):
                if lines[i].startswith(method.__name__):
                    count = int(lines[i].split(':')[1].strip()) + 1
                    lines[i] = f'{method.__name__}: {count}\n'
                    found = True
                    break
            if not found:
                lines.append(f'{method.__name__}: 1\n')
            file.writelines(lines)
            file.truncate()
        result = method(*args, **kwargs)
        return result

    return wrapper


def result_to_file(input_func):
    def result_writer(*args, **kwargs):
        result = input_func(*args, **kwargs)
        file_name = input_func.__qualname__
        file = open(f"{file_name}.txt", "a")
        for item in list(result):
            file.write(str(item) + "\n")
        file.close()
        return result

    return result_writer


def exception_logging(exception, mode):
    list_of_modes = {"file", "console"}

    def decorator(input_func):
        def wrapper(*args, **kwargs):
            try:
                return input_func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(str(e))
                elif mode == "file":
                    logging.basicConfig(level=logging.INFO, filename="exception_log.log")
                    logging.error(str(e))
                else:
                    raise NotMatchingModeException()
        return wrapper
    return decorator