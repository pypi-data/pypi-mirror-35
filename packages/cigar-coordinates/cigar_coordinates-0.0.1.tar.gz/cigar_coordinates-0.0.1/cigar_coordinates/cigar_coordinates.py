#!/usr/bin/env python3
import sys
import argparse
import re

def get_parameter():
    description = '''To get the coordinates of a given CIGAR string. 
By Guanliang MENG, see https://github.com/linzhi2013/cigar_coordinates.

I understand the following CIGAR types:

     seq - - - N N N O O O
  refseq - N O N - O O N -
   cigar P n D B u U M N I

The output coordinates are closed intervals.'''
   
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        '-c', 
        dest='cigar', 
        metavar='<STR>', 
        required=True,
        help='input CIGAR string'
    )

    parser.add_argument(
        '-s',
        dest='start',
        metavar='<INT>',
        type=int,
        default=1,
        help='the start coordinate on the sequence, whatever the gene direction is, this option is always the smaller one. [%(default)s]'
    )

    parser.add_argument(
        '-q',
        dest='is_query',
        action='store_false',
        default=True,
        help="the '-s' option is about query sequence, not refseq [%(default)s]"
    )

    parser.add_argument(
        '-d',
        dest='direction',
        default='+',
        choices=['+', '-'],
        help='the gene direction [%(default)s]'
    )


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


class CigarCoordinates(object):
    """
    Return the coordinates of given cigar.
    
    # 'O' normal bases, e.g. A, T, G, C
    # '-' deletion
    # 'N' unknown base
    #    seq - - - N N N O O O
    # refseq - N O N - O O N -
    #  cigar P n D B u U M N I
    
    match = 'M'
    insertion = 'I'
    deletion = 'D'
    padding = 'P'

    unknown_base_on_seq_and_refseq_normal = 'U'
    unknown_base_on_seq_and_refseq_is_gap = 'u'

    unknown_base_on_refseq_and_seq_normal = 'N'
    unknown_base_on_refseq_and_seq_is_gap = 'n'

    unknown_base_on_seq_and_refseq = 'B'

    Parameters:
    cigar - string
    start - int
    end - int
    is_query - asking for coordinates of query, and the start and end are on query sequence. if False, asking for refseq is assumed.
    direction - '+' or '-'

    Return:
    a list of three tuples: (cigar, start, end), in which start and end are  closed interval.

    #    seq - - - N N N O O O
    # refseq - N O N - O O N -
    #  cigar P n D B u U M N I
    
    Also see:
        package 'msa_cigars'

    """

    all_cigar_chars = 'PnDBuUMNI'
    consume_seq_cigar_chars = 'BuUMNI'
    consume_refseq_cigar_chars = 'nDBUMN'

    def __init__(self, cigar=None, start=1, is_query=True, direction='+'):
        super(CigarCoordinates, self).__init__()
        self.cigar = self.__check_cigar(cigar)
        self.start = self.__check_coordinate(start)
        self.is_query = is_query

        self.direction = self.__check_direction(direction)

        self.coordinates = self.__get_coordinates()


    def __check_cigar(self, cigar=None):
        if not isinstance(cigar, str):
            raise TypeError(
                "CIGAR must be string, not {0}".format(type(cigar))
            )

        cigar_chars = re.split(r'\d+', cigar)
        cigar_set = set(cigar_chars)
        unknown_chars = set()
        for char in cigar_set:
            if not char:
                continue
            if char not in self.all_cigar_chars:
                unknown_chars.add(char)

        if len(unknown_chars) > 0:
            raise TypeError(
            'unknown_chars in CIGAR found: {0}'
            .format(' '.join(unknown_chars))
            )
            return None

        return cigar


    def __check_coordinate(self, number=None):
        if not isinstance(number, int):
            raise TypeError(
                "coordinate must be int, not {0}".format(type(number))
            )
        return number


    def __check_direction(self, direction=None):
        if not isinstance(direction, str):
            raise TypeError(
                "direction must be string, not {0}".format(type(cigar))
            )

        if direction not in ('+', '-'):
            raise TypeError(
                "direction must be either '+' or '-', not {0}"
                .format(direction)
            )
        return direction


    def __query_add_cigar(self, start=None, cigar=None):
        number = int(cigar[:-1])
        cigar_type = cigar[-1]

        consumed = cigar_type in self.consume_seq_cigar_chars

        if consumed:
            return cigar, start, start+number-1, consumed

        else:
            return cigar, start, start, consumed

      
    def __refseq_add_cigar(self, start=None, cigar=None):
        number = int(cigar[:-1])
        cigar_type = cigar[-1]

        consumed = cigar_type in self.consume_refseq_cigar_chars
        if consumed:
            return cigar, start, start+number-1, consumed

        else:
            return cigar, start, start, consumed


    def __coordinates(self, start=None, cigar_lst=None, is_query=None):
        coordinates = []
        if is_query:
            for i in cigar_lst:
                cigar, begin, stop, consumed = self.__query_add_cigar(
                    start=start, 
                    cigar=i
                )
                coordinates.append((cigar, begin, stop))
                if consumed:
                    start = stop + 1

        else:
            for i in cigar_lst:
                cigar, begin, stop, consumed = self.__refseq_add_cigar(
                    start=start,
                    cigar=i
                )
                coordinates.append((cigar, begin, stop))
                if consumed:
                    start = stop + 1
        return coordinates


    def __get_coordinates(self):
        cigar_lst = re.findall(
            r'(\d+[{0}])'.format(self.all_cigar_chars), 
            self.cigar
        )

        if isinstance(cigar_lst, type(None)):
            raise TypeError(
                "cannot split \'{0}\' into individual cigar".format(self.cigar)
            )

        if self.direction == '-':
            cigar_lst = cigar_lst[::-1]
            
        return self.__coordinates(
            start=self.start,
            cigar_lst=cigar_lst,
            is_query=self.is_query
        )


    def __combine_coor(self):
        combine_coor = []
        for i in self.coordinates:
            k = [str(j) for j in i]
            combine_coor.append('\t'.join(k))

        return "\n".join(combine_coor)


    def __str__(self):
        return self.__combine_coor()


    def __repr__(self):
        return self.__combine_coor()
        

def main():
    args = get_parameter()

    cigar_coor = CigarCoordinates(
        cigar=args.cigar, 
        start=args.start, 
        is_query=args.is_query, 
        direction=args.direction
    )

    print(cigar_coor)


if __name__ == '__main__':
    main()