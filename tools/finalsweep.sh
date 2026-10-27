cd /tmp/claude-0/-home-claude/47fd48c3-e8a0-599b-9f2d-c17d40f53247/scratchpad/w
while pgrep -f "cxe.py" >/dev/null; do sleep 20; done
for q in "" potato ultra; do echo "== labs QL=${q:-auto}"; QL=$q timeout 1200 python3 cxth.py 2>&1 | tail -12; done
for q in "" potato ultra; do echo "== calc QL=${q:-auto}"; QL=$q VW=700 VH=700 timeout 3000 python3 cxe.py "$(cat scn.txt)" > p1/calc20_$q.txt 2>&1; echo "ok $(grep -c 'errors: 0' p1/calc20_$q.txt) / $(grep -c 'errors:' p1/calc20_$q.txt)"; grep "errors:" p1/calc20_$q.txt | grep -v "errors: 0" | head; done
echo FINISHED
