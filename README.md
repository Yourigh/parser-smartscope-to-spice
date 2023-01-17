# Parser for Labnation SmartScope oscilloscope
Python parser for SmartScope log to be used in LTSpice simulation as PWL supply.
Parse export from smartscope to format fo PWL in SPICE simulation.

Get real measured dat to SPICE simulation.

# Input data

In smartscope, stop the acqusition and log the data (not continuous, better is to log just one scan).
Save file as **source.csv**.

Example:
```
Description,AcquisitionID,AcquisitionStartTimeInSeconds,SamplePeriodInSeconds,SampleTime,ChannelA_Acq00000,ChannelB_Acq00000,ChannelARaw_Acq00000,ChannelBRaw_Acq00000,
SmartScope storage - data recorded on 2022-12-29 4:34:26 PM,0,0,1.6E-07,0,0.0007777484,0.02593515,126,115,
,,,,"=E2+D$2",0.0007777484,0.02593515,126,115,
,,,,,0.0007777484,0.02593515,126,115,
,,,,,0.0007777484,0.02593515,126,115,
,,,,,0.0007777484,0.02593515,126,115,
,,,,,0.0007777484,0.02593515,126,115,
```

# Output pwl.txt

Output file **pwl.txt** is formatted to be directly used for simulation.
```
0 0.0007777484
1.6e-07 0.0007777484
3.2000000000000001e-07 0.0007777484
4.8000000000000006e-07 0.0007777484
6.4000000000000001e-07 0.0007777484
7.9999999999999996e-07 0.0007777484
```

# Usage in LTspice
Simply add voltage source with PWL file.


![image](https://user-images.githubusercontent.com/25552139/212839936-31010e8b-16d6-418f-9639-5e44ce18d739.png)

# Other info

[Smartcope website](https://www.lab-nation.com/)
