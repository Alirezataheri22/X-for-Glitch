"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature<800 and neutrons_emitted>500 and temperature*neutrons_emitted<500000:
       return True
    else:
       return False
   



def reactor_efficiency(voltage, current, theoretical_max_power):
    condition1 = ((voltage*current)/theoretical_max_power)*100>=80
    condition2 = 60<=((voltage*current)/theoretical_max_power)*100<80
    condition3 = 30<=((voltage*current)/theoretical_max_power)*100<60
    condition4 = ((voltage*current)/theoretical_max_power)*100<30
    if condition1:
        result= "green"
    elif condition2:
        result="orange"
    elif condition3:
        result="red"
    else:
        result="black"
        
    return result
  


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    condition=temperature*neutrons_produced_per_second
    if condition<0.9*threshold:
        result='LOW'
    elif condition<=1.1*threshold:
        result='NORMAL'
    else:
        result='DANGER'
    return result
        
    
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass
