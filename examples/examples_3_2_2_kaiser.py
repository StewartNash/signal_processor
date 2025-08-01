import math
import numpy as np
import matplotlib.pyplot as plt
from signal_processor.finite_impulse_response import kaiser_coefficients, kaiser_filter_order, kaiser_bandpass, magnitude_response, FilterType

#---------------------------------
# Example 5.6: Bandpass FIR Filter
#---------------------------------
# Design a bandpass filter with the following specifications
# Passband: fp1 = 120 Hz, fp2 = 180 Hz, Ap = 0.5 dB
# Stopband: fs1 = 60 Hz, fs2 = 240 Hz, As = 35 dB
# Sampling frequency (F) = 600 Hz

# Ripple parameter, delta = 0.0177828 (Eq. 5.49)
# Actual stopband attenuation, As = 35 dB (Eq. 5.44)
# Parameter D, D = 1.883705 (Eq. 5.50)
# Filter order, N = 21 (Eq. 5.51)
# Non-causal impulse response (Eqs. 5.60, 5.61, 5.39, 5.52)

# (causal index, non-causal index, hd[n], ak[n], ak[n]hd[n])

fir_coefficients = [
	( 0, -10,  0.000000000, 0.243827427,  0.000000000),
	( 1,  -9, -0.000000000, 0.342116577,  0.000000000),
	( 2,  -8, -0.075682673, 0.445786231, -0.033738293),
	( 3,  -7,  0.000000000, 0.550960881,  0.000000000),
	( 4,  -6,  0.062365952, 0.653488069,  0.040755406),
	( 5,  -5,  0.000000000, 0.749153304,  0.000000000),
	( 6,  -4,  0.093548928, 0.833903592,  0.078010787),
	( 7,  -3, -0.000000000, 0.904066210,  0.000000000),
	( 8,  -2, -0.302730691, 0.956549514, -0.289576896),
	( 9,  -1,  0.000000000, 0.989013547,  0.000000000),
	(10,   0,  0.400000000, 1.000000000,  0.400000000),
	(11,   1,  0.000000000, 0.989013547,  0.000000000),
	(12,   2, -0.302730691, 0.956549514, -0.289576896),
	(13,   3, -0.000000000, 0.904066210,  0.000000000),
	(14,   4,  0.093548928, 0.833903592,  0.078010787),
	(15,   5,  0.000000000, 0.749153304,  0.000000000),
	(16,   6,  0.062365952, 0.653488069,  0.040755406),
	(17,   7,  0.000000000, 0.550960881,  0.000000000),
	(18,   8, -0.075682673, 0.445786231, -0.033738293),
	(19,   9, -0.000000000, 0.342116577,  0.000000000),
	(20,  10,  0.000000000, 0.243827427,  0.000000000),
]

# (frequency, response)

