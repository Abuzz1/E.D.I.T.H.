class Config():
    """ Configuration file for edith usage """
    def get():
        config = {
            "edith": {           # don't change
                "version": 1.0   # don't change
            }, 

            "config": { # change this
                "host": "Raspberry Pi Zero WH", # change host to machine running program
                "online server": {  # online server configuration
                    "host": "false", # change to true or false according to needs
                    "port": 8080  # change port
                },
                "go commands": "true" # change (true or false) according to needs. 
                
            }

        }
        return config