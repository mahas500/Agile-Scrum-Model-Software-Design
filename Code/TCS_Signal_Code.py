# Please place the text files signal1.txt, signal2.txt and signal3.txt at the same path and directory as that of this file.
# Output files will be generated in the same path
# Output_Signals.txt is the file which contains valid signal transition entries
# Error_signals.txt is the file which contains invalid or error signal transition entries
def main():
    file1 = open("signal1.txt", "r")
    file2 = open("signal2.txt", "r")
    file3 = open("signal3.txt", "r")

    combined = file1.read()+file2.read()+file3.read()
    valid = ""
    invalid =""
    for line in combined.split('\n'):
        cols = line.split(' ')

        if len(line) > 1 and cols[2] == 'From' and cols[3] == 'To':
            valid = valid + line + '\n'
            invalid = invalid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Red' and cols[3] == 'Green' and cols[4] =='0':
            valid = valid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Red' and cols[3] == 'Red' and cols[4] =='1':
            valid = valid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Green' and cols[3] == 'Red' and cols[4] == '1':
            valid = valid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Red' and cols[3] == 'Red' and cols[4] == '0':
            invalid = invalid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Green' and cols[3] == 'Amber' and cols[5] == '0':
            valid = valid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Green' and cols[3] == 'Amber' and cols[5] == '1':
            invalid = invalid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Red' and cols[3] == 'Green' and cols[4] == '1':
            invalid = invalid + line + '\n'
        elif len(line) > 1 and cols[2] == 'Green' and cols[3] == 'Red' and cols[4] == '0':
            invalid = invalid + line + '\n'


    fileValid = open('Output_signal.txt', 'w')
    fileInvalid = open('Error_signals.txt','w')

    fileValid.write(valid)
    fileInvalid.write(invalid)
    file1.close()
    file2.close()
    file3.close()
    fileValid.close()
    fileInvalid.close()

if __name__ == "__main__":
    main()