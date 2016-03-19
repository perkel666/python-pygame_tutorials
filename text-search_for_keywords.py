__author__ = 'Perkel'

import re


class TextParsing():

    @ staticmethod
    def parse_text(text):
        text_copy = text
        new_text = []
        for line in text_copy:
            if line != '':
                parsed_line = line.lstrip()
                new_text.append(parsed_line)

        return new_text


class ReadTextFile():
    def __init__(self, text_file):
        self.whole_text = TextParsing.parse_text(text_file.read().split('\n'))

    def parse_text_file(self):
        text = TextParsing.parse_text(self.whole_text)
        return text

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

        """ Look for event in event list
            Once found decide start of event line and end of event line
        """

        print_start = None
        print_end = None

        next_event = None

        count = -1  # -1 because i need to get over list starting with 0 twice so -1 and not 0
        for event in events:
            count += 1
            if event_name in event[0]:
                print_start = event[1]+2
                next_event = count + 1

        print_end = events[next_event]
        print_end = print_end[1]-1
        print "==========="
        print print_start
        print print_end
        print "==========="

        count2 = 0
        print ''
        print "=========EVENT========="
        full_event = []
        for x in self.whole_text:
            count2 += 1
            if count2 >= print_start and count2 <= print_end:
                if x != '':
                    full_event.append(x)

        event_content = []
        for line in full_event:
            x = line.lstrip()
            event_content.append(x)
            print line.lstrip()

        print "=========EVENT========="

        print event_content

        return event_content












crs = open("data/text/key_word_test.txt", "r")

categorized_text_file = ReadTextFile(crs)


categorized_text_file.print_events_list()
categorized_text_file.print_event("st002")
categorized_text_file.print_text()