class PDController:
    """A Proportional-Derivative controller class that computes control signals based on the error between a reference value and an observed value."""

    def __init__(self, K_P: float = 0.15, K_D: float = 0.6): # Define the controller parameters
        self.K_P = K_P  # Proportional gain
        self.K_D = K_D  # Derivative gain
        self.previous_error = 0.0 # Initialize the previous error to zero
        
    def control(self, reference_t: float, observation_t: float) -> float:
        """Uses reference and observed depths at time t, updates stored error, then returns control action."""
        error = reference_t - observation_t  # Calculate the error 
        derivative = error - self.previous_error # Calculate the derivative of the error
        self.previous_error = error  # Update the previous error for the next iteration
        control_signal = self.K_P * error + self.K_D * derivative
        return control_signal
