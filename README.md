# Elevators_project

## Description
The Elevators Project is a simulation of elevator systems, using pygame 

## Features
- Simulates multiple elevators serving multiple floors.
- Demonstrates various elevator scheduling algorithms.
- Provides visualization of elevator movement and system performance.

## Installation
1. Clone the repository:
   ```bash
git clone https://github.com/yosefmaatuf8/ELEVATORS.git
## classes
- manager: Manages the connection between floors and elevators, handles user interactions, and updates the simulation.
- Building: Initializes and plots the building with multiple floors.
- Floor: Represents a floor in the building, handles button clicks, and updates the state of the floor.
- Button: Represents a button on a floor, changes color when clicked, and plays a sound.
- Timer: Manages and updates the timer for elevator arrival at each floor.
- Elevator_sistem: Manages a collection of elevators and assigns the nearest elevator to a floor request.
- Elevator: Represents an elevator, moves it between floors, and updates its position.
## Functions:
- main: Initializes the manager and starts the main plotting loop.
- main_plot: Initializes Pygame, sets up the display, and runs the main event loop.
## Distance and Time Conversion in Context
Overview

When determining the nearest elevator, the algorithm considers the position of each elevator in relation to the requested floor. It specifically calculates the distance from the last floor in the elevator's queue (if the elevator has pending requests) or from its current location (if it has no pending requests).

## Algorithm for Finding the Nearest Elevator

### 1    Initialization:
The Elevator_sistem class initializes a list of Elevator objects. Each Elevator object represents an elevator in the system.

### 2  Calculating Distance and Time:
The nearest_elevator method iterates through all elevators in the system.
For each elevator, it calculates the time required to reach the requesting floor from the last floor in the elevator's queue. If the elevator has no pending requests, the time is calculated from its current location.
The distance function calculates the absolute distance between the two floors' y-coordinates.
The Convert_distance_to_time function converts this distance into time using the elevator's speed.
        
### 3   Selecting the Nearest Elevator:
The algorithm keeps track of the elevator with the shortest calculated time to reach the requesting floor.
After iterating through all the elevators, it selects the elevator with the minimum time.

### 4    Assigning the Elevator:
The selected elevator is assigned to respond to the request, and the time required for the elevator to reach the requesting floor is returned.

