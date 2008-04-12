# Basic Ternary Inverter, implemented with CD4007
#
# TODO: embed with tinv.asc, netlist generated by

nodes = ("Vin", "PTI_Out", "STI_Out", "NTI_Out")

# Dual MOSFET Complementary Pair + Binary Inverter
parts_generated = ["CD4007"]
parts_consumed = ["MP", "MN"]
parts_kept = ["RP", "RN"]

# Based on pinout from http://www.cedmagic.com/tech-info/data/cd4016.pdf
pins = [ 
        { 
            "Vin": ("CD4007", 6), 
            "PTI_Out": ("CD4007", 13),
            "NTI_Out": ("CD4007", 8), 
            "STI_Out": "STI_Out",
        },
        { 
            "Vin": ("CD4007", 1), 
            "PTI_Out": ("CD4007", 3),
            "NTI_Out": ("CD4007", 5), 
            "STI_Out": "STI_Out",
        },
       ]

# Always connected once if use once or more
global_pins = { "$G_Vdd": ("CD4007", 14), "$G_Vss": ("CD4007", 7) }

