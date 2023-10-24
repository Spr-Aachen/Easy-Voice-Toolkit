import numpy as np


# This function is obtained from librosa.
def get_rms(
    y,
    *,
    frame_length=2048,
    hop_length=512,
    pad_mode="constant",
):
    padding = (int(frame_length // 2), int(frame_length // 2))
    y = np.pad(y, padding, mode=pad_mode)

    axis = -1
    # put our new within-frame axis at the end for now
    out_strides = y.strides + tuple([y.strides[axis]])
    # Reduce the shape on the framing axis
    x_shape_trimmed = list(y.shape)
    x_shape_trimmed[axis] -= frame_length - 1
    out_shape = tuple(x_shape_trimmed) + tuple([frame_length])
    xw = np.lib.stride_tricks.as_strided(
        y, shape=out_shape, strides=out_strides
    )
    if axis < 0:
        target_axis = axis - 1
    else:
        target_axis = axis + 1
    xw = np.moveaxis(xw, -1, target_axis)
    # Downsample along the target axis
    slices = [slice(None)] * xw.ndim
    slices[axis] = slice(0, None, hop_length)
    x = xw[tuple(slices)]

    # Calculate power
    power = np.mean(np.abs(x) ** 2, axis=-2, keepdims=True)

    return np.sqrt(power)


class Slicer:
    '''
    sr
        Sampling rate of the input audio.
    db_threshold
        The RMS Threshold presented in dB. Areas where all RMS values are below this Threshold will be regarded as silence. Increase this value if your audio is noisy. Defaults to -40.
    Audio_Length_Min
        The minimum length required for each sliced audio clip, presented in milliseconds. Defaults to 5000.
    Silent_Interval_Min
        The minimum length for a silence part to be sliced, presented in milliseconds. Set this value smaller if your audio contains only short breaks. The smaller this value is, the more sliced audio clips this script is likely to generate. Note that this value must be smaller than Audio_Length_Min and larger than Hop_Size. Defaults to 300.
    Hop_Size
        Length of each RMS frame, presented in milliseconds. Increasing this value will increase the precision of slicing, but will slow down the process. Defaults to 10.
    max_silence_kept
        The maximum silence length kept around the sliced audio, presented in milliseconds. Adjust this value according to your needs. Note that setting this value does not mean that silence parts in the sliced audio have exactly the given length. The algorithm will search for the best position to slice, as described above. Defaults to 1000.
    '''
    def __init__(self,
        Sampling_Rate: int,
        RMS_Threshold: float = -40.,
        Audio_Length_Min: int = 5000,
        Silent_Interval_Min: int = 300,
        Hop_Size: int = 10,
        Silence_Kept_Max: int = 1000
    ):
        if not Audio_Length_Min >= Silent_Interval_Min >= Hop_Size:
            raise ValueError('The following condition must be satisfied: Audio_Length_Min >= Silent_Interval_Min >= Hop_Size')
        if not Silence_Kept_Max >= Hop_Size:
            raise ValueError('The following condition must be satisfied: Silence_Kept_Max >= Hop_Size')
        Silent_Interval_Min = Sampling_Rate * Silent_Interval_Min / 1000
        self.RMS_Threshold = 10 ** (RMS_Threshold / 20.)
        self.Hop_Size = round(Sampling_Rate * Hop_Size / 1000)
        self.win_size = min(round(Silent_Interval_Min), 4 * self.Hop_Size)
        self.Audio_Length_Min = round(Sampling_Rate * Audio_Length_Min / 1000 / self.Hop_Size)
        self.Silent_Interval_Min = round(Silent_Interval_Min / self.Hop_Size)
        self.Silence_Kept_Max = round(Sampling_Rate * Silence_Kept_Max / 1000 / self.Hop_Size)

    def _apply_slice(self, waveform, begin, end):
        if len(waveform.shape) > 1:
            return waveform[:, begin * self.Hop_Size: min(waveform.shape[1], end * self.Hop_Size)]
        else:
            return waveform[begin * self.Hop_Size: min(waveform.shape[0], end * self.Hop_Size)]

    # @timeit
    def slice(self, waveform):
        if len(waveform.shape) > 1:
            samples = waveform.mean(axis=0)
        else:
            samples = waveform
        if samples.shape[0] <= self.Audio_Length_Min:
            return [waveform]
        rms_list = get_rms(y=samples, frame_length=self.win_size, hop_length=self.Hop_Size).squeeze(0)
        sil_tags = []
        silence_start = None
        clip_start = 0
        for i, rms in enumerate(rms_list):
            # Keep looping while frame is silent.
            if rms < self.RMS_Threshold:
                # Record start of silent frames.
                if silence_start is None:
                    silence_start = i
                continue
            # Keep looping while frame is not silent and silence start has not been recorded.
            if silence_start is None:
                continue
            # Clear recorded silence start if interval is not enough or clip is too short
            is_leading_silence = silence_start == 0 and i > self.Silence_Kept_Max
            need_slice_middle = i - silence_start >= self.Silent_Interval_Min and i - clip_start >= self.Audio_Length_Min
            if not is_leading_silence and not need_slice_middle:
                silence_start = None
                continue
            # Need slicing. Record the range of silent frames to be removed.
            if i - silence_start <= self.Silence_Kept_Max:
                pos = rms_list[silence_start: i + 1].argmin() + silence_start
                if silence_start == 0:
                    sil_tags.append((0, pos))
                else:
                    sil_tags.append((pos, pos))
                clip_start = pos
            elif i - silence_start <= self.Silence_Kept_Max * 2:
                pos = rms_list[i - self.Silence_Kept_Max: silence_start + self.Silence_Kept_Max + 1].argmin()
                pos += i - self.Silence_Kept_Max
                pos_l = rms_list[silence_start: silence_start + self.Silence_Kept_Max + 1].argmin() + silence_start
                pos_r = rms_list[i - self.Silence_Kept_Max: i + 1].argmin() + i - self.Silence_Kept_Max
                if silence_start == 0:
                    sil_tags.append((0, pos_r))
                    clip_start = pos_r
                else:
                    sil_tags.append((min(pos_l, pos), max(pos_r, pos)))
                    clip_start = max(pos_r, pos)
            else:
                pos_l = rms_list[silence_start: silence_start + self.Silence_Kept_Max + 1].argmin() + silence_start
                pos_r = rms_list[i - self.Silence_Kept_Max: i + 1].argmin() + i - self.Silence_Kept_Max
                if silence_start == 0:
                    sil_tags.append((0, pos_r))
                else:
                    sil_tags.append((pos_l, pos_r))
                clip_start = pos_r
            silence_start = None
        # Deal with trailing silence.
        total_frames = rms_list.shape[0]
        if silence_start is not None and total_frames - silence_start >= self.Silent_Interval_Min:
            silence_end = min(total_frames, silence_start + self.Silence_Kept_Max)
            pos = rms_list[silence_start: silence_end + 1].argmin() + silence_start
            sil_tags.append((pos, total_frames + 1))
        # Apply and return slices.
        if len(sil_tags) == 0:
            IsSlicingNeeded = False
            return [waveform], IsSlicingNeeded
        else:
            IsSlicingNeeded = True
            chunks = []
            if sil_tags[0][0] > 0:
                chunks.append(self._apply_slice(waveform, 0, sil_tags[0][0]))
            for i in range(len(sil_tags) - 1):
                chunks.append(self._apply_slice(waveform, sil_tags[i][1], sil_tags[i + 1][0]))
            if sil_tags[-1][1] < total_frames:
                chunks.append(self._apply_slice(waveform, sil_tags[-1][1], total_frames))
            return chunks, IsSlicingNeeded
