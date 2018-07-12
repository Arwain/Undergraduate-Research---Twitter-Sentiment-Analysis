import re
import csv

DATE_IDENTIFIER = "2018-04-"
DATE_IDENTIFIER2 = "2018-05-" # TODO: Fixed but code is redundant


def main():
    timestamp = ""
    tweet = ""
    infile = open("korean_summit_data.txt", "r")
    mydata = ['DATE', 'TWEET', 'COMPOUND', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']
    for line in infile:

        if line[0:8] == DATE_IDENTIFIER:
            timestamp = line
            filename = timestamp[:13] + '.csv'
            filename = ''.join(filename)
            print(filename)
            outfile = open(filename, "w")
            writer = csv.writer(outfile)
            mydata = ['DATE', 'TWEET', 'COMPOUND', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']
            writer.writerow(mydata)

        if line[0:8] == DATE_IDENTIFIER2:
            timestamp = line
            filename = timestamp[:13] + '.csv'
            filename = ''.join(filename)
            print(filename)
            outfile = open(filename, "w")
            writer = csv.writer(outfile)
            mydata = ['DATE', 'TWEET', 'COMPOUND', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']
            writer.writerow(mydata)

        elif line == '\n':
            continue
        elif line[0:9] == "compound:":
            analysis = line
            # print(analysis)
            regex = re.sub(r"([a-z]|\,|\:)", '', analysis)
            analysis = ''.join(regex)
            regex = re.findall(r"[-+]?\d*\.\d+|\d+", analysis)

            # print(regex)
            mydata[0] = timestamp
            mydata[1] = tweet
            mydata[2] = regex[0]
            mydata[3] = regex[1]
            mydata[4] = regex[2]
            if len(regex) > 3:
                mydata[5] = regex[3]
            else:
                mydata[5] = 0.0
            writer.writerow(mydata)
        else:
            tweet = line


main()
