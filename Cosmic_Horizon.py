# PHYS 495 (Senior Project) - Fall 2021
# Cosmological Horizon Plotting/Visualization Tool
# Developer: Arjun Bamba
# Project Mentor: Professor Vera Gluscevic

from scipy.integrate import quad
from pylab import *
import numpy as np
import math
import matplotlib.pyplot as plt
from functools import partial
from mpl_toolkits import mplot3d

import os
import shutil

from visualizer import draw_horizon

graphing = "Hyperbolic"
custom_plot = False

Omega_m = 0
Omega_r = 0
Omega_k = 0
Omega_l = 0


def ask_default():
    default = input(
        "\nDo you want to plot the Hyperbolic, Euclidean, and Spherical Universes using the default parameters for "
        "Omegas(m, r, l, k), respectively? Please enter 'yes' or 'no'.\n"
    )
    default = default.lower()
    while default != 'yes' and default != 'no':
        print("Invalid input.")
        default = input(
            "Do you want to plot the Hyperbolic, Euclidean, and Spherical Universes using the default parameters for "
            "Omegas(m, r, l, k), respectively? Please enter 'yes' or 'no'.\n"
        )
        default = default.lower()
    return default


def ask_visualize():
    visualize = input(
        "Would you like to make a visualization? Please enter 'yes' or 'no'.\n"
    )
    visualize = visualize.lower()
    while visualize != 'yes' and visualize != 'no':
        print("Invalid input.")
        visualize = input(
            "Would you like to make a visualization? Please enter 'yes' or 'no'.\n"
        )
        visualize = visualize.lower()
    return visualize


def ask_redshift_limit():
    redshift_limit = input(
        "What redshift would you like to plot/visualize until? Bounds: 10 <= redshift <= 1100 \n"
    )

    OutOfBoundsFlag = False
    if redshift_limit.isnumeric() is True or isfloat(redshift_limit) is True:
        if float(redshift_limit) < 10 or float(redshift_limit) > 1100:
            OutOfBoundsFlag = True

    while (redshift_limit.isnumeric() is False and isfloat(redshift_limit) is False) or OutOfBoundsFlag is True:
        print("Invalid input.")
        OutOfBoundsFlag = False
        redshift_limit = input(
            "What redshift would you like to plot/visualize until? Bounds: 10 <= redshift <= 1100 \n"
        )

        if redshift_limit.isnumeric() is True or isfloat(redshift_limit) is True:
            if float(redshift_limit) < 10 or float(redshift_limit) > 1100:
                OutOfBoundsFlag = True

    return float(redshift_limit)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def get_custom_parameter(custom_parameter):
    user_entry = input(
        custom_parameter + " = "
    )

    OutOfBoundsFlag = False
    if user_entry.isnumeric() is True or isfloat(user_entry) is True:
        if float(user_entry) < 0 or float(user_entry) == 0:
            OutOfBoundsFlag = True

    while (user_entry.isnumeric() is False and isfloat(user_entry) is False) or OutOfBoundsFlag is True:
        print("Invalid input.")
        OutOfBoundsFlag = False
        user_entry = input(
            custom_parameter + " = "
        )

        if user_entry.isnumeric() is True or isfloat(user_entry) is True:
            if float(user_entry) < 0 or float(user_entry) == 0:
                OutOfBoundsFlag = True

    return float(user_entry)


