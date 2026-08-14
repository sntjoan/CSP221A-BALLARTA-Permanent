from abc import ABC, abstractmethod

class InsufficientBatteryError(Exception):
    def __init__(self, robot_name, required, available):
        self.robot_name = robot_name
        self.required = required
        self.available = available

        message = (
            f"{robot_name} needs {required}% battery for this task "
            f"but only has {available}%."
        )
        super().__init__(message)

    

class Robot(ABC):
    manufacturer = "RoboTech"
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self._battery = 100
        self.battery = battery
        Robot.population += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        self._battery = max(0, min(100, value))

    def use_battery(self, amount):
        if self.battery < amount:
            raise InsufficientBatteryError(
                self.name,
                amount,
                self.battery
            )

        self.battery -= amount

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', battery={self.battery})"

    @abstractmethod
    def perform_task(self):
        pass

class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=5):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity

    def perform_task(self):
        self.use_battery(20)
        return f"{self.name} cleaned an area with {self.dust_capacity}L dust capacity."




