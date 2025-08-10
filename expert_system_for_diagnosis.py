def get_user_input(prompt):
    """Prompt the user and validate the response as 'yes' or 'no'."""
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in ['yes', 'no']:
            return response
        print("❗ Invalid input. Please type 'yes' or 'no'.")


def collect_symptoms():
    """Ask the user a series of diagnostic questions."""
    print("===========================================")
    print("  Expert System for Computer Diagnostics 💻")
    print("===========================================\n")
    print("Answer the following questions truthfully to help diagnose your issue.\n")

    return {
        "not_turning_on": get_user_input("Does the computer fail to turn on?"),
        "beeping_sounds": get_user_input("Do you hear beeping sounds when turning it on?"),
        "overheating": get_user_input("Is the computer getting unusually hot?"),
        "slow_performance": get_user_input("Is the system running unusually slow?"),
        "blue_screen": get_user_input("Do you get a blue screen error (BSOD)?"),
        "frequent_restarts": get_user_input("Is your computer restarting frequently?"),
        "no_display": get_user_input("Does the screen remain black or show no display?"),
        "fan_noise": get_user_input("Is the fan making loud or unusual noises?"),
        "usb_not_working": get_user_input("Are USB devices not being detected?"),
        "internet_issues": get_user_input("Is the computer unable to connect to the internet?")
    }


def diagnose(symptoms):
    """Diagnose based on the collected symptoms and explain the reasoning and resolution."""
    print("\nAnalyzing symptoms...\n")

    if symptoms["not_turning_on"] == "yes" and symptoms["beeping_sounds"] == "yes":
        return (
            "🧠 Diagnosis: RAM Failure\n"
            "🔍 Reason: Beeping on startup often indicates memory issues.\n"
            "🛠️ Resolution: Reseat or replace the RAM module. Try one stick at a time if using multiple."
        )

    elif symptoms["no_display"] == "yes" and symptoms["not_turning_on"] == "no":
        return (
            "🧠 Diagnosis: GPU or Display Issue\n"
            "🔍 Reason: Power is on but there's no display, suggesting a graphics card or monitor fault.\n"
            "🛠️ Resolution: Check monitor cables, test with another screen or reseat the graphics card."
        )

    elif symptoms["overheating"] == "yes" and symptoms["fan_noise"] == "yes":
        return (
            "🧠 Diagnosis: Cooling System Failure\n"
            "🔍 Reason: Loud fans and overheating typically point to dust buildup or faulty cooling.\n"
            "🛠️ Resolution: Clean internal components and ensure fans are functioning properly."
        )

    elif symptoms["slow_performance"] == "yes" and symptoms["overheating"] == "yes":
        return (
            "🧠 Diagnosis: CPU Throttling\n"
            "🔍 Reason: Overheating causes CPU to reduce speed to avoid damage.\n"
            "🛠️ Resolution: Improve cooling, clean vents, and avoid running heavy tasks in hot environments."
        )

    elif symptoms["blue_screen"] == "yes" and symptoms["frequent_restarts"] == "yes":
        return (
            "🧠 Diagnosis: OS or Driver Corruption\n"
            "🔍 Reason: Blue screens and restarts are signs of deep software or driver conflicts.\n"
            "🛠️ Resolution: Boot in Safe Mode and update/reinstall drivers or perform a system restore."
        )

    elif symptoms["usb_not_working"] == "yes" and symptoms["not_turning_on"] == "no":
        return (
            "🧠 Diagnosis: USB Port or Motherboard Issue\n"
            "🔍 Reason: Non-functional USBs may indicate physical port failure or driver issues.\n"
            "🛠️ Resolution: Try different ports, reinstall USB drivers, or check for hardware damage."
        )

    elif symptoms["internet_issues"] == "yes":
        return (
            "🧠 Diagnosis: Network Adapter Issue\n"
            "🔍 Reason: No internet could be due to a disabled or faulty adapter.\n"
            "🛠️ Resolution: Check if the adapter is enabled, reinstall network drivers, or reset network settings."
        )

    elif symptoms["slow_performance"] == "yes":
        return (
            "🧠 Diagnosis: Resource Overload or Malware\n"
            "🔍 Reason: Unusual slowness is often due to background apps or malware.\n"
            "🛠️ Resolution: Check task manager, uninstall unnecessary software, and run a malware scan."
        )

    elif symptoms["not_turning_on"] == "yes":
        return (
            "🧠 Diagnosis: Power Supply Failure\n"
            "🔍 Reason: If the device doesn't power on at all, it likely has PSU or battery problems.\n"
            "🛠️ Resolution: Verify the power source, try a different cable, or replace the PSU/battery."
        )

    else:
        return (
            "🤔 Diagnosis: Unknown\n"
            "🔍 Reason: The symptoms do not match any known patterns.\n"
            "🛠️ Resolution: Consult a qualified technician for a thorough hardware/software inspection."
        )


def main():
    try:
        symptoms = collect_symptoms()
        result = diagnose(symptoms)
        print("\n" + result + "\n")
    except Exception as e:
        print("\n⚠️ An unexpected error occurred. Please try again.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    main()
