def main():
    time = input("Time: ").strip().lower()
    time = convert(time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")



def convert(time):
    if time.endswith("am") or time.endswith("pm"):
        time, twelveTime = time.split(" ")
        hours, minutes = time.split(":")
        if twelveTime == "pm":
            hours = float(hours) + 12
    else:
        hours, minutes = time.split(":")

    time = float(hours) + round((float(minutes) / 60), 2)
    return time
    


if __name__ == "__main__":
    main()
