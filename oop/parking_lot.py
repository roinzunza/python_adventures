"""
Create a parking lot

objects
 - parking lot
 - parking space
 - Vehicle (abstract)

actions
- checks available parking spots and assigns a spot to a car if available
- removes a car from a space
"""

from abc import ABCMeta, abstractmethod

class ParkingLot:
    pass

class ParkingSpace:
    pass

class Vehicle(ABCMeta):
    pass