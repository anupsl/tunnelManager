import logging


class Constants():
    jumpBox = {
        'nightly' : 'jumpbox1.nightly.capillary.in',
        'staging' : 'jumpbox1.staging.capillary.in',
        'eu' :  'jumpbox1.prod.capillary.sg',
        'more' : 'jumpbox1.prod.capillary.sg',
        'india' : 'jumpbox1.prod.capillary.in',
        'china' : 'jumper.capillarytech.cn.com',
        #'terra' : 'jumper-tf.kubernetestest.capillary.co.in'
    }     
        
    userName = 'anup.langoti'
    passWord = 'n67unz0Vncm3Q'
    config = {}	
    configuredPort = {
        'nightly' : [],
        'staging' : [],
        'eu' : [],
        'more' : [],
        'india' : [],
        'china' : [],
        #'terra' : []                        
    }

def Logger():
    logger = logging.getLogger("tunnelmanager")
    logger.setLevel(logging.DEBUG)
    filePath = '/var/log/capillary/tunnelManager/tunnelmanager.log'
    formatter = logging.Formatter("%(asctime)s - %(threadName)-10.12s - %(message).2000s", "%Y-%m-%d %H:%M:%S")     # Format for our loglines
    fh = logging.FileHandler(filePath)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)  
    
def log(*message):
    logger = logging.getLogger('tunnelmanager')
    logger.debug(''.join(map(str, list(message))))
        

    

