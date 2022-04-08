number_of_days = int(input())

viewed_patients_count = 0
not_viewed_patients_count = 0
doctors = 7

for day in range(1, number_of_days + 1):
    patients = int(input())

    if day % 3 != 0:
        if patients <= doctors:

            viewed_patients = patients
            viewed_patients_count += viewed_patients
            not_viewed_patients_count += 0
        elif patients > doctors:

            viewed_patients = doctors
            viewed_patients_count += viewed_patients
            not_viewed_patients = patients - viewed_patients
            not_viewed_patients_count += not_viewed_patients
    elif day % 3 == 0 and not_viewed_patients_count <= viewed_patients_count:

        if patients <= doctors:

            viewed_patients = patients
            viewed_patients_count += viewed_patients
            not_viewed_patients_count += 0
        elif patients > doctors:

            viewed_patients = doctors
            viewed_patients_count += viewed_patients
            not_viewed_patients = patients - viewed_patients
            not_viewed_patients_count += not_viewed_patients
    elif day % 3 == 0 and not_viewed_patients_count > viewed_patients_count:
        doctors += 1
        if patients <= doctors:

            viewed_patients = patients
            viewed_patients_count += viewed_patients
            not_viewed_patients_count += 0
        elif patients >= doctors:

            viewed_patients = doctors
            viewed_patients_count += viewed_patients
            not_viewed_patients = patients - viewed_patients
            not_viewed_patients_count += not_viewed_patients

print(f"Treated patients: {viewed_patients_count}.")
print(f"Untreated patients: {not_viewed_patients_count}.")
