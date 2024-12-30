import csv


short_month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def returnnMonthAxisLabels(x_range):
    xCoords=range(1,x_range,round(x_range/12))
    xlabels = dict(zip(xCoords, short_month_names))
    return xlabels

   
def load_csv_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header
        for row in csvreader:
            data.append(int(row[2]))
    return data

def generate_increasing_numbers(start, end, count):
    numbers = [start]
    for _ in range(count - 2):
        next_number = numbers[-1] + random.randint(0, ((end - numbers[-1])%40) // count)
        numbers.append(next_number)
    numbers.append(end)
    return numbers
