def calculate_paracetamol_dose(weight, strength):
    """
    Calculate the volume of paracetamol required for a child based on their weight and the drug strength.
    
    Parameters:
    weight (float): Child's weight in kilograms
    strength (float): Paracetamol concentration in mg per ml (either 24 mg/ml or 50 mg/ml)
    
    Returns:
    float: Volume of paracetamol to administer in milliliters
    
    Raises:
    ValueError: If weight is outside the valid range (10-100 kg)
    ValueError: If strength is not one of the expected concentrations
    """
    # Check if weight is within acceptable range
    if not 10 <= weight <= 100:
        raise ValueError(f"Invalid weight: {weight} kg. Weight must be between 10 and 100 kg.")
    
    # Check if strength is in the range
    if strength not in [24, 50]:  
        raise ValueError(f"Invalid strength: {strength} mg/ml. Must be either 24 mg/ml (120 mg/5 ml) or 50 mg/ml (250 mg/5 ml).")
    
    # Calculate required dose
    dose_mg = weight * 15
    
    # Calculate volume based on strength
    volume_ml = dose_mg / strength
    
    return volume_ml

# Example
# For a 30 kg child using 250 mg/5 ml strength paracetamol
try:
    required_volume = calculate_paracetamol_dose(30, 50)  
    print(f"Required paracetamol volume: {required_volume} ml")
except ValueError as e:
    print(e)