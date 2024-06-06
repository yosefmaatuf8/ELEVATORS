import pygame as pg
from setting import *
from class_manager import *
from plot_main import *
def main():
    if setting_corect():
        Manager = manager()
        main_plot(Manager)
main   ()
