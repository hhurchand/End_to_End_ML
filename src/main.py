import argparse
import pandas as pd
import yaml

def read_params(config_path: str)-> yaml:
    """Read parameters for project configuration

    Args:
        config_path (str): path of parameter file

    Returns:
        yaml : yaml file with project configuration data
    """
    with open(config_path, encoding="UTF-8") as f:
        return yaml.safe_load(f)

def read_data(path:str) -> pd.DataFrame:
    """Read training data

    Args:
        path (str): path to training data

    Returns:
        pd.DataFrame: Dataframe for training dataset
    """
    with open(path,encoding = "UTF-8") as f:
        return pd.read_csv(f)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    config_dict = read_params(config_path=parsed_args.config)
    df = read_data(config_dict['data_config']['train_data'])
