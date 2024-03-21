import time

def find_last_digits(reg_no):
    # Extract last 4 digits from the registration number
    last_digits = reg_no[-4:]

    # Check if the last 4 digits start with '0000' and end with '7073'
    if last_digits.startswith('0000') and last_digits.endswith('7073'):
        return True
    else:
        return False

def time_to_reach_7073():
    reg_no = '21MIC7073'

    # Loop to increment last 4 digits until reaching '7073'
    while not find_last_digits(reg_no):
        last_digits = int(reg_no[-4:])
        last_digits += 1
        reg_no = reg_no[:-4] + str(last_digits).zfill(4)
        time.sleep(1)  # Add a delay of 1 second for demonstration

    return reg_no

start_time = time.time()
result_reg_no = time_to_reach_7073()
end_time = time.time()

time_taken = end_time - start_time
print("Time taken to reach '7073':", time_taken, "seconds")
print("Resulting registration number:", result_reg_no)
