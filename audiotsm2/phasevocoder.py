'''audiotsm2/phasevocoder.py'''

import numpy as np

from windows import hanning
from analysis_synthesis import AnalysisSynthesisTSM

def find_peaks(amplitude):
    """
    A value is considered to be a peak if it is higher than its four closest
    neighbours.
    """

    # Pad the array with -1 at the beginning and the end to avoid overflows.
    padded = np.concatenate((-np.ones(2), amplitude, -np.ones(2)))

    # Shift the array by one/two values to the left/right
    shifted_l2 = padded[:-4]
    shifted_l1 = padded[1:-3]
    shifted_r1 = padded[3:-1]
    shifted_r2 = padded[4:]

    # Compare the original array with the shifted versions.
    peaks = ((amplitude >= shifted_l2) & (amplitude >= shifted_l1) &
             (amplitude >= shifted_r1) & (amplitude >= shifted_r2))

    return peaks


def get_closest_peaks(peaks):
    """
    Returns an array containing the index of the closest peak of each index.
    """
    closest_peak = np.empty_like(peaks, dtype=int)
    previous = -1
    for i, is_peak in enumerate(peaks):
        if(is_peak):
            if(previous >= 0):
                closest_peak[previous:(previous + i) // 2 + 1] = previous
                closest_peak[(previous + i) // 2 + 1:i] = i
            else:
                closest_peak[:i] = i
            previous = i
    closest_peak[previous:] = previous

    return closest_peak


class PhaseVocoderConverter():
    """
    A Converter implementing the phase vocoder time-scale modification procedure.
    """

    def __init__(self, channels, frame_length, analysis_hop, synthesis_hop, peak_finder):
        self._channels = channels
        self._frame_length = frame_length
        self._synthesis_hop = synthesis_hop
        self._analysis_hop = analysis_hop
        self._find_peaks = peak_finder

        # Centers of the FFT frequency bins
        self._center_frequency = np.fft.rfftfreq(frame_length) * 2 * np.pi
        fft_length = len(self._center_frequency)

        self._first = True

        self._previous_phase = np.empty((channels, fft_length))
        self._output_phase = np.empty((channels, fft_length))

        # Buffer used to compute the phase increment and the instantaneous frequency
        self._buffer = np.empty(fft_length)

    def clear(self):
        self._first = True

    def convert_frame(self, frame):
        for k in range(0, self._channels):
            # Compute the FFT of the analysis frame
            stft = np.fft.rfft(frame[k])
            amplitude = np.abs(stft)
            phase = np.angle(stft)
            del stft

            peaks = self._find_peaks(amplitude)
            closest_peak = get_closest_peaks(peaks)

            if(self._first):
                # Leave the first frame unchanged
                self._output_phase[k, :] = phase
            else:
                # Compute the phase increment
                self._buffer[peaks] = (
                    phase[peaks] - self._previous_phase[k, peaks] -
                    self._analysis_hop * self._center_frequency[peaks]
                )

                # Unwrap the phase increment
                self._buffer[peaks] += np.pi
                self._buffer[peaks] %= 2 * np.pi
                self._buffer[peaks] -= np.pi

                # Compute the instantaneous frequency (in the same buffer,
                # since the phase increment wont be required after that)
                self._buffer[peaks] /= self._analysis_hop
                self._buffer[peaks] += self._center_frequency[peaks]

                self._buffer[peaks] *= self._synthesis_hop
                self._output_phase[k][peaks] += self._buffer[peaks]

                # Phase locking
                self._output_phase[k] = (
                    self._output_phase[k][closest_peak] +
                    phase - phase[closest_peak]
                )

                # Compute the new stft
                output_stft = amplitude * np.exp(1j * self._output_phase[k])

                frame[k, :] = np.fft.irfft(output_stft).real

            # Save the phase for the next analysis frame
            self._previous_phase[k, :] = phase
            del phase
            del amplitude

        self._first = False

        return frame

    def set_analysis_hop(self, analysis_hop):
        self._analysis_hop = analysis_hop


def phasevocoder(inFile, outFile, speed=1.):

    FRAME_LENGTH = 2048
    analysis_hop = None
    synthesis_hop = None

    if(synthesis_hop is None):
        synthesis_hop = FRAME_LENGTH // 4

    if(analysis_hop is None):
        analysis_hop = int(synthesis_hop * speed)

    analysis_window = hanning(FRAME_LENGTH)
    synthesis_window = hanning(FRAME_LENGTH)

    from wav import WavReader, WavWriter

    with WavReader(inFile) as reader:
        with WavWriter(outFile, reader.channels, reader.samplerate) as writer:

            converter = PhaseVocoderConverter(reader.channels, FRAME_LENGTH, analysis_hop,
                synthesis_hop, find_peaks)

            AnalysisSynthesisTSM(converter, reader.channels, FRAME_LENGTH, analysis_hop,
                synthesis_hop, analysis_window, synthesis_window).run(reader, writer)
