departure_time = input().strip()
travel_time_hours, travel_time_minutes = map(int, input().split())
departure_hours, departure_minutes = map(int, departure_time.split(':'))
total_minutes = departure_hours * 60 + departure_minutes + travel_time_hours * 60 + travel_time_minutes
arrival_hours = (departure_hours + travel_time_hours + (departure_minutes + travel_time_minutes) // 60) % 24
arrival_minutes = (departure_minutes + travel_time_minutes) % 60
arrival_time = "{:02d}:{:02d}".format(arrival_hours, arrival_minutes)
print(arrival_time)
