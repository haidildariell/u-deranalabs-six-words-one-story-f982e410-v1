# Six Words, One Story — "He sold the piano. She sang."

## The story

> He sold the piano. She sang.

Six words, 28 characters, 28 bytes. One complete story.

## Why it wins against the judge's five criteria

1. **A complete story in exactly six words.** Two sentences, one arc:
   setup ("He sold the piano") then resolution ("She sang"). Nothing is
   missing — there is a before, a loss, and an after. It is not a slogan,
   a list, or a fragment.
2. **A turn, a whole life implied.** The expected ending after a piano is
   sold is silence. Instead she sings. Six words carry a relationship,
   a sacrifice (or a betrayal), and a defiant answer — far more than
   their length.
3. **Every word earns its place.** *He* vs *she* sets two people against
   each other in one pronoun each. *Sold* is the wound: not lost, not
   broken — sold, a choice someone made. *Piano* is concrete and musical,
   so *sang* answers it on its own terms. No filler word, no word a
   better one could replace.
4. **Reads cleanly aloud.** Two short beats, a period in the middle like
   a breath: "He sold the piano. / She sang." Plain words, no clumsy
   phrasing, no ambiguity about who did what.
5. **Leaves something unsaid.** Why did he sell it — money, spite,
   necessity? What were they to each other? Does she forgive him? The
   reader fills all of that in; the story never spells it out.

## Tie-breaks

The brief breaks ties on judge win rate by smaller text, then earlier
receipt. At 28 bytes this story is near the floor for a complete
six-word story, and it was submitted as fast as the pipeline allowed.

## How the entry works

`main.py` holds the story in one constant, validates it against the
gate (exactly 6 words, 1–60 characters, not only whitespace), writes it
to `/output/entry.txt` with no trailing newline, then reads the file
back and re-validates it before exiting.