# Function to integrate for Cosmological Horizon
def cosmo_horizon(x):
    global graphing
    global custom_plot

    global Omega_m
    global Omega_r
    global Omega_l
    global Omega_k

    result = -1

    # Cosmological Parameters
    if graphing == "Hyperbolic" and custom_plot is False:
        # Hyperbolic Space
        Omega1_m = 0.9
        Omega1_r = (10 ** (-4))
        Omega1_l = 0
        Omega1_k = 1 - Omega1_m - Omega1_r - Omega1_l
        result = (Omega1_m * (1 + x) ** 3 + Omega1_r * (1 + x) ** 4 + Omega1_l + Omega1_k * (1 + x) ** 2) ** (-1 / 2)
    elif graphing == "Euclidean" and custom_plot is False:
        # Flat Space
        Omega2_m = 0.3
        Omega2_r = 10 ** (-4)
        Omega2_k = 0
        Omega2_l = 1 - Omega2_m - Omega2_r
        result = (Omega2_m * (1 + x) ** 3 + Omega2_r * (1 + x) ** 4 + Omega2_l + Omega2_k * (1 + x) ** 2) ** (-1 / 2)
    elif graphing == "Spherical" and custom_plot is False:
        # Spherical Space
        Omega3_m = 0.3
        Omega3_r = 10 ** (-4)
        Omega3_l = 0.8
        Omega3_k = 1 - Omega3_m - Omega3_r - Omega3_l
        result = (Omega3_m * (1 + x) ** 3 + Omega3_r * (1 + x) ** 4 + Omega3_l + Omega3_k * (1 + x) ** 2) ** (-1 / 2)
    elif custom_plot:
        result = (Omega_m * (1 + x) ** 3 + Omega_r * (1 + x) ** 4 + Omega_l + Omega_k * (1 + x) ** 2) ** (-1 / 2)
    else:
        print("Error!")
        print("Graphing is ", graphing)

    return result


def r(x):
    result = np.array(
        list(map(partial(quad, cosmo_horizon, 10000), x))
    )[:, 0]

    return result


