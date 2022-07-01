from run_validation import pass_iam_policies_to_pariah_microservice
from aegis_helper_functions import get_iam_policies
import requests
# DO NOT REMOVE THE ABOVE


def get_aegis_iam_policies() -> list[dict]:
    # DO NOT CHANGE
    return get_iam_policies()

def main():
    # Add code here
    pass_iam_policies_to_pariah_microservice()