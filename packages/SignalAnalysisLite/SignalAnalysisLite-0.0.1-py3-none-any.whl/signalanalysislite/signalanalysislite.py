import numpy as np


class signalAnalysis:
    def modulus_square(complex_number):
        return abs(complex_number) ** 2

    def compute_root_power_spectral_density(data_array, t, dt):
        """Get Root Power Spectral Density - FFT code from FreqDemod
        FFT functions - https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html"""

        # x-axis (Frequency) | units = Hz
        freq = np.fft.fftshift(np.fft.fftfreq(data_array.size, d=dt))

        # y-axis (FFT) | units  = Signal/Hz
        sFT = dt * np.fft.fftshift(np.fft.fft(data_array))

        # RPSD
        # MODULUS SQUARE | units = Signal^2/Hz^2
        for complex_number_index in range(len(sFT)):
            sFT[complex_number_index] = modulus_square(sFT[complex_number_index])

        # (1/t) factor out front | units = Signal^2/Hz
        sFT = 1 / t * sFT

        # square root | units = Signal/(Hz**(1/2))
        sFT = sFT ** (1 / 2)

        # return x, y
        return freq, sFT

    def compute_power_spectral_density(data_array, t, dt):
        """Get Root Spectral Density - FFT code from FreqDemod
        FFT functions - https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html"""

        # x-axis (Frequency) | units = Hz
        freq = np.fft.fftshift(np.fft.fftfreq(data_array.size, d=dt))

        # y-axis (FFT) | units  = Signal/Hz
        sFT = dt * np.fft.fftshift(np.fft.fft(data_array))

        # RPSD
        # MODULUS SQUARE | units = Signal^2/Hz^2
        for complex_number_index in range(len(sFT)):
            sFT[complex_number_index] = modulus_square(sFT[complex_number_index])

        # (1/t) factor out front | units = Signal^2/Hz
        sFT = 1 / t * sFT

        # return x, y
        return freq, sFT

    def avg_spectrum_bartlett(spectrum_type, data_array, dt, M):
        """method of signal averaging to reduce variance and smooth data
        See - https://en.wikipedia.org/wiki/Bartlett%27s_method"""

        data_voxels = []

        voxel = []
        for value_index in range(len(data_array)):
            voxel.append(data_array[value_index])
            if value_index % M == (M - 1):
                data_voxels.append(voxel)
                voxel = []  # reset

        # convert to numpy array (there may be a cleaner way to do this step)
        for voxel_index in range(len(data_voxels)):
            data_voxels[voxel_index] = np.array(data_voxels[voxel_index])

        K = len(data_voxels)  # number of data segments
        # data is now split into K lists, each of length M

        # for each data segment (K), compute spectrum. Then add all spectrum to a list
        sFT_list = []
        freq_list = []
        for voxel in data_voxels:
            if spectrum_type == "PSD":
                freq, sFT = compute_power_spectral_density(voxel, (dt * M), dt)
            if spectrum_type == "RPSD":
                freq, sFT = compute_root_power_spectral_density(voxel, (dt * M), dt)
            sFT_list.append(sFT)
            freq_list.append(freq)

        # convert lists to arrays
        sFT_arrays = np.array(sFT_list)
        freq_arrays = np.array(freq_list)

        # compute the variance column-wise (for each point in spectrum) --> error bars
        sFT_error = np.std(sFT_arrays, axis=0) / (
            K ** (1 / 2)
        )  # divide by root of number of data segments (NOT M)

        # now average the lists over length K
        # average using numpy
        sFT_avg = np.average(sFT_arrays, axis=0)
        freq_avg = np.average(freq_arrays, axis=0)

        # return three arrays (x, y, yerr)
        return freq_avg, sFT_avg, sFT_error
