#!/bin/bash
# Chạy qua đêm trong lúc make_video.py dựng các bài: bài nào render xong (out/<bài>.mp4) thì dựng luôn trang
# cho bài đó (build_site.py ghi thẳng vào hsk6/ của repo), để lúc bài cuối xong chỉ còn một lượt dựng ngắn.
# Khi đủ mọi bài trong tools/todo.txt (mỗi dòng một tên: bai21, ds41…) và không còn make_video.py nào chạy:
# dựng lần cuối, commit hsk6/, push, rồi ghi build/hsk6-final.done. Nhật ký: build/logs/overnight_site.log
cd "$(dirname "$0")/.."
REPO=..
LOG=build/logs/overnight_site.log
DONE=build/hsk6-final.done
mkdir -p build/logs
rm -f "$DONE"
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }

done_lessons() { for n in $(cat tools/todo.txt); do [ -f out/$n.mp4 ] && printf "%s " $n; done; }
missing() { for n in $(cat tools/todo.txt); do [ -f out/$n.mp4 ] || return 0; done; return 1; }
need_build() { for b in $(done_lessons); do [ -d $REPO/hsk6/$b/slides ] || return 0; done; return 1; }
build() {
  while pgrep -f "build_site.py" >/dev/null; do sleep 30; done
  log "dựng trang: $(done_lessons)"
  python3 build_site.py $(done_lessons) >> "$LOG" 2>&1 && log "dựng xong" || { log "dựng LỖI"; return 1; }
}
push() {
  cd "$REPO" || return 1
  git add hsk6 && git commit -q -m "feat(hsk6): thêm các bài vừa render xong qua đêm

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" || { cd - >/dev/null; log "không có gì để commit"; return 0; }
  for i in 1 2 3; do
    git push -q origin main && { cd - >/dev/null; log "push xong"; return 0; }
    git fetch -q origin && git rebase -q --autostash origin/main
    sleep 20
  done
  cd - >/dev/null; return 1
}

log "bắt đầu"
while missing || pgrep -f "make_video.py [bd]" >/dev/null; do
  need_build && build
  sleep 120
done
build; b=$?
push; p=$?
log "kết thúc: build=$b push=$p"
echo "build=$b push=$p $(date '+%F %T')" > "$DONE"
