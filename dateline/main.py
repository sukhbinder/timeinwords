from dateline import DateLine, TimeInWords
import time

def main():
    test = DateLine()
    print (test)

    

def main_tw():
    while True:
        try:
            test = TimeInWords()
            print(test, end="\r")
            time.sleep(10)
        except KeyboardInterrupt:
            raise

if __name__ == '__main__':
    test = DateLine()
    print (test)