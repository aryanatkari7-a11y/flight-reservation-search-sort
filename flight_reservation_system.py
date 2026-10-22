
flights = [
    {
        "flight_no": "AI101",
        "source": "Pune",
        "destination": "Delhi",
        "price": 5500,
        "departure": "09:30",
        "seats": 5
    },
    {
        "flight_no": "6E202",
        "source": "Pune",
        "destination": "Mumbai",
        "price": 2500,
        "departure": "07:00",
        "seats": 4
    },
    {
        "flight_no": "UK303",
        "source": "Pune",
        "destination": "Bangalore",
        "price": 4200,
        "departure": "12:15",
        "seats": 3
    },
    {
        "flight_no": "AI404",
        "source": "Pune",
        "destination": "Delhi",
        "price": 4800,
        "departure": "16:00",
        "seats": 2
    }
]


def display_flights(records):
    if not records:
        print("No flights found.")
        return

    print("\nFlight Details")
    print("-" * 76)
    print(f"{'Flight':<10}{'Source':<12}{'Destination':<15}"
          f"{'Price':<10}{'Departure':<12}{'Seats':<6}")
    print("-" * 76)

    for f in records:
        print(f"{f['flight_no']:<10}{f['source']:<12}"
              f"{f['destination']:<15}{f['price']:<10}"
              f"{f['departure']:<12}{f['seats']:<6}")


# Linear Search
def search_flight(flight_no):
    for flight in flights:
        if flight["flight_no"].lower() == flight_no.lower():
            return flight
    return None


# Bubble Sort
def sort_flights(key):
    records = flights.copy()
    n = len(records)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if records[j][key] > records[j + 1][key]:
                records[j], records[j + 1] = (
                    records[j + 1], records[j]
                )

    return records


# Search flights by destination
def search_destination(destination):
    result = [
        f for f in flights
        if f["destination"].lower() == destination.lower()
    ]
    display_flights(result)


# Reserve a seat
def reserve_seat(flight_no):
    flight = search_flight(flight_no)

    if flight is None:
        print("Flight not found.")
    elif flight["seats"] <= 0:
        print("Sorry, no seats available.")
    else:
        flight["seats"] -= 1
        print("Reservation successful!")
        print("Flight:", flight["flight_no"])
        print("Destination:", flight["destination"])
        print("Ticket Price: Rs.", flight["price"])
        print("Remaining seats:", flight["seats"])


def main():
    while True:
        print("\n===== FLIGHT RESERVATION SYSTEM =====")
        print("1. Display all flights")
        print("2. Search by flight number")
        print("3. Search by destination")
        print("4. Sort flights by price")
        print("5. Sort flights by departure time")
        print("6. Sort flights by flight number")
        print("7. Reserve a seat")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_flights(flights)

        elif choice == "2":
            number = input("Enter flight number: ")
            result = search_flight(number)

            if result:
                display_flights([result])
            else:
                print("Flight not found.")

        elif choice == "3":
            destination = input("Enter destination: ")
            search_destination(destination)

        elif choice == "4":
            display_flights(sort_flights("price"))

        elif choice == "5":
            display_flights(sort_flights("departure"))

        elif choice == "6":
            display_flights(sort_flights("flight_no"))

        elif choice == "7":
            number = input("Enter flight number to reserve: ")
            reserve_seat(number)

        elif choice == "8":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
