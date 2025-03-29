from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime

class Status(Enum):
	ON_TIME = "ON TIME"
	DELAYED = "DELAYED"
	CANCELLED = "CANCELLED"

class FlightDataProcessor:
	def __init__(self)->None:
		self.flights : List[Dict[str,str]] = []

	def add_flight(self, data:Dict[str,str])->None:
		if any(flight['flight_number'] == data['flight_number'] for flight in self.flights):
			print("flight number already exists")
			return
		self.flights.append(data)

	def remove_flight(self, flight_number:str)->None:
		self.flights = [flight for flight in self.flights if flight['flight_number'] != flight_number]

	def flights_by_status(self,status:Status)->List[Dict[str,str]]:
		return [ flight for flight in self.flights if flight["status"] == status.value ]
		
	def calculate_duration(self,flights:list)->list:
		new_list = []
		for flight in flights:
			departure_time = datetime.strptime(flight["departure_time"], "%Y-%m-%d %H:%M")
			arrival_time = datetime.strptime(flight["arrival_time"], "%Y-%m-%d %H:%M")
			duration = (arrival_time - departure_time).total_seconds() / 60
			duration = int(duration)
			flight["duration_minutes"] = duration
			new_list.append(i)

		return new_list
				
		
	def get_longest_flight(self)->Optional[Dict[str,str]]
		if not self.flights:
			return None
		self.flights = self.calculate_duration(self.flights)
		longest_flight = max(self.flights, key=lambda flight:flight['duration_minutes'])
		return longest_flight
