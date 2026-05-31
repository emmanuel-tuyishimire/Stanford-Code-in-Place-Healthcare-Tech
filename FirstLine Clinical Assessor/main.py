def get_valid_vital(prompt, min_val, max_val, is_float=False):
    """
    Helper function to ensure the user enters a medically possible number.
    It loops until a valid number within the realistic boundaries is provided.
    """
    while True:
        user_input = input(prompt)
        try:
            # Convert to float for Temp, integer for everything else
            if is_float:
                val = float(user_input)
            else:
                val = int(user_input)
                
            # The Clinical Sanity Check
            if val < min_val or val > max_val:
                print("   ❌ ERROR: Unrealistic value (" + str(val) + "). Please verify and re-enter.")
            else:
                return val # It passed the test! Send it back.
                
        except ValueError:
            print("   ❌ ERROR: Invalid input. Please enter a number.")
import random
import datetime
def main():
    print("=== Emergency Department Triage Assistant ===")
    patient_id = "PT-" + str(random.randint(10000, 99999))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Patient ID: " + patient_id + " | Time: " + timestamp)
    print("Please enter the patient's current vital signs.")
    print("-" * 45)
    
    # Milestone 1: Patient Intake (Now using our secure helper function!)
    # The numbers at the end define the (minimum, maximum) physically possible limits
    temperature = get_valid_vital("Temperature (°C): ", 20.0, 45.0, True)
    heart_rate = get_valid_vital("Heart Rate (bpm): ", 0, 300, False)
    resp_rate = get_valid_vital("Respiratory Rate (breaths/min): ", 0, 100, False)
    systolic_bp = get_valid_vital("Systolic Blood Pressure (mmHg): ", 0, 300, False)
    diastolic_bp = get_valid_vital("Diastolic Blood Pressure (mmHg): ", 0, 200, False)
    spo2 = get_valid_vital("Oxygen Saturation (SpO2 %): ", 0, 100, False)
    pain_level = get_valid_vital("Pain Level (0-10): ", 0, 10, False)
    
    # Milestone 2: Standard Adult Baselines
    adult_baselines = {
        "temp_min": 36.5, "temp_max": 37.5,
        "hr_min": 60,     "hr_max": 100,
        "rr_min": 12,     "rr_max": 20,
        "sys_min": 90,    "sys_max": 120,
        "dia_min": 60,    "dia_max": 80,
        "spo2_min": 95
    }
    
    print("-" * 45)
    print("Vitals recorded successfully. Ready for evaluation...")

    # Milestone 3: The Complete Triage Logic
    print("\n=== SYSTEM ASSESSMENT ===")
    flags = 0 
    
    # Check Heart Rate
    if heart_rate > adult_baselines["hr_max"]:
        print("⚠️ FLAG: Tachycardia detected.")
        flags += 1
    elif heart_rate < adult_baselines["hr_min"]:
        print("⚠️ FLAG: Bradycardia detected.")
        flags += 1
        
    # Check Temperature
    if temperature > adult_baselines["temp_max"]:
        print("⚠️ FLAG: Febrile (High Temperature).")
        flags += 1
    elif temperature < adult_baselines["temp_min"]:
        print("⚠️ FLAG: Hypothermia (Low Temperature).")
        flags += 1

    # Check Respiratory Rate
    if resp_rate > adult_baselines["rr_max"]:
        print("⚠️ FLAG: Tachypnea (High Respiratory Rate).")
        flags += 1
    elif resp_rate < adult_baselines["rr_min"]:
        print("⚠️ FLAG: Bradypnea (Low Respiratory Rate).")
        flags += 1

    # Check Blood Pressure
    if systolic_bp > adult_baselines["sys_max"] or diastolic_bp > adult_baselines["dia_max"]:
        print("⚠️ FLAG: Hypertension (High Blood Pressure).")
        flags += 1
    elif systolic_bp < adult_baselines["sys_min"] or diastolic_bp < adult_baselines["dia_min"]:
        print("⚠️ FLAG: Hypotension (Low Blood Pressure).")
        flags += 1
        
    # Check Oxygen Saturation
    if spo2 < adult_baselines["spo2_min"]:
        print("⚠️ FLAG: Hypoxia (Low Oxygen).")
        flags += 1
        
    # Check Pain Level
    if pain_level >= 7:
        print("⚠️ FLAG: Severe Pain reported.")
        flags += 1
        
    # If no flags were raised
    if flags == 0:
        print("✅ All evaluated vitals are within normal limits.")
        
    # Milestone 4: Final Triage Priority & Clinical Recommendations
    print("\n=== FINAL TRIAGE PRIORITY & NEXT STEPS ===")
    
    if spo2 <= 90 or flags >= 3:
        print("🔴 CRITICAL: Immediate medical intervention required.")
        print("\n>> RECOMMENDED CLINICAL ACTIONS:")
        print("   - Activate emergency response / alert attending physician.")
        print("   - Move patient to resuscitation bay immediately.")
        print("   - Prepare for supplemental oxygen and continuous ECG monitoring.")
        print("   - Ensure crash cart and IV access kits are on standby.")
        
    elif flags >= 1 or pain_level >= 4:
        print("🟡 URGENT: Patient needs prompt evaluation.")
        print("\n>> RECOMMENDED CLINICAL ACTIONS:")
        print("   - Escort patient to an available assessment bed.")
        print("   - Initiate continuous pulse oximetry and cardiac monitoring.")
        if pain_level >= 7:
            print("   - ⚠️ Flag for rapid analgesic intervention per standing orders.")
        print("   - Prepare for potential IV access and stat lab draws.")
        
    else:
        print("🟢 ROUTINE: Patient is stable for standard queue.")
        print("\n>> RECOMMENDED CLINICAL ACTIONS:")
        print("   - Direct patient to the standard waiting area.")
        print("   - Advise patient to notify staff immediately if condition changes.")
        print("   - Schedule routine reassessment of vitals in 60 minutes.")
        
    print("-" * 45)

if __name__ == '__main__':
    main()