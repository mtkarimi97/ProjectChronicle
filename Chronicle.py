import matplotlib.pyplot as plt;

#Prompt user for value
year = input("Enter the desired year: ");

def convertHijri(year):

    hijriYear = ((year - 622) * 33) / 32;
    return hijriYear;

hijriYear = convertHijri(year);
print("{0} AH".format(hijriYear));

hijri, = plt.plot([year, 1500], [hijriYear, 1500], label='hijri');
plt.legend(handles=[hijri]);
plt.ylabel("Converted Calendar Year");
plt.xlabel("Gregorian Calendar Year");
plt.show();