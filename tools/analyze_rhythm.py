#!/usr/bin/env python3
"""节奏客观测量 —— 画面切点 + 音轨鼓点，无第三方依赖。

用法: python3 analyze_rhythm.py a.mp4 b.mp4 ...

它存在的理由：「要更高动态」这类要求本身不可验证，改完也说不清有没有变好。
这个脚本把那句话翻译成能测的信号——跟写提示词时把「紧张」翻译成
可观察线索是同一个动作，只是发生在跑完之后。

⚠️ 两条使用限制，比任何一个指标都重要：

  1. 只在受控对照里可比 —— 同一条片子、同参数、只改一个变量。
     跨片子的绝对值没有意义：画面对比度、题材本身的运动量、镜头运动方式、
     分辨率与帧率都会改变基线。实测见过一条低对比绘本画风的片子四版全在
     0.10–0.16，而一条高对比限色 MG 在 0.688–0.825 —— 那是两把不同刻度的尺子。
     正确用法：改之前测一次，改完再测一次，看你想改的那个指标动了没有。

  2. 它测的是画面变化量，不是"动态感" —— 给不了运动质量（流畅／卡顿／形变），
     也分不清高数值是"动得好"还是"画面在闪"。它给的是信号，不是判决；
     动态、节奏、整体调性最终要靠人看回放。

指标说明：
  YUV 突变     —— 帧间 (Y,U,V) 欧氏距离 >12。必须带色度，否则抓不到"亮度相近的整屏换色"
  0.5s 网格对齐 —— 120BPM 的判据：突变点是否落在 0.5 秒整数倍附近（±2 帧）
  间隔规律性   —— 相邻突变间隔的标准差，越小越像节拍
  定格占比     —— 连续 ≥0.5s 帧间差 <0.6 的总时长
  帧间差中位数 —— 画面基线运动量，越大说明"一直在动"
  音轨鼓点     —— 10ms RMS 包络的峰值间隔 → 反推实际 BPM
"""
import math
import statistics
import subprocess
import sys


def frame_yuv(path):
    out = subprocess.run(
        ['ffmpeg', '-v', 'error', '-i', path, '-vf',
         'scale=64:36,signalstats,metadata=print:file=-', '-f', 'null', '-'],
        capture_output=True, text=True).stdout
    frames, cur = {}, None
    for line in out.splitlines():
        line = line.strip()
        if line.startswith('frame:'):
            cur = int(line.split()[0].split(':')[1])
            frames[cur] = {}
        elif '=' in line and 'signalstats' in line and cur is not None:
            k, v = line.split('=')
            frames[cur][k.split('.')[-1]] = float(v)
    return [(frames[i].get('YAVG', 0), frames[i].get('UAVG', 0), frames[i].get('VAVG', 0))
            for i in sorted(frames)]


def audio_env(path, ms=10):
    """10ms RMS 包络。asetnsamples 按 48k 估算，实际采样率不影响相对间隔。"""
    n = int(48000 * ms / 1000)
    out = subprocess.run(
        ['ffmpeg', '-v', 'error', '-i', path, '-af',
         f'asetnsamples={n}:p=0,astats=metadata=1:reset=1,'
         'ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-',
         '-f', 'null', '-'], capture_output=True, text=True).stdout
    vals = []
    for line in out.splitlines():
        if 'RMS_level' in line:
            try:
                vals.append(float(line.split('=')[1]))
            except ValueError:
                pass
    return vals


def peaks(env, ms=10):
    """局部极大且显著高于邻域均值的点 → 鼓点候选。"""
    if not env:
        return []
    out = []
    W = 8
    for i in range(W, len(env) - W):
        loc = env[i - W:i + W + 1]
        if env[i] == max(loc) and env[i] - (sum(loc) / len(loc)) > 3.0:
            if not out or (i - out[-1]) > 6:   # 最小间隔 60ms，去重
                out.append(i)
    return [round(i * ms / 1000.0, 3) for i in out]


def report(path):
    seq = frame_yuv(path)
    if not seq:
        print(f'{path}: 读不到帧'); return
    fps = 24.0
    d = [math.dist(seq[i], seq[i + 1]) for i in range(len(seq) - 1)]
    jumps = [i / fps for i in range(len(d)) if d[i] > 12]

    # BPM 网格对齐：同时测多个候选 BPM，看哪个网格最贴
    tol = 2 / fps
    grids = {}
    for bpm in (120, 132, 240, 264):
        beat = 60.0 / bpm
        hit = [t for t in jumps if abs(t - round(t / beat) * beat) <= tol]
        grids[bpm] = len(hit)
    aligned = []

    gaps = [round(jumps[i + 1] - jumps[i], 3) for i in range(len(jumps) - 1)]
    gaps_wide = [g for g in gaps if g > 0.1]      # 忽略同一事件内的连续帧

    runs, s = [], None
    for i, v in enumerate(d):
        if v < 0.6:
            if s is None: s = i
        else:
            if s is not None and i - s >= 12: runs.append((i - s) / fps)
            s = None
    if s is not None and len(d) - s >= 12: runs.append((len(d) - s) / fps)

    dur = len(seq) / fps
    pk = peaks(audio_env(path))
    apg = [round(pk[i + 1] - pk[i], 3) for i in range(len(pk) - 1)]
    apg_med = statistics.median(apg) if apg else 0

    print(f'\n===== {path} ({dur:.1f}s) =====')
    print(f'画面 YUV 突变      {len(jumps)} 处')
    n = len(jumps) or 1
    print('  BPM 网格对齐     ' + '  '.join(
        f'{b}:{c}/{len(jumps)}({100*c/n:.0f}%)' for b, c in grids.items()))
    if gaps_wide:
        print(f'  间隔中位数 {statistics.median(gaps_wide):.3f}s'
              f'  标准差 {statistics.pstdev(gaps_wide):.3f}  ← 越小越像节拍')
    print(f'定格               {len(runs)} 段 共 {sum(runs):.2f}s = {100*sum(runs)/dur:.0f}%')
    print(f'帧间差中位数       {statistics.median(d):.3f}  ← 基线运动量')
    print(f'音轨鼓点           {len(pk)} 个'
          + (f'  间隔中位数 {apg_med:.3f}s → 约 {60/apg_med:.0f} BPM' if apg_med else ''))
    if jumps:
        print(f'  突变时间点: {[round(t,2) for t in jumps]}')


if __name__ == '__main__':
    for p in sys.argv[1:]:
        report(p)
