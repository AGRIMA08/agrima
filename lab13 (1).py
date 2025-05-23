import csv
def read_data(file_path):
    mclass=[]
    mgrade=[]
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['grade_level']=="":
                mentor_class = row['mentor_class']
                mentor_grade = row['mentor_grade']
                judge = row['judge'].strip().lower()
                if mentor_class not in mclass:
                    mclass.append(mentor_class)
                if judge=="true":
                    mgrade.append(mentor_grade)
    return mclass,mgrade
def detect_errors(mclass,mgrade):
    errors = []
    classes=["6A", "6B", "6C","7A", "7B", "7C","8A", "8B", "8C","9A", "9B", "9C","10A", "10B", "10C","11A", "11B", "11C",
    "12A", "12B", "12C"
]
    grade=["6","7","8","9","10","11","12"]
    for i in mclass:
        if i in classes:
            classes.remove(i)
    for j in mgrade:
        if j in grade:
            grade.remove(j)
    for k in classes:
            errors.append(f"Class {k}: Error TEACHER not found.")
    for l in grade:
            errors.append(f"Class {l}: Error JUDGE not found.")  
    return errors
def write_errors_to_file(errors, output_file):
    with open(output_file, mode='w') as file:
        for error in errors:
            file.write(error + "\n")
def main():
    input_file = 'generated_data.csv'
    output_file = 'errors.txt'
    mclass,mgrade= read_data(input_file)
    errors = detect_errors(mclass,mgrade)
    write_errors_to_file(errors, output_file)
main()