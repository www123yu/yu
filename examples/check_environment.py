"""检查 Python 科研依赖与理想 Buck 直流关系；不执行开关仿真。"""

from importlib import import_module, metadata
from math import isclose


def main() -> None:
    for module, distribution in (
        ("numpy", "numpy"),
        ("scipy", "scipy"),
        ("matplotlib", "matplotlib"),
        ("pandas", "pandas"),
        ("sympy", "sympy"),
        ("control", "control"),
    ):
        import_module(module)
        print(f"{distribution}: {metadata.version(distribution)}")

    # Ideal lossless Buck converter, steady state and continuous conduction.
    # This relation alone does not validate ripple, stability, or real hardware.
    input_voltage_v = 48.0
    duty_ratio = 0.25
    output_voltage_v = duty_ratio * input_voltage_v
    if not isclose(output_voltage_v, 12.0, rel_tol=1e-12):
        raise RuntimeError("Ideal Buck relation check failed")
    print(f"Ideal Buck DC relation: Vout = D * Vin = {output_voltage_v:.1f} V")
    print("Environment check passed; no switching simulation was performed.")


if __name__ == "__main__":
    main()
