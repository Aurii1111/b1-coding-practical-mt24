class PDController:
    """A Proportional-Derivative controller class that computes control signals based on the error between a reference value and an observed value."""

    def __init__(self, K_P: float = 0.15, K_D: float = 0.6): # Define the controller parameters
        self.K_P = K_P  # Proportional gain
        self.K_D = K_D  # Derivative gain
        self.previous_error = 0.0 # Initialize the previous error to zero

