# Existential-LightBulb-Problem

This assignment aims to complete the existential light bulb problem.

Problem Description****
  Consider a collection of M lightbulbs and N switches. The switches can be placed either in a down or up position. Each lightbulb is connected to two of the switches and it can only be turned off if the two switches connected to it assume a specific configuration.
  We ask if there is a configuration of the switches (down or up for each) so that all of the lightbulbs are on simultaneously.
  
  Suppose we represent the N switches as integers 1 through N. We represent each lightbulb as a pair of integers which encodes the configuration which avoids the 
  lightbulb to be turned off. We will encode the up and down positions by using positive and negative integers. So, if a lightbulb is represented by the pair (i, -j), 
  then this means the lightbulb is connected to switches i and j. If switch i is in the down position and switch j is in the up position, then the lightbulb is off, 
  otherwise the lightbulb will be on. 
  ******
