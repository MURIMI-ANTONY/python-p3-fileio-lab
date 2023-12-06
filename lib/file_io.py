def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w" ) as log_file:
        log_file.write(file_content)
    

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a" ) as log_file:
        log_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt") as log_file:
        return log_file.read()
