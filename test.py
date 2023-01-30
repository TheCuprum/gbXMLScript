import math
import os
import shutil

from calculator.segment3_calculator_builder import Segment3CalculatorBuilder
from edit_seg3 import edit_xml
from run_DB import run_db


def copy_result_folder(source_dir: str, target_dir: str):
    destination_list = []
    source_sub_dir_list = os.listdir(source_dir)
    target_sub_dir_list = os.listdir(target_dir)
    for source_sub_dir in source_sub_dir_list:
        source_sub_dir_full = os.path.join(source_dir, source_sub_dir)
        if os.path.isdir(source_sub_dir_full):
            postfix = 1
            renamed_dir = source_sub_dir
            while(renamed_dir in target_sub_dir_list):
                postfix += 1 
                renamed_dir = source_sub_dir + f'_{postfix}'
            target_sub_dir_full = os.path.join(target_dir, renamed_dir)
            shutil.copytree(source_sub_dir_full, target_sub_dir_full)
            destination_list.append(target_sub_dir_full)

    return destination_list

def run_test():
    input_dir = ''
    input_backup_dir = ''
    output_dir = ''
    copy_dir = ''
    db_path = ''
    job_server_dir = ''

    builder = Segment3CalculatorBuilder()

    for i in range(0): # need loop condition
        # builder.left_length
        # builder.left_width
        # builder.middle_length
        # builder.middle_width
        # builder.right_length
        # builder.right_width
        # builder.height
        # builder.left_angle
        # builder.right_angle

        shutil.copytree(input_dir, input_backup_dir, dirs_exist_ok=True) # backup models

        edit_xml(builder)
        run_db(input_dir, output_dir, db_path, job_server_dir)
        copy_result_folder(output_dir, copy_dir)

        shutil.copytree(input_backup_dir, input_dir, dirs_exist_ok=True) # restore models

if __name__ == '__main__':
    run_test()