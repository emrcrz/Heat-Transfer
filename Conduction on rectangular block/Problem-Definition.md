# Conduction on Rectangular Block

![This is an image](https://github.com/emrcrz/Heat-Transfer/blob/main/Conduction%20on%20rectangular%20block/Images/rectangular_block.PNG)

Consider a rectangular block shown in the figure. The thermal properties of the block is stated below.\
Thermal conductivity (k) of the block is 1.1 W/mK and density (ρ) * specific heat constant (c) is 1900 kJ/m3K. There is no heat generation inside the block. The block is subjected to a heat flux (q = 0.2 W/cm2) at a part of the bottom surface and the rest of the bottom wall is isolated. Side walls of the block are also isolated.
The top surface allows to convective heat trasfer with the surrounding and its convective heat transfer coefficient is 10 W/m2K. The ambient temperature is 23 C.
Dimensions of the block is shown below.
- Lx = 1.5 cm
- Ly = 0.5 cm
- a = 0.25 cm

In this code, finite difference numerical method is applied for the problem mentioned above. Computional domain is divided into a hundrant pieces in both the x and y direction. Then, boundary conditions are implemented for each node in the domain. Finally, temperature distribution matrix is obtained due to lineer system solver from numpy library and solution is visualized via a contour plot that you can see below.

![This is an image](https://github.com/emrcrz/Heat-Transfer/blob/main/Conduction%20on%20rectangular%20block/Images/Figure_1.png)

To make sure that the solution is correct, the same case is solved via a commertial software Siemens StarCCM + and the result is compared with it. As shown below, there is a good aligment between two results.  
