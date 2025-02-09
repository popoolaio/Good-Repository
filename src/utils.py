def read_data(file_path):
    with open(file_path, "r") as file:
        return file.read()
        
def process_data(data):
    return data.split()
