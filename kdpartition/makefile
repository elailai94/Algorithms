# ==============================================================================
# Kd-tree Partition
#
# @author: Elisha Lai
# @description: Makefile for kdpartition.cpp
# @version: 0.0.1 19/11/2015
# ==============================================================================

all:
	@echo "Compiling..."
	g++ -Wall -MMD -o kdpartition kdpartition.cpp
	@echo "Granting file execution permissions..."
	chmod +x kdpartition

run: all
	@echo "Running..."
	./kdpartition 

.PHONY: clean

clean:
	@echo "Cleaning..."
	rm kdpartition
