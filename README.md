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


## Process from Pressing the Order Button

### User Clicks the Button:
The user clicks the order button on a specific floor.
This triggers a MOUSEBUTTONDOWN event in Pygame.

Event Handling in Manager Class:
   The Manager class handles this event in the handle_click method.
   The method calculates the actual position considering scroll offsets and checks if the click is on any floor's button.

    Floor Class:
        Each Floor object has a get_invitation_button method that checks if the button was clicked and if the floor is not occupied.
        If true, it returns that the button was clicked.

    Elevator System:
        The Manager class calls the choose_elevator method of the ElevatorSystem class to find the nearest available elevator.
        The ElevatorSystem calculates the nearest elevator based on the current positions and queues of the elevators.

    Updating Floor State:
        The chosen elevator is added to the floor's queue.
        The update_values method of the Floor class is called to update the floor's state and set the timer.

    Elevator Class:
        The elevator starts moving towards the requested floor.
        Once the elevator arrives, it updates its position and removes the floor from its queue.

Involved Classes

   Manager:
     Handles user interactions and manages the connection between floors and elevators.
     Methods: handle_click, update_timer, render.

    Floor:
     Represents a floor in the building.
     Handles button clicks and updates its state.
     Methods: get_invitation_button, update_values, plot_floor.

    ElevatorSystem:
      Manages a collection of elevators.
      Determines which elevator should respond to a floor request.
      Methods: choose_elevator, nearest_elevator, plot_all_elevators.

    Elevator:
      epresents an elevator in the building.
      Moves between floors based on requests.
      Methods: add_call_elevator, update_position, plot_elevator.

### Summary of the Flow
  Button Press: User clicks the order button.
  Event Handling: Manager class detects the click event.
  Button Check: Floor class checks if the button was clicked.
 Find Nearest Elevator: ElevatorSystem finds the nearest available elevator.
 Update Floor: Floor updates its state.
 Move Elevator: Elevator moves to the requested floor and updates its position.

This flow ensures that the system responds to user requests efficiently and updates the state of floors and elevators appropriately.


