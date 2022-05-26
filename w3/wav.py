#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from random import sample
from wave import open
from struct import Struct
from math import floor

frame_rate = 11025


def encode(x):
    """
    Encode float x between -1 and 1 as two bytes

    This module performs conversions between Python values and C structs represented as Python bytes objects. This can be used in handling binary data stored in files or from network connections, among other sources. It uses Format Strings as compact descriptions of the layout of the C structs and the intended conversion to/from Python values.

    Return a bytes object containing the values v1, v2, packed according to the format string format. The arguments must match the values required by the format exactly.

    """
    i = int(16384 * x)
    return Struct('h').pack(i)


def play(sampler, name='song.wav', seconds=2):
    """
    Write the output of a sampler function as a wav file.

    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)

    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()


def tri(frequency, amplitude=0.3):
    """
    A continuous triangle wave
    amplitude 振幅
    floor 向下取整
    frequency -- pitch//音调
    amplitude -- volume//音量
    """
    period = frame_rate // frequency

    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler


c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

def both(f, g):
    return lambda t: f(t) + g(t)

# play(both(tri(c_freq), tri(e_freq)))

def note(f, start, end, fade=0.001):
    """start - end in second"""
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler


def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    z += 1/2
    return song

def mario_at(octave):
    """octave 八度
    """
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq), tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)
play(both(both(mario_at(1.5), mario_at(1)), mario_at(0.5)))
