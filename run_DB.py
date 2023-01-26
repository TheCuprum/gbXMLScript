from dbbatch.run_batch import run_batch

def run_db(input_dir: str, output_dir: str, db_path: str, job_server_dir: str) -> None:
    input_dir = r"D:\cly\Documents\DesignBuilder Data\BatchInput"
    output_dir =  r"D:\cly\Documents\DesignBuilder Data\BatchOutput"
    kwargs = {
        "db_pth": db_path,
        "job_server_dir": job_server_dir,
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
