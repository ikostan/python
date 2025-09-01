"""Functions to prevent a nuclear meltdown."""


# pylint: disable=C0301
def is_criticality_balanced(temperature, neutrons_emitted) -> bool:
    """
    Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted
                             per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second
      is less than 500000.
    """
    return (
        temperature < 800
        and neutrons_emitted > 500
        and (temperature * neutrons_emitted) < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power) -> str:
    """
    Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds
                                  to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency < 30:
        return "black"

    if 30 <= efficiency < 60:
        return "red"

    if 60 <= efficiency < 80:
        return "orange"

    return "green"


def fail_safe(temperature, neutrons_produced_per_second, threshold) -> str:
    """
    Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').
    """
    current_state = (temperature * neutrons_produced_per_second) / 100
    thr_percent = threshold / 100

    if thr_percent - 10 <= current_state <= thr_percent + 10:
        return "NORMAL"

    if current_state < thr_percent - 10:
        return "LOW"

    return "DANGER"
