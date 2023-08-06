#!/usr/bin/env python3
#
# Copyright (C) 2018 William Meng
#
# This file is part of rtl_ultrasound
#
# rtl_ultrasound is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# rtl_ultrasound is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rtl_ultrasound.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import *
from scipy.signal import resample
import time
from datetime import datetime
import argparse
import cv2

global_verbose = False

def process_image(im_in):
    maxRadius = 2500
    im_in = image_repeated[:, :maxRadius] # cut off any data beyond maxRadius
    plt.imshow(im_in, cmap='gray')
    plt.title("Input image")
    plt.show()

    angle_range = np.pi/2 # range of angle swept by transducer (radians)
    theta_scale_factor = image_repeated.shape[0] / angle_range # rows per radian
    print("{} rows per radian".format(theta_scale_factor))
    theta_min = 3/2*np.pi - angle_range/2
    theta_max = 3/2*np.pi + angle_range/2
    print("theta: [{}, {}] radians".format(theta_min, theta_max))

    # pad the image
    pad_below = int(theta_min * theta_scale_factor) # how many rows to pad below theta_min
    pad_above = int((2*np.pi - theta_max) * theta_scale_factor) # how mahy rows to pad above theta_max
    print("Padding {} above and {} below".format(pad_above, pad_below))
    im_below = np.zeros((pad_below, maxRadius))
    im_above = np.zeros((pad_above, maxRadius))

    padded_image = np.vstack((im_above, im_in, im_below))
    plt.imshow(padded_image, cmap='gray')
    plt.title("Vertically Padded image")
    plt.show()

    # scale image
    scaled_image = cv2.resize(padded_image, (2*maxRadius, maxRadius), interpolation=cv2.INTER_CUBIC)
    plt.imshow(scaled_image, cmap='gray')
    plt.title("Scaled image")
    plt.show()

    # transform image
    center = (int(im_out.shape[1]/2), 0) # (x, y) coordinate from top-left of image
    flags = cv2.WARP_INVERSE_MAP
    im_out = cv2.linearPolar(scaled_image, center, maxRadius, flags)
    plt.imshow(im_out, cmap='gray')
    plt.title("Output image")
    plt.show()

def main():
    # Parse command-line arguments
    parser.add_argument('-v', '--verbose', action='store_true', help="enable verbose output")
    args = parser.parse_args()
    global_verbose = args.verbose

    sdr = RtlSdr()

    # configure device
    sdr.set_direct_sampling(2) # directly sample Q channel
    sdr.center_freq = 8e6
    sdr.sample_rate = 2.4e6
    sdr.gain = 'auto'

    center_freq = sdr.center_freq
    sample_rate = sdr.sample_rate
    if global_verbose:
        print("center freq = {} Hz".format(center_freq))
        print("sample rate = {} Hz".format(sample_rate))
        print("gain = {}".format(sdr.gain))

    # read samples
    samples = sdr.read_samples(256*512)
    sdr.close()
    if global_verbose:
        print("Captured {} samples".format(len(samples)))

    # sample data and determine timebase
    upsampling_factor = 10
    resampled = resample(samples, len(samples) * upsampling_factor)
    fs = sample_rate * upsampling_factor
    Ts = 1e6/fs # time per sample after resampling, in microseconds
    if global_verbose:
        print("Resampled at:")
        print("fs = %.2f Msps" % (fs/1e6))
        print("Ts = {} microseconds".format(Ts))

    t = np.array([ x * Ts for x in range(len(resampled))]) # time base, in microseconds
    envelope = np.abs(resampled)
    t_ms = t/1000

    # configure triggering
    max_envelope = np.max(envelope)
    trigger_level = 0.8 * max_envelope
    trigger_holdoff_us = 130 # trigger holdoff time in microseconds
    trigger_holdoff = int(trigger_holdoff_us / Ts) # trigger holdoff in # of samples
    if global_verbose:
        print("max(envelope) = {}".format(max_envelope))
        print("Trigger level = {}".format(trigger_level))
        print("Trigger holdoff = {} microseconds = {} samples".format(trigger_holdoff_us, trigger_holdoff))

    # slice scan lines
    prev_trigger = -trigger_holdoff # allow first trigger to be at 0th sample
    slice_indices = list()
    for i in range(len(envelope)):
        if i >= prev_trigger + trigger_holdoff:
            if envelope[i] > trigger_level:
                slice_indices.append(i)
                prev_trigger = i

    if global_verbose:
        print("Slicing at indices {}".format(slice_indices))
        print("Triggered {} times".format(len(slice_indices)))

    # slice array and vstack
    diffs = np.diff(slice_indices)
    min_diff = np.min(diffs)
    if global_verbose:
        print("Intervals between each trigger are {}".format(diffs))
        print("Choosing the minimum, {}, as the length of each scan line".format(min_diff))

    scan_lines = list()
    for index in slice_indices:
        if len(envelope) < index + min_diff:
            if global_verbose:
                print("Not enough samples left for a complete scan line!")
            continue # TODO: change to break?
        scan_line = envelope[index:index+min_diff]
        scan_lines.append(scan_line)

    if global_verbose:
        print("Created {} scan lines".format(len(scan_lines)))

    image = np.vstack(tuple(scan_lines))


if __name__ == '__main__':
    main()
