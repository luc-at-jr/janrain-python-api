""" Utilities for working with the Janrain API configuration file. """
import yaml
import os

def read_config_file():
    """
    Read the YAML configuration file named ``.apidrc`` and located in the
    user's home directory.
    
    Return:
        A Python structure representing the YAML.
    """
    yaml_file = os.path.join(os.path.expanduser("~"), ".apidrc")
    
    with open(yaml_file) as stream:
        config = yaml.load(stream.read())
    
    return config
        
def default_client():
    """
    Get the settings for the default client defined in the .apidrc file.
    
    Returns:
        A dictionary containing the default client settings.
    """
    config = read_config_file()
    return config['clients'][config['defaults']['default_client']]

def cluster(cluster_name):
    """
    Get the client_id and client_secret defined for the specified cluster.
    
    Args:
        The name of the cluster defined in the .apidrc file. Eg. "prod".
    
    Returns:
        A dictionary containing the cluster settings.
    """
    config = read_config_file()
    try:
        return config['clusters'][cluster_name]
    except KeyError as error:
        raise KeyError("A cluster named '{}' was not found in the config file" \
                       .format(cluster_name))
    
