#!/bin/bash
# Chạy cùng dispatch.sh: bài nào render xong (out/<tên>.mp4) thì dựng luôn trang cho bài đó
# rồi chép sang repo da-di-qua (hsk6/), commit, push — bài nào xong là lên web. Khi đủ mọi bài trong
# todo.txt và không còn bài nào đang render: dựng + push lần cuối rồi ghi build/hsk6-final.done.
# Nhật ký: build/logs/overnight_site.log
# Ai khác cần dựng/sửa site/ thì giữ khóa build/site.lock (mkdir) trong lúc làm, script này chờ.
cd "$(dirname "$0")/.."
REPO=~/Desktop/Project/da-di-qua
LOG=build/logs/overnight_site.log
DONE=build/hsk6-final.done
rm -f "$DONE"
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }

# mục trong todo.txt: số bài HSK 6 (21 → bai21) hoặc tên đầy đủ (ds11 cho 顶石中文), như dispatch.sh
name() { [[ $1 =~ ^[0-9]+$ ]] && echo "bai$1" || echo "$1"; }
# bài đang render đã có out/<tên>.mp4 (ffmpeg ghi dần) nhưng còn khóa build/locks/<mục>: chưa tính là xong
done_lessons() { for n in $(cat tools/todo.txt); do b=$(name $n); [ -f out/$b.mp4 ] && [ ! -f build/locks/$n ] && printf "%s " $b; done; }
missing() { for n in $(cat tools/todo.txt); do [ -f out/$(name $n).mp4 ] || return 0; done; return 1; }
rendering() { ls build/locks 2>/dev/null | grep -q .; }
need_build() { for b in $(done_lessons); do [ -d site/$b/slides ] || return 0; done; return 1; }
# chỉ tính tiến trình Python thật: pgrep -f còn khớp cả lệnh chờ của phiên khác có chứa tên file
running() { ps -axo args= | awk -v pat="$1" '$1 ~ /[Pp]ython3?$/ && index($0, pat)' | grep -q .; }
LOCK=build/site.lock
lock() { until mkdir "$LOCK" 2>/dev/null; do sleep 30; done; }
unlock() { rmdir "$LOCK" 2>/dev/null; }
# build_site.py tự giữ mọi bài đã lên trang (web/published.json), chỉ cần đưa các bài mới
build() {
  while running build_site.py; do sleep 30; done
  log "dựng trang: $(done_lessons)"
  python3 build_site.py $(done_lessons) >> "$LOG" 2>&1 && log "dựng xong" || { log "dựng LỖI"; return 1; }
}
# dựng rồi push, giữ khóa suốt hai bước để không ai đổi site/ giữa chừng
round() { lock; build && push; local r=$?; unlock; return $r; }
push() {
  # video, slide, âm thanh lên Cloudflare Pages (tools/deploy_media.sh), repo chỉ nhận trang và dữ liệu nhẹ
  tools/deploy_media.sh >> "$LOG" 2>&1 || return 1
  rsync -a --delete --exclude='/*/vid/' --exclude='/*/audio/' --exclude='/*/slides/*.jpg' --exclude='/media.json' \
    site/ "$REPO/hsk6/" || return 1
  cd "$REPO" || return 1
  git add hsk6 && git commit -q -m "feat(hsk6): thêm các bài 顶石中文 vừa render xong

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- hsk6 || { cd - >/dev/null; log "không có gì để commit"; return 0; }
  for i in 1 2 3; do
    git push -q origin main && { cd - >/dev/null; log "push xong"; return 0; }
    git fetch -q origin && git rebase -q --autostash origin/main
    sleep 20
  done
  cd - >/dev/null; return 1
}

log "bắt đầu"
while missing || rendering; do
  need_build && round
  sleep 120
done
lock; build; b=$?
[ $b -eq 0 ] && { push; p=$?; } || p=skip
unlock
log "kết thúc: build=$b push=$p"
echo "build=$b push=$p $(date '+%F %T')" > "$DONE"
