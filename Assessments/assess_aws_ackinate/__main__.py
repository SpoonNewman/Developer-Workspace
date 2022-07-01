from run_validation import pass_iam_policies_to_pariah_microservice
from aegis_helper_functions import get_iam_policies
# DO NOT REMOVE THE ABOVE

# Premise:
# A coworker, named Benjamin, on the Tools team has built a microservice that 
# is able to simplify and consolidate the management of IAM policies that your 
# company uses to control permissions in its AWS environment. As such you've 
# been told that this service works flawlessly.

# Your task is to pull down these IAM policies and pass them on to our own 
# microservice that will build AWS resources. Ensure that the policies pass 
# our strict validation.

# Bad data values that is displayed in the fields must be changed to the string 
# "BAD_DATA" to be reviewed by our SecOps team.

# Bad data will have format of "<event name>-00000"


def get_aegis_iam_policies() -> list[dict]:
    # DO NOT CHANGE
    return get_iam_policies()

def main():
    # Add code here
    pass_iam_policies_to_pariah_microservice()

if __name__ == "__main__":
    main()