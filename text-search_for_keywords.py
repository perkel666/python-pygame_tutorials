__author__ = 'Perkel'

import re


class TextHandling():

    """
    General class to handle text
    """

    @ staticmethod
    def get_text_from_file(filepath):
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
        This class operates on text variable, it provides support to create list of event objects that
        later can be used to make game events with text.
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

    def get_events_list(self):
        """
        :return: tuple of event and line number
        """

        event_list = []
        line_number = 0
        for line in self.parsed_whole_event_text_file:
            line_number += 1
            if "EVENT" in line:
                event = TextHandling.find_text_between_brackets(line)
                event_list.append((event, line_number))

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

        # get where event starts and ends
        count = -1
        for event in events:
            count += 1
            if event_name in event[0]:
                print_start = event[1]+1
                next_event = count + 1

        print_end = events[next_event]
        print_end = print_end[1]-1

        # put lines from event into list
        count = 0
        for line in self.parsed_whole_event_text_file:
            count += 1
            if print_start <= count <= print_end:
                event_content.append(line)

        # figure out who is participating in event
        speaker_list = []
        for text_line in event_content:
            if "SPEAKER" in text_line:
                speaker_list.append(text_line)

        # removing duplikates from speaker list
        speaker_list = list(set(speaker_list))

        event_content = (speaker_list, event_content)
        return event_content

    def create_event_objects_list(self):

        event_objects_list = []
        for event in self.event_list:
            if "EVENT:END" not in event[0]:
                scratch_event = self.event_content(event[0])
                event_object = Event(event, scratch_event[0], scratch_event[1])
                event_objects_list.append(event_object)
                print event_object
            else:
                pass
        print event_objects_list
        return event_objects_list


class Event():
    """
    This class creates event object with data that can be later on extracted for use in game events.
    """
    def __init__(self, name, participants, event_text):
        self.name = name[0]
        self.starts_at_line = name[1]
        self.participants = participants
        self.event_text = event_text

    def print_event_to_console(self):
        print ""
        print "=================="
        print "EVENT NAME : "+self.name
        print "EVENT PARTICIPANTS : "
        print "------------------"
        for participant in self.participants:
            print participant
        print "------------------"
        print "EVENT TEXT :"
        print "------------------"
        for line in self.event_text:
            print line
        print "------------------"
        print "=================="


text01 = TextHandling.get_text_from_file("data/text/key_word_test.txt")
events_file = GameTextEvents(text01)

events_object_list = events_file.create_event_objects_list()

#for event in events_file.event_list:
#    print event[0]

#for linex in events_file.event_content("st001"):
#    print linex

#events_file.print_text()

for event in events_object_list:
    event.print_event_to_console()