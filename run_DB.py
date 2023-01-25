from dbbatch.run_batch import run_batch

def run_db() -> None:
    input_dir = r"D:\cly\Documents\DesignBuilder Data\BatchInput"
    output_dir =  r"D:\cly\Documents\DesignBuilder Data\BatchOutput"
    kwargs = {
        "db_pth": r"D:\Program Files (x86)\DesignBuilder\DesignBuilder.exe",
        "job_server_dir": r"D:\ProgramData\DesignBuilder\JobServer\Users\User",
        "make_output_subdirs": True,
        "include_model_name": False,
        "include_orig_name": True,
        # "use_sim_manager": True,
        "analysis_type": "eplus",
        "write_report": False,
    }
    # str_args = f"\tmodels dir : {input_dir}\n\toutputs dir : {output_dir}\n"
    # for k, v in kwargs.items():
    #     str_args += f"\t{k} : {v}\n"
    # print(f"Running batch with following arguments:\n{str_args}")
    run_batch(input_dir, output_dir, **kwargs)

if __name__ == '__main__':
    run_db()