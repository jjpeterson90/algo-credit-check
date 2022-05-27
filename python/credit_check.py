def credit_check(credit_number):
    credit_number = ([int(n) for n in credit_number])
    credit_number.reverse()
    final_sum = 0
    for num in range(1, len(credit_number), 2):
        credit_number[num] *= 2
        if credit_number[num] > 9:
            sum_of_digits = 0
            for digit in str(credit_number[num]):
                sum_of_digits += int(digit)
            credit_number[num] = sum_of_digits
    for num in credit_number:
        final_sum += num
    if final_sum % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"


#print(credit_check('5541808923795240'))

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

