#!/usr/bin/python3
from fileinput import filename
import os,sys
import zipfile

from sf_virtual_data.api.vt_pb2 import  TABLES
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import pandas as pd
from sys import argv
from sf_virtual_data import utils
from sf_virtual_data.virtual_tags_runner import VirtualTagsRunner
from user_calculation import calculate as user_calc
from user_calculation import debug as user_debug

def main(cmd_line_args=argv[1:]) -> pd.DataFrame:
    base_cmd_line_args  = utils.parse_input(cmd_line_args)
    print(base_cmd_line_args)
    print(base_cmd_line_args.site)
    vt = VirtualTagsRunner(base_cmd_line_args.metadata_file)
    res = vt.execute(base_cmd_line_args, user_calc)
    tagTimeSeriesData = utils.convert_to_dto(res)
    if not base_cmd_line_args.debug:
        filename = base_cmd_line_args.output_filename
        if vt.metadata.category == TABLES :
            with zipfile.ZipFile(filename, 'w') as myzip:
                print("writing zip file of tables csv's")
                for (columnName, columnData) in res.iteritems():
                    csv_name = columnName + ".csv"
                    columnData.iloc[0].to_csv(csv_name)
                    myzip.write(csv_name)
        else:
            with open(filename, 'wb') as bin_file:
                bin_text = tagTimeSeriesData.SerializeToString()
                bin_file.write(bin_text)
    else:
        user_debug(res)

    return res


if __name__ == "__main__":
    """
    Example of script run:  python virtual_trend_entry_point.py --start-utc "2020-10-07 02:00:00" --end-utc "2020-10-07 16:00:00" --debug --api-access-key "<your_api_access_key>"
    or run with IDE run-time args  ["--start-utc","2020-10-07 02:00:00", "--end-utc", "2020-10-07 16:00:00", "--debug", "--api-access-key", "<your_api_access_key>"]
    """
    main()
