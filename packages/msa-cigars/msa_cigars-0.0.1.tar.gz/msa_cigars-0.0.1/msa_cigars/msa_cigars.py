#!/usr/bin/env python3
import sys
# import os
import argparse
import re
import collections
from Bio import AlignIO



def get_parameter():
    description = '''
To get the CIGARs of a multiple sequence alignment. 
ONE alignment in the input file is assumed!

CIGARs are in respect of the reference sequence. 

'O' normal bases, e.g. A, T, G, C
'-' deletion
'N' unknown base

    seq - - - N N N O O O
 refseq - N O N - O O N -
  cigar P n D B u U M N I

By Guanliang MENG, 
see https://github.com/linzhi2013/msa_cigars.'''

    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        '-i', 
        dest='msafile', 
        metavar='<FILE>', 
        required=True,
        help='input msa file'
        )

    parser.add_argument(
        '-refseq_id',
        metavar='<STR>',
        required=True,
        help='''MsaCigars class uses regular expression to find out the 
sequence id of refseq. Thus, make sure the value of 'refseq_id' option is 
unique among the input msa file.'''
        )

    parser.add_argument(
        '-n',
        metavar='<STR>',
        dest='unknown_base',
        default='N',
        help = 'character of unknown base [%(default)s]'

    )

    parser.add_argument(
        '-g',
        dest='gap_base',
        metavar='<STR>',
        default='-',
        help='character of gap base [%(default)s]'


    )

    parser.add_argument(
        '-f', 
        dest='msaformat', 
        metavar='<FORMAT>', 
        default='fasta', 
        help='the msa format [%(default)s]'
        )

    parser.add_argument(
        '-o', 
        dest='fh_out', 
        metavar='<FILE>', 
        type=argparse.FileType('w', encoding='UTF-8'),
        default=sys.stdout, 
        help='outfile name [stdout]'
        )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args()

    if len(args.unknown_base) != 1:
        sys.exit(''''-n' option should be one charater in length!''')

    if len(args.gap_base) != 1:
        sys.exit(''''-g' option should be one charater in length!''')

    return args


class UnEqualLenth(Exception):
    def __init__(self, m):
        super(UnEqualLenth, self).__init__()
        self.message = m

    def __str__(self):
        return self.message


class PairSeqCigar(object):
    """see https://davetang.org/wiki/tiki-index.php?page=SAM and 
    https://samtools.github.io/hts-specs/SAMv1.pdf

    #    seq - - - N N N O O O
    # refseq - N O N - O O N -
    #  cigar P n D B u U M N I

    """

    match = 'M'
    insertion = 'I'
    deletion = 'D'
    padding = 'P'

    unknown_base_on_seq_and_refseq_normal = 'U'
    unknown_base_on_seq_and_refseq_is_gap = 'u'

    unknown_base_on_refseq_and_seq_normal = 'N'
    unknown_base_on_refseq_and_seq_is_gap = 'n'

    unknown_base_on_seq_and_refseq = 'B'


    def __init__(self, seq=None, refseq=None, unknown_base=None, gap_base=None):
        super(PairSeqCigar, self).__init__()
        self.refseq = re.sub(r'\s+', '', refseq).upper()
        self.seq = re.sub(r'\s+', '', seq).upper()
        self.unknown_base = unknown_base.upper()

        self.cigar = self.__examine_pair(
            seq=self.seq, 
            refseq=self.refseq, 
            unknown_base=self.unknown_base
        )


    def __examine_pair(self, seq=None, refseq=None, unknown_base=None):
        con = []
        if len(seq) != len(refseq):
            raise UnEqualLenth(
                'UnEqualLenth of seq({0}) and refseq({1})!'
                .format(len(seq), len(refseq))
            )

        for i in range(0, len(seq)):
            b1 = seq[i]
            b2 = refseq[i]

            '''
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
            '''

            # seq: -
            if b1 == b2 == '-':
                con.append(self.padding)

            elif (b1 == '-') and (b2 == unknown_base):
                con.append(self.unknown_base_on_refseq_and_seq_is_gap)

            elif (b1 == '-') and (b2 not in (unknown_base, '-')) :
                con.append(self.deletion)
                
            # seq: N
            elif b1 == b2 == unknown_base:
                con.append(self.unknown_base_on_seq_and_refseq)

            elif (b1 == unknown_base) and (b2 == '-'):
                con.append(self.unknown_base_on_seq_and_refseq_is_gap)

            elif (b1 == unknown_base) and (b2 not in (unknown_base, '-')):
                con.append(self.unknown_base_on_seq_and_refseq_normal)

            #    seq - - - N N N O O O
            # refseq - N O N - O O N -
            #  cigar P n D B u U M N I

            # seq: O
            elif (b1 not in (unknown_base, '-')) and (b2 not in (unknown_base, '-')):
                con.append(self.match)

            elif (b1 not in (unknown_base, '-')) and (b2 == unknown_base):
                con.append(self.unknown_base_on_refseq_and_seq_normal)

            elif (b1 not in (unknown_base, '-')) and (b2 == '-'):
                con.append(self.insertion)

        cigar = []
        pre_type = con[0]
        count = 1
        for cur_type in con[1:]:
            if cur_type == pre_type:
                count += 1
            else:
                cigar.append((str(count)+pre_type))
                count = 1
                pre_type = cur_type
        # the last ele
        cigar.append((str(count)+pre_type))

        if len(cigar) > 0:
            return ''.join(cigar)
        else:
            return None


    def __str__(self):
        return self.cigar

    def __repr__(self):
        return self.cigar


