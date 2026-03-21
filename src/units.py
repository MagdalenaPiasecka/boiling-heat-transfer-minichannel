"""Basic unit-conversion helpers used in thermal-flow data processing."""

from __future__ import annotations


def mm_to_m(value_mm: float) -> float:
    """Convert millimetres to metres."""
    return value_mm / 1000.0


def um_to_m(value_um: float) -> float:
    """Convert micrometres to metres."""
    return value_um / 1_000_000.0


def bar_to_pa(value_bar: float) -> float:
    """Convert bar to pascal."""
    return value_bar * 100000.0


def kpa_to_pa(value_kpa: float) -> float:
    """Convert kilopascal to pascal."""
    return value_kpa * 1000.0


def c_to_k(value_c: float) -> float:
    """Convert temperature from degree Celsius to kelvin."""
    return value_c + 273.15


def k_to_c(value_k: float) -> float:
    """Convert temperature from kelvin to degree Celsius."""
    return value_k - 273.15


def g_s_to_kg_s(value_g_s: float) -> float:
    """Convert grams per second to kilograms per second."""
    return value_g_s / 1000.0


def kg_h_to_kg_s(value_kg_h: float) -> float:
    """Convert kilograms per hour to kilograms per second."""
    return value_kg_h / 3600.0


def cm2_to_m2(value_cm2: float) -> float:
    """Convert square centimetres to square metres."""
    return value_cm2 / 10000.0


def mm2_to_m2(value_mm2: float) -> float:
    """Convert square millimetres to square metres."""
    return value_mm2 / 1_000_000.0
