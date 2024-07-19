class Formulas:
    def atomicWeight(weights):
        """
        Input a list of lists of percent composition (in form of 0.x) and mass and outputs amu.
        """

        return sum([i * j for i, j in weights])
    
    def molarity(molarity=False, moles=False, volume=False):
        """
        Inputs two of molarity, moles, and volume and outputs the other.
        """

        if molarity == False:
            try:
                volume = float(volume)
                moles = float(moles)
                return moles / volume
            except:
                raise Exception("Invalid input. Input a numerical value.")
        elif moles == False:
            try:
                volume = float(volume)
                moles = float(moles)
                return moles * volume
            except:
                raise Exception("Invalid input. Input a numerical value.")
        elif volume == False:
            try:
                volume = float(volume)
                moles = float(moles)
                return moles / molarity
            except:
                raise Exception("Invalid input. Input a numerical value.")
        else:
            raise Exception("Leave one parameter blank to solve for the missing parameter.")