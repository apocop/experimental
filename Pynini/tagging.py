#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pynini

input_strings = [
        'Mellophone - King 1121SP, .687 Bore, Key of F, 3 Valves, 10 1/2" Bell, Silver Plate Finish, No Sub',
        'Mellophone King 1121SP',
        'Mellophone Silver plate King 1121SP Silver',
        'Mellophone King Marching Mellophone Outfit King 1121SP Silver, lacquer',
        'Marching Baritone King 1127SP',
        'Baritone Marching Baritone King 1127 silver',
        'King 1127SP Silver Marching Baritone with large bore receiver',
        'Baritone Marching Baritone MBH1129SP',
        'Conn 112H Double Rotor Bass Trombone',
        'King 1135W King Tubas with Rolling Case',
        'Tuba 3/4 3-Valve 3/4 BBb Tuba Standard King King 1135W',
        'Piccolo Pearl PFP-105E',
        'Conn-Selmer King Student Model 1140W 3 Valve Tuba',
        'Tuba Marching Ultimate Series BBb King 1151SP silver',
        'Oboe Intermediate Standard Selmer 120B',
        'Selmer USA Genadilla Wood Oboe - 122F',
        'Oboe, Intermediate For Advancing Student, with Case Selmer 123FB',
        'Bb Clarinet Selmer 1400B',
        'Bass Clarinet Selmer 1430LP',
        'Selmer 1430LP Bass Clarinet',
        'Bass Clarinet Selmer 1430LP with low EB Dense Resin body Dense resin body; and silver keys with low Eb; adjustrable peg; with wooden case and mpc',
        'Bass Clarinet w/case, Selmer, 1430LP',
        'Bass Clarinet Selmer/1430LP',
        'Yamaha ¾ Tuba Model YBB-105',
        'Yamaha YBB-105WC ¾ Size Tuba',
        'Yamaha YBB-105WC Standard 3/4 size Tuba;']


brands = ("Yamaha", "Selmer", "King", "Conn-Selmer", "Pearl")


fst_target = pynini.string_map(brands)
left_tag = pynini.transducer("", "<brand>")
right_tag = pynini.transducer("", r"</brand>")
substitution = left_tag + fst_target + right_tag
chars = [chr(i) for i in range(1, 91)] + [r"\[", r"\\", r"\]"] + [chr(i) for i in range(94, 256)]
sigma_star = pynini.union(*chars).closure()

rewrite = pynini.cdrewrite(substitution, "", "", sigma_star)


# Instrument rewrite.
instruments = ("flute", "trumpet", "Mellophone", "Marching Mellophone",
               "Marching Baritone", "Baritone", "Bass Clarinet", "Tuba",
               "Bb Clarinet"
               )
fst_inst_target = pynini.string_map(instruments)
inst_left_tag = pynini.transducer('', '<instrument>')
inst_right_tag = pynini.transducer('', r'</instrument>')
inst_substitution = inst_left_tag + fst_inst_target + inst_right_tag
inst_rewrite = pynini.cdrewrite(inst_substitution, "", "", sigma_star)




for string in input_strings:
    output = pynini.compose(string, rewrite).stringify()
    output = pynini.compose(output, inst_rewrite).stringify()
    print(output)