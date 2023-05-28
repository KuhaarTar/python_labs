def registerer(input_func):
    number_of_calls = 1
    file_path = "C:\\Users\\taras\\PycharmProjects\\pythonProject\\reg_file.txt"
    register_str = f"\n[ Name:  {input_func.__name__}, number of calls: {number_of_calls} ]\n"
    file = open(file_path, "a")
    file.write(register_str)
    file.close()

    return input_func


def result_to_file(input_func):
    def result_writer(*args, **kwargs):
        result = input_func(*args, **kwargs)
        file_name = input_func.__qualname__
        file = open(f"C:\\Users\\taras\\PycharmProjects\\pythonProject\\{file_name}.txt", "a")
        for item in list(result):
            file.write(str(item) + "\n")
        file.close()
        return result
    return result_writer

