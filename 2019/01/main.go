package main

import (
	"io/ioutil"
	"log"
	"math"
	"strconv"
	"strings"
)

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	trimmed := strings.TrimSpace(string(b))
	lines := strings.Split(trimmed, "\n")

	totalFuel := 0
	for _, massStr := range lines {
		mass, err := strconv.Atoi(massStr)
		if err != nil {
			log.Fatal(err)
		}
		totalFuel += fuelFor(mass)
	}
	log.Printf("Total fuel for mass: %d\n", totalFuel)

	totalFuel = 0
	for _, massStr := range lines {
		mass, err := strconv.Atoi(massStr)
		if err != nil {
			log.Fatal(err)
		}
		fuel := fuelFor(mass)
		totalFuel += fuel
		for extraFuel := fuelFor(fuel); extraFuel != 0; extraFuel = fuelFor(extraFuel) {
			totalFuel += extraFuel
		}
	}

	log.Printf("Total fuel for mass and fuel: %d\n", totalFuel)
}

func fuelFor(mass int) int {
	fuel := int(math.Floor(float64(mass)/3) - 2)
	if fuel < 0 {
		fuel = 0
	}
	return fuel
}
