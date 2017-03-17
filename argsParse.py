import argparse

def system_startup():
    #LOGGER = log.getLogger(__name__)

    
   # LOGGER.info("\n****\nHCOE system startup process starts")
        
   # Get the parameters for running system startup
   #LOGGER.info("Prepare the list of parameters based on arguments passed")
   args = get_args()
   vcenter_host = args.vcenterHost
   vcenter_port = args.vcenterPort
   vcenter_user = args.vcenterUser
   vcenter_password = args.vcenterPassword
   datacenter_name = args.datacenterName
   hcoe_host = args.hcoeHost
   hcoe_user = args.hcoeUser
   hcoe_password = args.hcoePassword
   print vcenter_host, vcenter_port, vcenter_user, vcenter_password, datacenter_name, hcoe_host, hcoe_user, hcoe_password
def get_args():
    """
    Get CLI arguments.
    """
   # LOGGER = log.getLogger(__name__)

    # Prepare the parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-vh', '--vcenterHost',
                        required=True,
                        action='store',
                        help='VCenter host name or IP address')
    parser.add_argument('-vo', '--vcenterPort',
                        type=int,
                        default=443,
                        action='store',
                        help='VCenter port number')
    parser.add_argument('-vu', '--vcenterUser',
                        required=True,
                        action='store',
                        help='VCenter user name')
    parser.add_argument('-vp', '--vcenterPassword',
                        required=True,
                        action='store',
                        help='VCenter password')
    parser.add_argument('-dn', '--datacenterName',
                        required=True,
                        action='store',
                        default=None,
                        help='Datacenter path used for HCOE')
    parser.add_argument('-hh', '--hcoeHost',
                        required=True,
                        action='store',
                        help='HCOE system host name or IP address')
    parser.add_argument('-hu', '--hcoeUser',
                        required=True,
                        action='store',
                        help='HCOE user name')
    parser.add_argument('-hp', '--hcoePassword',
                        required=True,
                        action='store',
                        help='HCOE password')

    # Initialize logging
#    log.add_logging_arguments(parser)

    # Parse the request parameters
    args = parser.parse_args()
 #   log.setup_from_cmdline(args)
    
  #  LOGGER.info("Arguments passed are! %s", args)
    return args


if __name__ == "__main__":
    system_startup()
