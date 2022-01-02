
def sort_by_name(arr):
    output = []
    num_words = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",
    }
    teens = {
        "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
        "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen",
    }
    tens = {
        "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
        "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety",
    }

    def double_digits(word: str):
        """
        takes in a double-digit string
        :return: word version of a number
        """
        if 0 <= int(word) <= 9:
            return num_words[word[-1]]
        if 10 <= int(word) < 20:
            return teens[word]
        if 19 < int(word) and word[-1] == '0':
            return tens[word[0]]
        if 19 < int(word):
            return tens[word[0]] + num_words[word[-1]]

    for n in arr:
        if len(str(n)) == 3:
            hundreds = num_words[str(n)[0]] + " hundred "
            if str(n)[-2:] != '00':
                word_output = hundreds + double_digits(str(n)[1:])
                output.append((n, word_output.strip()))
            else:
                output.append((n, hundreds.strip()))
        else:
            output.append((n, double_digits(str(n)).strip()))
    print(output)
    output.sort(key=lambda x: x[1])
    return [a for a, b in output]