"""Command line conversion tools `nbrmd` and `nbsrc`
"""

import os
import argparse
from nbformat import writes as ipynb_writes
from nbformat.reader import NotJSONError
from nbrmd import readf, writef
from nbrmd import writes
from .languages import get_default_language
from .combine import combine_inputs_with_outputs
from .file_format_version import check_file_version


def cli_nbrmd(args=None):
    """
    Command line parser
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser(description='Jupyter notebook '
                                                 'from/to R Markdown')
    parser.add_argument('notebooks',
                        help='One or more .ipynb or .Rmd notebook(s) '
                             'to be converted to the alternate form',
                        nargs='+')
    parser.add_argument('-i', '--in-place', action='store_true',
                        help='Store the result of conversion '
                             'to file with opposite extension')
    parser.add_argument('-p', '--preserve_outputs', action='store_true',
                        help='Preserve outputs of .ipynb '
                             'notebook when file exists and inputs match')
    return parser.parse_args(args)


def nbrmd():
    """
    Entry point for the nbrmd script
    :return:
    """
    args = cli_nbrmd()
    convert(args.notebooks, args.in_place, args.preserve_outputs, True)


def convert(nb_files, in_place=True, combine=True, markdown=False):
    """
    Export R markdown notebooks, python or R scripts, or Jupyter notebooks,
    to the opposite format
    :param nb_files: one or more notebooks
    :param markdown: R markdown to Jupyter, or scripts to Jupyter?
    :param in_place: should result of conversion be stored in file
    with opposite extension?
    :param combine: should the current outputs of .ipynb file be preserved,
    when a cell with corresponding input is found in .Rmd/.py or .R file?
    :return:
    """
    for nb_file in nb_files:
        file, ext = os.path.splitext(nb_file)
        if markdown:
            format = 'R Markdown'
            if ext not in ['.ipynb', '.Rmd']:
                raise TypeError(
                    'File {} is neither a Jupyter (.ipynb) nor a '
                    'R Markdown (.Rmd) notebook'.format(nb_file))
        else:
            format = 'source'
            if ext not in ['.ipynb', '.py', '.R']:
                raise TypeError(
                    'File {} is neither a Jupyter (.ipynb) nor a '
                    'python script (.py), nor a R script (.R)'.format(nb_file))

        nb = readf(nb_file)
        main_language = get_default_language(nb)
        ext_dest = '.Rmd' if markdown else '.R' \
            if main_language == 'R' else '.py'

        if in_place:
            if ext == '.ipynb':
                nb_dest = file + ext_dest
                print('Jupyter notebook {} being converted to '
                      '{} {}'.format(nb_file, format, nb_dest))
            else:
                msg = ''
                nb_dest = file + '.ipynb'
                if combine and os.path.isfile(nb_dest):
                    check_file_version(nb, nb_file, nb_dest)
                    try:
                        nb_outputs = readf(nb_dest)
                        combine_inputs_with_outputs(nb, nb_outputs)
                        msg = '(outputs were preserved)'
                    except (IOError, NotJSONError) as error:
                        msg = '(outputs were not preserved: {})'.format(error)
                print('{} {} being converted to '
                      'Jupyter notebook {} {}'
                      .format(format, nb_file, nb_dest, msg))
            writef(nb, nb_dest)
        else:
            if ext == '.ipynb':
                print(writes(nb, ext_dest))
            else:
                print(ipynb_writes(nb))


def cli_nbsrc(args=None):
    """
    Command line parser
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser(description='Jupyter notebook '
                                                 'from/to R or Python script')
    parser.add_argument('notebooks',
                        help='One or more .ipynb or .R or .py script(s) '
                             'to be converted to the alternate form',
                        nargs='+')
    parser.add_argument('-i', '--in-place', action='store_true',
                        help='Store the result of conversion '
                             'to file with opposite extension')
    parser.add_argument('-p', '--preserve_outputs', action='store_true',
                        help='Preserve outputs of .ipynb '
                             'notebook when file exists and inputs match')
    return parser.parse_args(args)


def nbsrc():
    """
    Entry point for the nbsrc script
    :return:
    """
    args = cli_nbsrc()
    convert(args.notebooks, args.in_place, args.preserve_outputs, False)
