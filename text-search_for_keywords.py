__author__ = 'Perkel'


class ReadTextFile():
    def __init__(self, text_file):
        self.whole_text = text_file.read().split('\n')

    def print_text(self):
        print ''
        print "====WHOLE FILE======"
        for line in self.whole_text:
            print line
        print "===================="
        print ''

    def print_events_list(self):
        print ''
        print "========EVENTS=========="
        count = 0
        for line in self.whole_text:
            count += 1
            if "EVENT" in line:
                print line, "line :", count
        print "========================"
        print ''



crs = open("data/text/key_word_test.txt", "r")

categorized_text_file = ReadTextFile(crs)

categorized_text_file.print_text()
categorized_text_file.print_events_list()