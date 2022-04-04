# from go.bj_strat import blackjack

class Memory:
    # output line
    def lights_off(self):
        print("lights are off in room")

    def lights_on(self):
        print("lights are on in room")

    
    # calling line
    def acs(self, input): 
        """used for a uon input to output (call function). It is a modular implementation for a memory module

        Args:
            input (str): used to ask the memory if there is a worthy function. And if there is it is to be called.

        Returns:
            function: calls the function
        """
        mem = {
            "go turn off lights": self.lights_off,
            "go turn on lights": self.lights_on,
            # "go run blackjack": blackjack
        }

        return mem[input]()


# bare and modular implementation for a memory to be used. Custom and simple.