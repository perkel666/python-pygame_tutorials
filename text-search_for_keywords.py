__author__ = 'Perkel'

import re


class TextHandling():

    @ staticmethod
    def get_text(filepath):
        opened_file = open(filepath, "r")
        text = opened_file.read().split('\n')
        return text

    @ staticmethod
    def parse_text(text):

        """ Removes empty lines and removes empty space from left side
        """

        text_copy = text
        new_text = []
        for line in text_copy:
            if line != '':
                parsed_line = line.lstrip()
                new_text.append(parsed_line)

        return new_text

    @ staticmethod
    def find_text_between_brackets(text_with_brackets):
        result = re.search(r'\[(.*)\]', text_with_brackets).group(1)
        return result


class GameTextEvents():
    def __init__(self, text):
        """
        :param text: accepts list with strings of text
        """
        self.unparsed_text = text
        self.parsed_whole_event_text_file = TextHandling.parse_text(text)
        self.event_list = self.get_events_list()

    def print_text(self):
        print ""
        print "====WHOLE FILE=========="
        for line in self.unparsed_text:
            print line
        print "====WHOLE FILE END======"
        print ""

    def get_events_list(self, print_list=False):
        """
        :param print_list: prints all events in text file
        :return: tuple of event and line number
        """
        event_list = []

        line_number = 0
        for line in self.parsed_whole_event_text_file:
            line_number += 1
            if "EVENT" in line:
                event = TextHandling.find_text_between_brackets(line)
                event_list.append((event, line_number))

        if print_list is True:
            print "===EVENTS LIST========="
            for event in event_list:
                print event[0]
            print "===EVENTS LIST END====="

        return event_list

    def find_text_between_brackets(self, line):
        """
        :param line: accepts string line
        :return: text inside of brackets
        """
        result = re.search(r'\[(.*)\]', line).group(1)
        return result

    def event_content(self, event_name):
        """
        :param event_name: name of event (eg. st001)
        :return: list with lines from specified event
        """
        events = self.event_list

        print_start = None
        print_end = None
        next_event = None
        event_content = []

        count = -1  # -1 because i need to get over list starting with 0 twice so -1 and not 0
        for event in events:
            count += 1
            if event_name in event[0]:
                print_start = event[1]+1
                next_event = count + 1

        print_end = events[next_event]
        print_end = print_end[1]-1

        count = 0
        for line in self.parsed_whole_event_text_file:
            count += 1
            if print_start <= count <= print_end:
                event_content.append(line)

        return event_content


text01 = TextHandling.get_text("data/text/key_word_test.txt")
events_file = GameTextEvents(text01)


#for event in events_file.event_list:
#    print event[0]

#for line in  events_file.event_content("st001"):
#    print line

#events_file.print_text()