frequency_response = [
	(0.000, -40.95871194),
	(0.005, -41.53972527),
	(0.010, -43.47408288),
	(0.015, -47.67955806),
	(0.020, -60.37714136),
	(0.025, -52.26415913),
	(0.030, -44.98973102),
	(0.035, -41.72196862),
	(0.040, -40.19650153),
	(0.045, -39.93992605),
	(0.050, -40.98592055),
	(0.055, -43.93314474),
	(0.060, -51.84050200),
	(0.065, -53.62988040),
	(0.070, -43.12179137),
	(0.075, -38.87616856),
	(0.080, -36.84238683),
	(0.085, -36.48371486),
	(0.090, -38.30447119),
	(0.095, -46.28836755),
	(0.100, -42.06227736),
	(0.105, -31.41634109),
	(0.110, -25.56272301),
	(0.115, -21.33161805),
	(0.120, -17.97897906),
	(0.125, -15.20263872),
	(0.130, -12.84694166),
	(0.135, -10.81976064),
	(0.140, -9.06130297),
	(0.145, -7.53009991),
	(0.150, -6.19588906),
	(0.155, -5.03564985),
	(0.160, -4.03122748),
	(0.165, -3.16781809),
	(0.170, -2.43294818),
	(0.175, -1.81575053),
	(0.180, -1.30642476),
	(0.185, -0.89581703),
	(0.190, -0.57508097),
	(0.195, -0.33539938),
	(0.200, -0.16775908),
	(0.205, -0.06278179),
	(0.210, -0.01062274),
	(0.215, -0.00095600),
	(0.220, -0.02306906),
	(0.225, -0.06608794),
	(0.230, -0.11934344),
	(0.235, -0.17286909),
	(0.240, -0.21799247),
	(0.245, -0.24794964),
	(0.250, -0.25842937),
	(0.255, -0.24794964),
	(0.260, -0.21799247),
	(0.265, -0.17286909),
	(0.270, -0.11934344),
	(0.275, -0.06608794),
	(0.280, -0.02306906),
	(0.285, -0.00095600),
	(0.290, -0.01062274),
	(0.295, -0.06278179),
	(0.300, -0.16775908),
	(0.305, -0.33539938),
	(0.310, -0.57508097),
	(0.315, -0.89581703),
	(0.320, -1.30642476),
	(0.325, -1.81575053),
	(0.330, -2.43294818),
	(0.335, -3.16781809),
	(0.340, -4.03122748),
	(0.345, -5.03564985),
	(0.350, -6.19588906),
	(0.355, -7.53009991),
	(0.360, -9.06130297),
	(0.365, -10.81976064),
	(0.370, -12.84694166),
	(0.375, -15.20263872),
	(0.380, -17.97897906),
	(0.385, -21.33161805),
	(0.390, -25.56272301),
	(0.395, -31.41634109),
	(0.400, -42.06227736),
	(0.405, -46.28836755),
	(0.410, -38.30447119),
	(0.415, -36.48371486),
	(0.420, -36.84238683),
	(0.425, -38.87616856),
	(0.430, -43.12179137),
	(0.435, -53.62988040),
	(0.440, -51.84050200),
	(0.445, -43.93314474),
	(0.450, -40.98592055),
	(0.455, -39.93992605),
	(0.460, -40.19650153),
	(0.465, -41.72196862),
	(0.470, -44.98973102),
	(0.475, -52.26415913),
	(0.480, -60.37714136),
	(0.485, -47.67955806),
	(0.490, -43.47408288),
	(0.495, -41.53972527)
]

FREQUENCY_RESOLUTION = 500

# Filter specifications
passband_frequency_low = 120
passband_frequency_high = 180
specified_passband_ripple = 0.5
stopband_frequency_low = 60
stopband_frequency_high = 240
minimum_stopband_attenuation = 35
sampling_frequency = 600

filter_type = FilterType.BANDPASS

filter_order, delta, minimum_stopband_attenuation, parameter_d = kaiser_filter_order(filter_type,
	passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	sampling_frequency,
	specified_passband_ripple,
	minimum_stopband_attenuation)

kaiser_coeffs, alpha = kaiser_coefficients(filter_order, minimum_stopband_attenuation)

impulse_response = kaiser_bandpass(passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	sampling_frequency,
	filter_order,
	kaiser_coeffs)
	
maximum_frequency = sampling_frequency / 2
frequencies = np.linspace(0, maximum_frequency, FREQUENCY_RESOLUTION)
angular_frequencies = frequencies * 2 * math.pi

response_magnitude = [magnitude_response(w, impulse_response, sampling_frequency, filter_order)
                      for w in angular_frequencies]
response_magnitude_db = [20 * math.log10(max(abs(m), 1e-10)) for m in response_magnitude]

# Plot
plt.figure(figsize=(8,4))
plt.plot(frequencies, response_magnitude_db)
plt.xlim(0, sampling_frequency / 2)
plt.ylim(-100, 5)
plt.axvline(stopband_frequency_low, color='red', linestyle='--', label='Stopband Low')
plt.axvline(passband_frequency_low, color='green', linestyle='--', label='Passband Low')
plt.axvline(passband_frequency_high, color='green', linestyle='--', label='Passband High')
plt.axvline(stopband_frequency_high, color='red', linestyle='--', label='Stopband High')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title(f"Kaiser Bandpass FIR (N={filter_order}, A={minimum_stopband_attenuation} dB)")
plt.grid(True)
plt.legend()
plt.show()

