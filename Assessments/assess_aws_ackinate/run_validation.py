
def run_tests(iam_policies: list[dict]):
    # grab the list of SIDs from mockapi
    # grab the corresponding schemas from mockapi
    # validate the SIDs
    if iam_policies is None:
        raise ValueError("No IAM policies were received")
    for x in iam_policies:
        for key in x.keys():
            if key not in ["Sid", "Action", "Resource", "Principal"]:
                raise ValueError("It appears that the keys of the IAM Policy dictionary are invalid. Check your data")
        for z in x.values():
            if "-" in z:
                raise ValueError("It appears that there is still bad data in the dictionary. Check your data.")

def pass_iam_policies_to_pariah_microservice(iam_policies: list[dict]) -> bool:
    run_tests(iam_policies=iam_policies)

if __name__ == 'run_tests':
    run_tests()