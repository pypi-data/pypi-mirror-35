#!/usr/bin/env python
import subprocess

for ref_band in ["H", "J", "K", "Z", "Y", "SELF"]:
    for snr in [50, 75, 100, 125, 150, 175, 200, 225]:
        subprocess.call(
            "../Codes/eniric/eniric_scripts/nIR_precision.py -b ALL --snr {} --ref_band {}".format(
                snr, ref_band
            ),
            shell=True,
        )
