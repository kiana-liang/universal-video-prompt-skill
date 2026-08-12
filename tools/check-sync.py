#!/usr/bin/env python3
"""
中英同步检查。

中文是真源，英文是译本，方向单向。每份英文文件头部记着它所翻译的那份中文文件
的内容哈希；中文一改，哈希对不上，这里就会把它报出来。

    <!-- sync-source: spec-format.zh-CN.md sha256:a3f9c2e1 -->

**这个脚本不阻断任何东西。** 它只让"英文欠了多少"变得可见。
硬阻断会拖累中文迭代，而一旦有人开始绕过检查，机制就死了——
2026-08-07 那次中英分叉的病根是没人知道它分叉了，不是没被拦住。

用法：
    python3 tools/check-sync.py            # 打印状态表
    python3 tools/check-sync.py --write    # 同时写回 SYNC-STATUS.md
    python3 tools/check-sync.py --stamp spec-format.md
                                           # 翻译完一份后，盖上当前哈希
"""

import argparse
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REFS = ROOT / "references"

# 英文文件 → 它的中文真源。三个隔离区不翻译，故不在表内。
PAIRS = {
    "SKILL.md": "references/workflow.zh-CN.md",
    "references/constitution.md": "references/constitution.zh-CN.md",
    "references/spec-format.md": "references/spec-format.zh-CN.md",
    "references/slot-filling.md": "references/slot-filling.zh-CN.md",
    "references/verifiability.md": "references/verifiability.zh-CN.md",
    "references/portability.md": "references/portability.zh-CN.md",
    "references/film-type-dna.md": "references/film-type-dna.zh-CN.md",
    "references/model-profile-schema.md": "references/model-profile-schema.zh-CN.md",
    "references/execution.md": "references/execution.zh-CN.md",
    "references/checklist.md": "references/checklist.zh-CN.md",
}

STAMP_RE = re.compile(
    r"<!--\s*sync-source:\s*(?P<src>[\w.\-/]+)\s+sha256:(?P<hash>[0-9a-f]{8,64})\s*-->"
)


def digest(path: pathlib.Path) -> str:
    """中文源的内容哈希。取前 12 位，够用且不占地方。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def read_stamp(path: pathlib.Path):
    """英文文件头部的同步戳。只扫前 4000 字节。"""
    if not path.exists():
        return None
    head = path.read_text(encoding="utf-8", errors="replace")[:4000]
    m = STAMP_RE.search(head)
    return m.groupdict() if m else None


def check():
    rows = []
    for en_rel, zh_rel in PAIRS.items():
        en, zh = ROOT / en_rel, ROOT / zh_rel

        if not zh.exists():
            rows.append((en_rel, zh_rel, "❌", "中文真源不存在"))
            continue

        want = digest(zh)

        if not en.exists():
            rows.append((en_rel, zh_rel, "⬜", "英文还没写"))
            continue

        stamp = read_stamp(en)
        if stamp is None:
            rows.append((en_rel, zh_rel, "❓", "英文没有同步戳，无法判断"))
        elif stamp["src"] != pathlib.PurePath(zh_rel).name:
            rows.append((en_rel, zh_rel, "❌", f"同步戳指向别的源：{stamp['src']}"))
        elif stamp["hash"] != want:
            rows.append((en_rel, zh_rel, "⚠️", f"中文已改，英文未跟（戳 {stamp['hash']} / 现 {want}）"))
        else:
            rows.append((en_rel, zh_rel, "✅", "同步"))
    return rows


def render(rows) -> str:
    out = [
        "# 中英同步状态",
        "",
        "> 本文件由 `tools/check-sync.py` 生成，不要手改。",
        "> 中文是真源，英文是译本。⚠️ 表示中文改过而英文还没跟上——**这是待办，不是错误**。",
        "",
        "| 英文 | 中文真源 | 状态 | 说明 |",
        "|---|---|---|---|",
    ]
    for en, zh, mark, note in rows:
        out.append(f"| `{en}` | `{zh}` | {mark} | {note} |")

    stale = [r for r in rows if r[2] in ("⚠️", "⬜", "❓", "❌")]
    out += [
        "",
        f"**{len(rows) - len(stale)} / {len(rows)} 同步。**",
        "",
        "三个隔离区（`case-library` / `film-types` / `observations`）**不翻译**，故不在表内——",
        "它们装的是具体术语措辞，翻译会造出第二套皮：同一个术语两种译法，下一个人不知道该抄哪个。",
    ]
    return "\n".join(out) + "\n"


def stamp(target: str):
    """翻译完一份之后调用，把当前中文哈希盖到英文文件头部。"""
    if target not in PAIRS:
        sys.exit(f"不认识的目标：{target}\n可选：{', '.join(PAIRS)}")

    en, zh = ROOT / target, ROOT / PAIRS[target]
    if not en.exists():
        sys.exit(f"英文文件还不存在：{target}")

    line = f"<!-- sync-source: {pathlib.PurePath(PAIRS[target]).name} sha256:{digest(zh)} -->"
    text = en.read_text(encoding="utf-8")

    if STAMP_RE.search(text[:4000]):
        text = STAMP_RE.sub(line, text, count=1)
    elif text.startswith("---"):
        # 有 frontmatter 的（SKILL.md），戳放在 frontmatter 之后
        end = text.index("\n---", 3) + len("\n---\n")
        text = text[:end] + line + "\n" + text[end:]
    else:
        text = line + "\n\n" + text

    en.write_text(text, encoding="utf-8")
    print(f"✅ 已盖戳：{target} ← {PAIRS[target]} @ {digest(zh)}")


def main():
    ap = argparse.ArgumentParser(description="中英同步检查（只报告，不阻断）")
    ap.add_argument("--write", action="store_true", help="把状态表写进 SYNC-STATUS.md")
    ap.add_argument("--stamp", metavar="英文文件", help="翻译完一份后盖上当前哈希")
    args = ap.parse_args()

    if args.stamp:
        stamp(args.stamp)
        return

    rows = check()
    report = render(rows)
    print(report)

    if args.write:
        (ROOT / "SYNC-STATUS.md").write_text(report, encoding="utf-8")
        print("→ 已写入 SYNC-STATUS.md")

    # 永远返回 0：这个脚本报告状态，不裁决对错。
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
