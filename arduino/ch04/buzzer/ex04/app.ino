#include <Melody.h>
#include "pitches.h"
#include "pirates.h"

int length = sizeof(notes) / sizeof(int);
Melody melody(2, notes, durations, length);

void setup() {
    melody.play();
}

void loop() {
    melody.run();
}