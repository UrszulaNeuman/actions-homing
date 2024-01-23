#!/bin/env /dls_sw/prod/python3/RHEL7-x86_64/pmac_motorhome/1.5/lightweight-venv/bin/python3
from pmac_motorhome.commands import ControllerType, PostHomeMove, comment, group, motor, plc
from pmac_motorhome.sequences import home_hsw, home_rlim


with plc(
    plc_num=10,
    controller=ControllerType.pbrick,
    filepath="PLC10_P2R_HM.pmc"
    
):
    with group(group_num=2):
        motor(axis=1, jdist=-1000, index=0)
        comment("RLIM")
        home_rlim()

    with group(group_num=3):
        motor(axis=2, jdist=-1000, index=1)
        comment("HSW")
        home_hsw()

    with group(group_num=4):
        motor(axis=3, jdist=-1000, index=2)
        comment("HSW")
        home_hsw()
