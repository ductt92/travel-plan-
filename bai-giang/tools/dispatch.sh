#!/bin/bash
# Render lần lượt các bài trong tools/todo.txt (MAX bài cùng lúc). Mục là số bài HSK 6 (21 → bai21)
# hoặc tên đầy đủ (ds11 cho 顶石中文). Bỏ qua bài đã có out/<tên>.mp4 hoặc đang có khóa build/locks/<mục>;
# bài chưa có <tên>.json (kịch bản chưa xong) thì chờ. Nhật ký: build/logs/dispatch.log
cd "$(dirname "$0")/.."
MAX=1
mkdir -p build/locks build/logs
name() { [[ $1 =~ ^[0-9]+$ ]] && echo "bai$1" || echo "$1"; }
running() { ls build/locks | wc -l | tr -d ' '; }
while true; do
  next=""; waiting=0
  for n in $(cat tools/todo.txt); do
    b=$(name $n)
    [ -f out/$b.mp4 ] && continue
    [ -e build/locks/$n ] && continue
    [ -f $b.json ] || { waiting=1; continue; }
    next=$n; break
  done
  if [ -z "$next" ]; then
    [ "$(running)" = 0 ] && [ $waiting = 0 ] && exit 0
    sleep 60; continue
  fi
  if [ "$(running)" -ge $MAX ]; then sleep 30; continue; fi
  b=$(name $next)
  touch build/locks/$next
  ( python3 make_video.py $b.json > build/logs/render$next.log 2>&1
    rc=$?; echo "$(date '+%F %T') $b exit $rc" >> build/logs/dispatch.log
    # render lỗi: bỏ file mp4 dở, chờ một lúc rồi thử lại (lỗi thoáng qua của "say", đầy ổ…)
    [ $rc -ne 0 ] && { rm -f out/$b.mp4; sleep 120; }
    rm -f build/locks/$next ) &
  sleep 5
done