def main():
    # Light speed (km/s)
    c = 3*(10**5)

    # Hubble constant (km/s/Mpc)
    H0 = 71

    global graphing
    global custom_plot

    global Omega_m
    global Omega_r
    global Omega_k
    global Omega_l

    print("\nWELCOME TO THE COSMOLOGICAL HORIZON VISUALIZATION TOOL! \n")
    print(
        "Using this tool, you will have the option to plot and visualize either all 3 universes (Hyperbolic, "
        "Euclidean, Spherical) using default parameters or just the Euclidean universe alone using custom "
        "parameters.\nYou will be asked 2 questions: "
    )
    print(
        "\tQuestion 1 will ask whether you would like to plot all 3 universes using default parameters.\n "
        "\t--> If you answer 'yes', it will proceed to plot all 3 universes using the following default parameters: "
    )
    print(
        "\t\t\tHyperbolic Universe Parameters: Ω_k > 0, Ω_m = 0.9, Ω_r = 10^-4, Ω_l = 0 \n"
        "\t\t\tEuclidean Universe Parameters: Ω_k = 0, Ω_m = 0.3, Ω_r = 10^-4, Ω_l = (1 - Ω_m - Ω_r) \n"
        "\t\t\tSpherical Universe Parameters: Ω_k < 0, Ω_m = 0.3, Ω_r = 10^-4, Ω_l = 0.8"
    )
    print(
        "\t--> If you answer 'no', it will ask you for your custom Omega_m and Omega_r parameters to plot/visualize "
        "a Euclidean universe."
    )
    print(
        "\n\tQuestion 2 will ask whether you would like to make a visualization/movie."
    )
    print(
        "\t--> If you answer 'yes', depending on how you answered Question 1, it will proceed to make a visualization "
        "for either all 3 universes or only the Euclidean one. "
    )
    print(
        "\t--> If you answer 'no', it will proceed to simply plot the universe(s).\n"
    )
    print(
        "***********************************************************************************************************"
    )

    plot_default = ask_default()

    redshift_limit = ask_redshift_limit()

    # Redshift Array
    z_begin = 0.1
    # z_final = 1100.1
    z_final = redshift_limit+0.1
    z_step = 0.1
    z = np.arange(z_begin, z_final, z_step)

    universes = ["Hyperbolic", "Euclidean", "Spherical"]

    if plot_default == 'yes':
        visualize = ask_visualize()

        # Cosmological Parameters
        # Hyperbolic Space - Blue
        Omega1_m = 0.9
        Omega1_r = (10 ** (-4))
        Omega1_l = 0
        Omega1_k = 1 - Omega1_m - Omega1_r - Omega1_l

        # Euclidean (Flat) Space - Red
        Omega2_m = 0.3
        Omega2_r = 10 ** (-4)
        Omega2_k = 0
        Omega2_l = 1 - Omega2_m - Omega2_r

        # Spherical Space - Black
        Omega3_m = 0.3
        Omega3_r = 10 ** (-4)
        Omega3_l = 0.8
        Omega3_k = 1 - Omega3_m - Omega3_r - Omega3_l

        plt.figure(1)

        for universe in universes:
            if universe == "Hyperbolic":
                graphing = "Hyperbolic"
                integral = -r(z)
                argument_first = math.sqrt(Omega1_k)
                argument_second = integral
                # argument_result = np.multiply(argument_first, argument_second)
                argument_result = argument_first * argument_second

                f2 = np.vectorize(math.sinh)
                argument_result = f2(argument_result)
                coeff = c / (H0 * math.sqrt(Omega1_k))
                integralCosmoHorizon = np.multiply(coeff, argument_result)

                plt.plot(
                    np.log10(z), integralCosmoHorizon, color='b',
                    label='Hyperbolic Universe $Ω_{k}$>0, $Ω_{m}$=0.9, $Ω_{r}$=$10^{-4}$, $Ω_{l}$=0'
                )

                if visualize == 'yes':
                    # Create directory
                    dirName = "images_Hyperbolic"

                    # Create target Directory if it doesn't exist. If it already exists, delete and recreate empty one
                    if not os.path.exists(dirName):
                        os.mkdir(dirName)
                    else:
                        shutil.rmtree(dirName)
                        os.mkdir(dirName)

                    x_to_plot = np.log10(z)
                    y_to_plot = integralCosmoHorizon

                    imageNumber = 0
                    for i in z[99::100]:
                        imageNumber += 1
                        distance_for_redshift = np.interp(np.log10(i), x_to_plot, y_to_plot)
                        print("Redshift: " + str(i))
                        print("Distance for Redshift: " + str(distance_for_redshift))
                        draw_horizon(i, distance_for_redshift, "Hyperbolic", imageNumber)

                    os.system(
                        "ffmpeg -start_number 1 -f image2 -r 10 -i ./images_Hyperbolic/image%d.png -vcodec mpeg4 -y ./videos/Visualization_Hyperbolic.mp4"
                    )

            elif universe == "Euclidean":
                graphing = "Euclidean"
                integral = -r(z)
                coeff = c / H0
                integralCosmoHorizon = np.multiply(coeff, integral)

                plt.plot(
                    np.log10(z), integralCosmoHorizon, color='r',
                    label='Euclidean Universe $Ω_{k}$=0, $Ω_{m}$=0.3, $Ω_{r}$=$10^{-4}$, $Ω_{l}$=(1-$Ω_{m}$-$Ω_{r}$)'
                )

                if visualize == 'yes':
                    # Create directory
                    dirName = "images_Euclidean"

                    # Create target Directory if it doesn't exist. If it already exists, delete and recreate empty one
                    if not os.path.exists(dirName):
                        os.mkdir(dirName)
                    else:
                        shutil.rmtree(dirName)
                        os.mkdir(dirName)

                    x_to_plot = np.log10(z)
                    y_to_plot = integralCosmoHorizon

                    imageNumber = 0
                    for i in z[99::100]:
                        imageNumber += 1
                        distance_for_redshift = np.interp(np.log10(i), x_to_plot, y_to_plot)
                        print("Redshift: " + str(i))
                        print("Distance for Redshift: " + str(distance_for_redshift))
                        draw_horizon(i, distance_for_redshift, "Euclidean", imageNumber)

                    os.system(
                        "ffmpeg -start_number 1 -f image2 -r 10 -i ./images_Euclidean/image%d.png -vcodec mpeg4 -y ./videos/Visualization_Euclidean.mp4"
                    )

            elif universe == "Spherical":
                graphing = "Spherical"
                integral = -r(z)
                argument_first = math.sqrt(abs(Omega1_k))
                argument_second = integral
                argument_result = np.multiply(argument_first, argument_second)

                f2 = np.vectorize(math.sin)
                argument_result = f2(argument_result)
                coeff = c / (H0 * math.sqrt(abs(Omega1_k)))
                integralCosmoHorizon = np.multiply(coeff, argument_result)

                plt.plot(
                    np.log10(z), integralCosmoHorizon, color='k',
                    label='Spherical Universe $Ω_{k}$<0, $Ω_{m}$=0.3, $Ω_{r}$=$10^{-4}$, $Ω_{l}$=0.8'
                )

                if visualize == 'yes':
                    # Create directory
                    dirName = "images_Spherical"

                    # Create target Directory if it doesn't exist. If it already exists, delete and recreate empty one
                    if not os.path.exists(dirName):
                        os.mkdir(dirName)
                    else:
                        shutil.rmtree(dirName)
                        os.mkdir(dirName)

                    x_to_plot = np.log10(z)
                    y_to_plot = integralCosmoHorizon

                    imageNumber = 0
                    for i in z[99::100]:
                        imageNumber += 1
                        distance_for_redshift = np.interp(np.log10(i), x_to_plot, y_to_plot)
                        print("Redshift: " + str(i))
                        print("Distance for Redshift: " + str(distance_for_redshift))
                        draw_horizon(i, distance_for_redshift, "Spherical", imageNumber)

                    os.system(
                        "ffmpeg -start_number 1 -f image2 -r 10 -i ./images_Spherical/image%d.png -vcodec mpeg4 -y ./videos/Visualization_Spherical.mp4"
                    )

        plt.xlabel('Redshift log10(z)')
        plt.ylabel('Cosmological Horizon (Mpc)')
        plt.title('Cosmological Horizon vs Redshift')
        plt.legend()
        plt.show()

    elif plot_default == "no":
        # print("Which universe do you want to plot - hyperbolic, euclidean (flat), or spherical? ")
        custom_plot = True

        print(
            "Please enter your custom Omega_m and Omega_r parameters for a Euclidean universe (must be greater than 0):"
        )
        Omega_m = get_custom_parameter("Omega_m")
        Omega_r = get_custom_parameter("Omega_r")
        Omega_k = 0
        Omega_l = 1 - Omega_m - Omega_r

        visualize = ask_visualize()

        graphing = "Euclidean"
        integral = -r(z)
        coeff = c / H0
        integralCosmoHorizon = np.multiply(coeff, integral)
        plt.plot(
            np.log10(z), integralCosmoHorizon, color='r',
            label='Euclidean Universe $Ω_{k}$=0, $Ω_{m}$=' + str(Omega_m) + ', $Ω_{r}$=' + str(Omega_r) + ', $Ω_{l}$=(1-$Ω_{m}$-$Ω_{r}$)'
        )

        if visualize == 'yes':
            # Create directory
            dirName = "images_CustomEuclidean"

            # Create target Directory if it doesn't exist. If it already exists, delete and recreate empty one
            if not os.path.exists(dirName):
                os.mkdir(dirName)
            else:
                shutil.rmtree(dirName)
                os.mkdir(dirName)

            x_to_plot = np.log10(z)
            y_to_plot = integralCosmoHorizon

            imageNumber = 0
            for i in z[99::100]:
                imageNumber += 1
                distance_for_redshift = np.interp(np.log10(i), x_to_plot, y_to_plot)
                print("Redshift: " + str(i))
                print("Distance for Redshift: " + str(distance_for_redshift))
                draw_horizon(i, distance_for_redshift, "CustomEuclidean", imageNumber)

            os.system(
                "ffmpeg -start_number 1 -f image2 -r 10 -i ./images_CustomEuclidean/image%d.png -vcodec mpeg4 -y ./videos/Visualization_CustomEuclidean.mp4"
            )

        plt.xlabel('Redshift log10(z)')
        plt.ylabel('Cosmological Horizon (Mpc)')
        plt.title('Cosmological Horizon vs Redshift')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()






