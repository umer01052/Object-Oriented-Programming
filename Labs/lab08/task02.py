file1=open("grades.txt","r")
file2=open("grades2.txt","w")
leng=(file1.read())
def read_file(file_path):
    records = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            record = line.replace('\n', '').split()
            records.append(record)
    return records

def write_file(file_path, records):
    with open(file_path, 'w') as file:
        for record in records:
            line = ' '.join(record) + '\n'
            file.write(line)

def correct_data(records):
    
    for i in range(len(records)):
        for j in range(len(records[i])):
            if records[i][j] == 'AB':
                records[i][j] = '0'
    
    return records

def update_file(original_path, corrected_data):
    original_data = read_file(original_path)

    for i in range(len(original_data)):
        if original_data[i] != corrected_data[i]:
            original_data[i] = corrected_data[i]

    write_file(original_path, original_data)

