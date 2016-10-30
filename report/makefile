# ==============================================================================
# Report
#
# @author: Elisha Lai
# @description: Makefile for report.cpp
# @version: 0.0.1 02/11/2015
# ==============================================================================

all:
	@echo "Compiling..."
	g++ -Wall -MMD -o report report.cpp
	@echo "Granting file execution permissions..."
	chmod +x report

run: all
	@echo "Running..."
	./report 

.PHONY: clean

clean:
	@echo "Cleaning..."
	rm report
