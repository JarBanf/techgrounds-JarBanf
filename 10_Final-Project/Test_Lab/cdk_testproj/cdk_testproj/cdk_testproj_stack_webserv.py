from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
import cdk_testproj_stack_network as network


# Configuratio parameters


class CdkTestprojStackWebserv(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # STANDARD CODES
        


        ################################################################################################


        # INITIATE STANDARD CODES



        # PER RESOURCE CODE

        # instance_1 = ec2.Instance(self, "Instance-1",
        #     vpc=
        #     )

