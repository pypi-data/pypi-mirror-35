import os
import re

import pandas as pd
from cement.core.controller import CementBaseController, expose
from cement.core.foundation import CementApp


def _list_dir(directory, glob=None):
    glob_matcher = None
    if glob:
        glob_matcher = re.compile(glob)
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if glob_matcher and not glob_matcher.match(f):
                continue
            yield os.path.abspath(os.path.join(dirpath, f))


def _csv_to_par(filepath, output_filepath=None, output_filedir=None,
                logger=None):
    logger.debug("Converting {}".format(filepath))
    csv = pd.read_csv(filepath, memory_map=True, na_values=r'\N')
    parquet_filepath = ''
    if output_filepath:
        csv.to_parquet(output_filepath)
        return output_filepath
    elif output_filedir:
        parquet_filepath += output_filepath
    else:
        name_wo_extension = os.path.splitext(filepath)[0]
        parquet_filepath = os.path.join(parquet_filepath,
                                        name_wo_extension) + '.parquet'
    csv.to_parquet(parquet_filepath, compression='gzip')
    if logger:
        logger.info("Successfully converted {} to {}".format(filepath,
                                                             parquet_filepath))
    return parquet_filepath


def csv_to_par(path, output_path=None, logger=None):
    if os.path.isdir(path):
        if logger:
            logger.info("{} is a directory, traversing".format(path))
        for file in _list_dir(path, ".*\.csv"):
            _csv_to_par(file, output_filedir=output_path, logger=logger)
    else:
        _csv_to_par(path, output_filepath=output_path, logger=logger)


class Converter(CementBaseController):
    class Meta:
        label = 'base'
        description = "Util tool for parquet"
        arguments = [
            (['-i', '--input-file'],
             dict(action='store', help='input file path', dest='input_file')),
            (['-o', '--output-file'],
             dict(action='store', help='output file path',
                  dest='output_file')),
            (['-d', '--input-dir'],
             dict(action='store', help='input dir path', dest='input_dir')),
        ]

    @expose(hide=True)
    def default(self):
        self.app.log.info('Inside MyBaseController.default()')
        if self.app.pargs.debug:
            print("Recieved option: foo => %s" % self.app.pargs.debug)

    @expose(help="Convert csv file to parquet file")
    def csv_to_parquet(self):
        filepath = self.app.pargs.input_file
        outfilepath = self.app.pargs.output_file
        try:
            csv_to_par(filepath, outfilepath,
                       logger=self.app.log)
        except Exception as e:
            self.app.log.error(
                "Cannot convert {} because of {}".format(filepath, e))
            raise e


class ParquetUtils(CementApp):
    class Meta:
        label = 'parquet-utils'
        base_controller = 'base'
        handlers = [Converter]


with ParquetUtils() as app:
    app.run()