class MsaCigars(object):
    """
    MsaCigars class uses regular expression to find out the sequence id of 
    refseq. Thus, make sure the value of 'refseq_id' option is unique among the
    input msa file.
    """
    def __init__(self, msafile=None, msaformat=None, refseq_id=None, unknown_base='N', gap_base='-'):
        self.msafile = msafile
        self.msaformat = msaformat
        self.refseq_id = refseq_id
        self.unknown_base = unknown_base
        self.gap_base = gap_base

        self.msa, self.is_refseq, self.refseq_rec = self._read_msa()

        self.cigars = self._get_all_cigars_of_pairseqs()


    def __combine_cigars(self):
        cigars_str = []
        for refseq_id in self.cigars:
            for seqid in self.cigars[refseq_id]:
                i = (refseq_id, seqid, str(self.cigars[refseq_id][seqid]))
                cigars_str.append('\t'.join(i))
        return '\n'.join(cigars_str)

    def __str__(self):
        return self.__combine_cigars()


    def __repr__(self):
        return self.__combine_cigars()


    def _read_msa(self):
        msa = AlignIO.read(self.msafile, self.msaformat)
        is_refseq = {}
        refseq_rec = None
        for i, rec in enumerate(msa):
            msa[i].seq = rec.seq.upper()
            if re.search(self.refseq_id, str(rec.id)):
            #if str(rec.id).startswith('NC_'):
                is_refseq[str(rec.id)] = True
                refseq_rec = rec
            else:
                is_refseq[str(rec.id)] = False

        return msa, is_refseq, refseq_rec


    def _get_pairseq_cigar(self, seq, refseq, unknown_base, gap_base):
        return PairSeqCigar(
            seq = seq, 
            refseq = refseq, 
            unknown_base = unknown_base, 
            gap_base = gap_base
            )


    def _get_all_cigars_of_pairseqs(self):
        cigars = collections.defaultdict(dict)
        for rec in self.msa:
            if self.is_refseq[str(rec.id)]:
                continue

            cigar = self._get_pairseq_cigar(
                        seq = str(rec.seq), 
                        refseq = str(self.refseq_rec.seq),
                        unknown_base = self.unknown_base,
                        gap_base = self.gap_base
                    )
            cigars[str(self.refseq_rec.id)][str(rec.id)] = cigar

        return cigars


def main():
    args = get_parameter()
    msa_cigars = MsaCigars(
        msafile=args.msafile, 
        msaformat=args.msaformat, 
        refseq_id=args.refseq_id,
        unknown_base=args.unknown_base,
        gap_base=args.gap_base
    )

    for refseq_id in msa_cigars.cigars:
        for seqid in msa_cigars.cigars[refseq_id]:
            print(refseq_id, seqid, msa_cigars.cigars[refseq_id][seqid], 
                sep='\t', file=args.fh_out)


if __name__ == '__main__':
    main()





















