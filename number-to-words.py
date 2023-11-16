def convert_to_words(number):
    # Define lists for the words
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Function to convert a number less than 100 into words
    def convert_below_100(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + " " + ones[num % 10]

    # Function to convert a number less than 1000 into words
    def convert_below_1000(num):
        if num < 100:
            return convert_below_100(num)
        else:
            if num % 100 == 0:
                return ones[num // 100] + " hundred"
            else:
                return ones[num // 100] + " hundred and " + convert_below_100(num % 100)

    # Handle special case for zero
    if number == 0:
        return "zero"

    # Convert the number based on its magnitude (thousands, millions, etc.)
    result = ""
    magnitudes = ["", "thousand", "million", "billion", "trillion", "quadrillion"]
    magnitude_index = 0

    while number > 0:
        chunk = number % 1000
        if chunk != 0:
            result = convert_below_1000(chunk) + " " + magnitudes[magnitude_index] + " " + result
        number //= 1000
        magnitude_index += 1

    return result.strip()

# Get user input
try:
    number = int(input("Enter a number: "))
    if number < 0 or number == str:
        print("Please enter a non-negative number.")
    else:
        words = convert_to_words(number)
        print(f"{number} in words: {words.capitalize()}")
except ValueError:
    print("Please enter a valid number.")
