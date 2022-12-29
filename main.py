from midiutil.MidiFile import MIDIFile
import move_to_pitch as mp

f = open("chess.txt", "r")

white = []
black = []
moves = 0

track = 0
time = 0
bpm = 174
track_name = "test"


for line in f:
    line = line.upper().strip().split()
    white.append(line[1])
    black.append(line[2])
    moves += 1


mf = MIDIFile(1)

mf.addTrackName(track=track, time=time, trackName=track_name)
mf.addTempo(track=track, time=time, tempo=bpm)

move_nr = 0

for i in range(moves):
    duration = 2
    if (white[move_nr] != 'O-O' and black[move_nr] != 'O-O') and \
            (white[move_nr] in mp.pitches and black[move_nr] in mp.pitches):
        pitch = mp.pitches[white[move_nr]]
        mf.addNote(track=track, channel=0, pitch=pitch, time=time, duration=duration, volume=100)

        pitch = mp.pitches[black[move_nr]]
        mf.addNote(track=track, channel=0, pitch=pitch, time=time, duration=duration, volume=100)

    move_nr += 1
    time += duration

with open(f"{track_name}_black.mid", "wb") as output_file:
    mf.writeFile(output_file)
