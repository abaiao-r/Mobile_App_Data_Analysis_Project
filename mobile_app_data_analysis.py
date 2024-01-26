
import csv

def explore_data(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end];
    for i in dataset_slice:
        print(i);
        print("\n");
        
    if rows_and_columns:
        print("Number of rows: ", len(dataset));
        print("Number of columns: ", len(dataset[0]));
        
def open_csv(file_name):
    csv_file = open(file_name, enconding="utf-8");
    csv_reader = csv.reader(csv_file);
    data = [row for row in csv_reader];
    csv_file.close();
    return (data);