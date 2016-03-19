__author__ = 'Perkel'

import re


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
        event_list = []
        print ''
        print "========EVENTS=========="
        line_number = 0
        for line in self.whole_text:
            line_number += 1
            if "EVENT" in line:
                event = self.find_text_between_brackets(line)
                event_list.append((event, line_number))
                print event, "line :", line_number
        print "========================"
        print ''

        return event_list

    def find_text_between_brackets(self, line):
        result = re.search(r'\[(.*)\]', line).group(1)
        return result

    def print_event(self, event_name):
        events = self.print_events_list()

        count = -1

        print_start = None
        print_end = None

        next_event = None

        for event in events:
            count += 1
            if event_name in event[0]:
                print_start = event[1]+3
                next_event = count + 1

        print_end = events[next_event]
        print_end = print_end[1]
        print "==========="
        print print_start
        print print_end
        print "==========="

        count2 = 0
        print ''
        print "=========EVENT========="
        full_event = []
        for x in self.whole_text:
            count += 1
            if count >= print_start and count <= print_end:
                if x != '':
                    full_event.append(x)

        for line in full_event:
            print line.lstrip()

        print "=========EVENT========="





        if count == 1:
            print "There is such a file"
        else:
            print "No such event"






crs = open("data/text/key_word_test.txt", "r")

categorized_text_file = ReadTextFile(crs)


categorized_text_file.print_events_list()
categorized_text_file.print_event("st002")