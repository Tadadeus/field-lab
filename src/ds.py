import re

TOKENS = """:root{color-scheme:dark;--bg:#121519;--panel:#171b20;--panel2:#1c2127;--ctl:#21272e;--elev:#262d35;--well:#0d1013;--bg2:var(--ctl);--line:#2a2f35;--line2:#3a414a;--track:#707984;--fg:#dfe3e8;--dim:#a8b1bb;--faint:#8d97a2;--acc:#7fb6c9;--hl:var(--acc);--on-acc:#0d1013;--hov:rgba(255,255,255,.04);--sel:color-mix(in srgb,var(--acc) 14%,transparent);--selb:color-mix(in srgb,var(--acc) 50%,var(--line2));--ok:#5fc98a;--bad:#ef7a6a;--warn:#e3b45a;--rec:#ef6a6a;--star:#e9c46a;--Z1:#2fd8f2;--Z2:#ff6b2c;--mix:#e257d3;--vio:#b49cff;--sig:#f3f5f9;--dk-bg:#0d1013;--dk-panel:#171b20;--dk-panel2:#1c2127;--dk-line:#2a2f35;--dk-line2:#3a414a;--dk-fg:#dfe3e8;--dk-dim:#a8b1bb;--dk-faint:#8d97a2;--dk-ax-x:#ff6b6b;--dk-ax-y:#7dff8a;--dk-ax-z:#6bb8ff;--dk-ax-w:#c9a6ff;--dk-pos:#ff6a5c;--dk-neg:#62a6ff;--dk-glass:rgba(13,16,19,.72);--ink-shadow:rgba(0,0,0,.85);--on-fill:#0d1013;--sh-1:0 4px 14px rgba(0,0,0,.32);--sh-2:0 8px 24px rgba(0,0,0,.4);--scrim:rgba(6,8,10,.62);--spot:rgba(6,8,10,.66);--glass-line:rgba(255,255,255,.35);--ui:"IBM Plex Sans Condensed","IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--prose:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"JetBrains Mono","SF Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--math:"STIX Two Text","Cambria Math","Times New Roman",serif;--t-1:11px;--t-2:12px;--t-3:13px;--t-4:16px;--t-5:19px;--t-6:24px;--lh-tight:1.25;--lh-prose:1.5;--s-h:2px;--s-1:4px;--s-2:8px;--s-3:12px;--s-4:16px;--s-6:24px;--s-8:32px;--s-12:48px;--r-1:2px;--r-2:4px;--r-3:8px;--r:var(--r-2);--hdr:28px;--lbw:40%;--ease-out:cubic-bezier(.23,1,.32,1);--ease-in-out:cubic-bezier(.77,0,.175,1);--ease:var(--ease-out);--eio:var(--ease-in-out);--d-1:120ms;--d-2:160ms;--d-3:200ms;--d-4:250ms;--z-1:1;--z-2:2;--z-3:3;--z-sticky:10;--z-float:20;--z-modal:30;--z-top:40}
:root[data-theme=light]{color-scheme:light;--bg:#e8ebee;--panel:#f6f7f9;--panel2:#eef1f4;--ctl:#ffffff;--elev:#ffffff;--well:#ffffff;--line:#d7dce1;--line2:#b4bcc5;--track:#78818b;--fg:#161b21;--dim:#46505b;--faint:#5b6570;--acc:#1d6a82;--on-acc:#ffffff;--hov:rgba(0,0,0,.04);--ok:#16733d;--bad:#b2342a;--warn:#8a5f00;--rec:#b2342a;--star:#8a6200;--Z1:#08718a;--Z2:#b8410f;--mix:#ad2f98;--vio:#6a4fd0;--sig:#1b2230;--sh-1:0 4px 14px rgba(20,25,34,.12);--sh-2:0 8px 24px rgba(20,25,34,.16);--scrim:rgba(20,25,34,.35);--spot:rgba(20,25,34,.45)}
"""

TOKEN_SELS = {":root", ":root[data-theme=light]", "[data-theme=light]", "body", ":root[data-theme=light] body"}
LAB_RE = re.compile(r"^(:root\[data-theme=light\] )?body\.(ca|al-[\w-]+)$")
DARK_REMAP = {"--bg": "var(--dk-bg)", "--bg2": "var(--dk-panel2)", "--panel": "var(--dk-panel)", "--panel2": "var(--dk-panel2)", "--line": "var(--dk-line)", "--line2": "var(--dk-line2)", "--fg": "var(--dk-fg)", "--dim": "var(--dk-dim)", "--faint": "var(--dk-faint)", "--well": "var(--dk-bg)", "--ctl": "var(--dk-panel2)", "--elev": "var(--dk-panel2)"}

HEX = {"#04060a": "var(--dk-bg)", "#070a10": "var(--dk-bg)", "#0a0d11": "var(--dk-bg)", "#0b0e14": "var(--dk-bg)", "#0b0f16": "var(--dk-bg)", "#080b11": "var(--dk-panel)", "#0e1219": "var(--dk-panel2)", "#0d121b": "var(--elev)", "#101420": "var(--ctl)", "#121826": "var(--ctl)", "#0a0d10": "var(--on-fill)", "#05070b": "var(--on-fill)", "#e8ecf2": "var(--dk-fg)", "#f3f5f9": "var(--dk-fg)", "#cfd5df": "var(--dk-fg)", "#9ea7b6": "var(--dk-dim)", "#9aa3b2": "var(--dk-dim)", "#6a7487": "var(--dk-faint)", "#3a4353": "var(--dk-line2)", "#202734": "var(--dk-line)", "#000": "var(--ink-shadow)", "#fff": "var(--dk-fg)", "#ffffff": "var(--ctl)", "#ff6b6b": "var(--rec)", "#ff4d4d": "var(--rec)", "#9ff0c4": "var(--ok)", "#ffd166": "var(--star)", "#b07a00": "var(--star)", "#3fbf6e": "var(--ok)", "#5fd38d": "var(--ok)", "#1d8a4a": "var(--ok)", "#e5604f": "var(--bad)", "#ff7a6b": "var(--bad)", "#c43a2a": "var(--bad)", "#e2e7ee": "var(--panel2)", "#c9f6fd": "color-mix(in srgb,var(--Z1) 30%,var(--fg))", "#ffdccb": "color-mix(in srgb,var(--Z2) 30%,var(--fg))", "#fbd5f6": "color-mix(in srgb,var(--mix) 30%,var(--fg))", "#e6dcff": "color-mix(in srgb,var(--vio) 30%,var(--fg))", "#06566a": "color-mix(in srgb,var(--Z1) 60%,var(--fg))", "#8a3209": "color-mix(in srgb,var(--Z2) 60%,var(--fg))", "#7a1d6b": "color-mix(in srgb,var(--mix) 60%,var(--fg))", "#432f96": "color-mix(in srgb,var(--vio) 60%,var(--fg))"}

RGBA = {"rgba(0,0,0,.35)": "SH", "rgba(0,0,0,.5)": "SH", "rgba(0,0,0,.45)": "SH", "rgba(0,0,0,.55)": "SH", "rgba(0,0,0,.3)": "SH", "rgba(0,0,0,.28)": "SH", "rgba(0,0,0,.32)": "SH", "rgba(0,0,0,.18)": "SH", "rgba(0,0,0,.16)": "SH", "rgba(20,25,34,.12)": "SH", "rgba(20,25,34,.22)": "SH", "rgba(20,25,34,.14)": "SH", "rgba(4,6,10,.62)": "var(--dk-glass)", "rgba(10,13,16,.7)": "var(--dk-glass)", "rgba(10,13,16,.72)": "var(--dk-glass)", "rgba(10,13,16,.85)": "var(--dk-glass)", "rgba(10,13,16,.62)": "var(--dk-glass)", "rgba(5,7,11,.55)": "var(--dk-glass)", "rgba(10,12,18,.7)": "var(--dk-glass)", "rgba(8,11,17,.94)": "var(--elev)", "rgba(3,5,9,.72)": "var(--scrim)", "rgba(5,7,10,.6)": "var(--scrim)", "rgba(20,25,34,.35)": "var(--scrim)", "rgba(2,4,8,.22)": "var(--scrim)", "rgba(2,4,8,0)": "transparent", "rgba(3,5,9,.66)": "var(--spot)", "rgba(20,25,34,.45)": "var(--spot)", "rgba(255,255,255,.035)": "var(--hov)", "rgba(0,0,0,.035)": "var(--hov)", "rgba(255,255,255,.025)": "var(--hov)", "rgba(255,255,255,.1)": "var(--sel)", "rgba(255,255,255,.06)": "var(--sel)", "rgba(255,255,255,.07)": "var(--sel)", "rgba(0,0,0,.06)": "var(--sel)", "rgba(0,0,0,.07)": "var(--sel)", "rgba(124,243,255,.1)": "var(--sel)", "rgba(10,125,156,.1)": "var(--sel)", "rgba(214,222,236,.75)": "var(--dk-dim)", "rgba(255,255,255,.35)": "var(--glass-line)", "rgba(158,167,182,.4)": "var(--line2)", "rgba(72,83,102,.4)": "var(--line2)", "rgba(47,216,242,.11)": "color-mix(in srgb,var(--Z1) 11%,transparent)", "rgba(255,107,44,.12)": "color-mix(in srgb,var(--Z2) 12%,transparent)", "rgba(226,87,211,.24)": "color-mix(in srgb,var(--mix) 24%,transparent)", "rgba(180,156,255,.24)": "color-mix(in srgb,var(--vio) 24%,transparent)", "rgba(11,143,172,.1)": "color-mix(in srgb,var(--Z1) 10%,transparent)", "rgba(207,76,23,.1)": "color-mix(in srgb,var(--Z2) 10%,transparent)", "rgba(173,47,152,.14)": "color-mix(in srgb,var(--mix) 14%,transparent)", "rgba(106,79,208,.14)": "color-mix(in srgb,var(--vio) 14%,transparent)"}

FS = {8: 1, 9: 1, 9.5: 1, 10: 1, 10.5: 1, 11: 1, 11.5: 2, 12: 2, 12.5: 3, 13: 3, 13.5: 3, 14: 3, 14.5: 4, 15: 4, 15.5: 4, 16: 4, 17: 4, 18: 5, 19: 5, 20: 5, 24: 6, 32: 6}
SPACE = [(0.5, None), (2, "--s-h"), (4, "--s-1"), (8, "--s-2"), (12, "--s-3"), (16, "--s-4"), (24, "--s-6"), (32, "--s-8"), (48, "--s-12")]
ZMAP = {1: "--z-1", 2: "--z-2", 3: "--z-3", 4: "--z-3", 5: "--z-3", 6: "--z-3", 8: "--z-3", 40: "--z-sticky", 50: "--z-float", 60: "--z-float", 70: "--z-float", 80: "--z-modal", 85: "--z-modal", 90: "--z-top", 91: "--z-top", 92: "--z-top", 95: "--z-top"}
DROP_RULE = [re.compile(p) for p in [r"^html\.boot ", r"^body\.labsw ", r"^@property "]]
DROP_DECL = [re.compile(p) for p in [r"^box-shadow:0 0 12px ", r"^transition:--acc", r"^will-change:transform$", r"^animation:recp"]]


def split_top(css):
    out = []
    i = 0
    n = len(css)
    while i < n:
        while i < n and css[i] in " \t\r\n":
            i += 1
        if i >= n:
            break
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        j = i
        depth = 0
        q = None
        while j < n:
            c = css[j]
            if q:
                if c == q:
                    q = None
            elif c in "\"'":
                q = c
            elif css.startswith("/*", j):
                k = css.find("*/", j + 2)
                j = k + 1
            elif c == "{":
                if depth == 0:
                    pre = css[i:j]
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    body = css[css.find("{", i) + 1:j]
                    out.append((re.sub(r"/\*[\s\S]*?\*/", "", pre).strip(), body))
                    j += 1
                    break
            elif c == ";" and depth == 0:
                out.append((css[i:j].strip(), None))
                j += 1
                break
            j += 1
        i = j
    return out


def split_decls(body):
    out = []
    cur = ""
    depth = 0
    q = None
    for c in body:
        if q:
            cur += c
            if c == q:
                q = None
            continue
        if c in "\"'":
            q = c
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        if c == ";" and depth == 0:
            if cur.strip():
                out.append(cur.strip())
            cur = ""
        else:
            cur += c
    if cur.strip():
        out.append(cur.strip())
    return out


def snap_space(v):
    neg = v < 0
    a = abs(v)
    if a <= 1:
        return None
    if a > 52:
        return None
    best = min(SPACE[1:], key=lambda s: (abs(s[0] - a), -s[0]))
    return ("calc(-1*var(%s))" % best[1]) if neg else "var(%s)" % best[1]


def space_value(val):
    def rep(m):
        num = float(m.group(1))
        r = snap_space(num)
        return m.group(0) if r is None else r
    if re.search(r"(calc|min|max|clamp|env)\(", val):
        return val
    return re.sub(r"(?<![\w.#-])(-?\d*\.?\d+)px\b", rep, val)


def radius_value(val):
    def rep(m):
        num = float(m.group(1))
        if num == 0:
            return "0"
        if num >= 99:
            return "var(--r-2)"
        if num <= 2:
            return "var(--r-1)"
        if num <= 5:
            return "var(--r-2)"
        return "var(--r-3)"
    if re.search(r"(calc|var)\(", val):
        return val
    return re.sub(r"(?<![\w.])(\d*\.?\d+)px\b", rep, val)


def fs_tok(px):
    k = FS.get(px)
    if k is None:
        k = min(FS, key=lambda x: abs(x - px))
        k = FS[k]
    return "var(--t-%d)" % k


def font_value(val, short):
    if short:
        m = re.search(r"(^|\s)(\d*\.?\d+)px(?=[\s/]|$)", val)
        if not m:
            return val
        return val[:m.start(2)] + fs_tok(float(m.group(2))) + val[m.end(2) + 2:]
    if "calc(" in val:
        return re.sub(r"calc\((\d*\.?\d+)px\*", lambda m: "calc(" + fs_tok(float(m.group(1))) + "*", val)
    if "clamp(" in val:
        return "var(--t-5)"
    m = re.fullmatch(r"(\d*\.?\d+)px(\s*!important)?", val.strip())
    if not m:
        return val
    return fs_tok(float(m.group(1))) + (m.group(2) or "")


def color_value(val, prop):
    def hx(m):
        h = m.group(0).lower()
        return HEX.get(h, m.group(0))
    val = re.sub(r"#[0-9a-fA-F]{3,8}\b", hx, val)
    def rg(m):
        k = re.sub(r"\s", "", m.group(0))
        r = RGBA.get(k)
        if r is None:
            return m.group(0)
        if r == "SH":
            return "SHADOW"
        return r
    val = re.sub(r"rgba?\([^)]*\)", rg, val)
    if prop == "box-shadow" and "SHADOW" in val:
        val = "var(--sh-2)" if re.search(r"\b(2\d|[3-9]\d)px", val) else "var(--sh-1)"
    return val.replace("SHADOW", "transparent")


def motion_value(prop, val):
    v = val
    v = re.sub(r"\bvar\(--ease\)", "var(--ease-out)", v)
    v = re.sub(r"\bvar\(--eio\)", "var(--ease-in-out)", v)
    v = re.sub(r"cubic-bezier\(\.2,\.8,\.2,1\)", "var(--ease-out)", v)
    def dur(m):
        s = float(m.group(1))
        ms = s * 1000
        if ms <= 130:
            return "var(--d-1)"
        if ms <= 170:
            return "var(--d-2)"
        if ms <= 220:
            return "var(--d-3)"
        return "var(--d-4)"
    if prop.startswith("animation"):
        v = re.sub(r"(?<![\w.])(\d*\.\d+)s\b", lambda m: dur(m) if float(m.group(1)) <= .6 else m.group(0), v)
    if prop.startswith("transition"):
        v = re.sub(r"(?<![\w.])(\d*\.\d+|\d+)s\b", dur, v)
        v = re.sub(r"(?<![\w-])ease(?![\w-])", "var(--ease-out)", v)
        v = re.sub(r"(?<![\w-])linear(?![\w-])", "var(--ease-out)", v)
    return v


def gate_hover(sel):
    parts = [p.strip() for p in sel.split(",")]
    hov = [p for p in parts if ":hover" in p]
    rest = [p for p in parts if ":hover" not in p]
    return ",".join(hov), ",".join(rest)


def fix_decl(sel, d):
    if ":" not in d:
        return d
    prop, val = d.split(":", 1)
    prop = prop.strip()
    if not prop.startswith("--"):
        prop = prop.lower()
    val = val.strip()
    for p in DROP_DECL:
        if p.search(prop + ":" + val):
            return None
    if prop.startswith("--"):
        return prop + ":" + color_value(val, prop)
    if prop == "transition" and val.startswith("all"):
        return "transition:opacity var(--d-2) var(--ease-out)"
    if prop in ("padding", "margin", "gap", "row-gap", "column-gap", "padding-block", "padding-inline", "margin-block", "margin-inline") or prop.startswith("padding-") or prop.startswith("margin-"):
        val = space_value(val)
    elif prop == "border-radius":
        val = radius_value(val)
    elif prop == "font-size":
        val = font_value(val, False)
    elif prop == "font":
        val = font_value(val, True)
    elif prop == "z-index":
        m = re.fullmatch(r"(\d+)(\s*!important)?", val)
        if m and int(m.group(1)) in ZMAP:
            val = "var(%s)" % ZMAP[int(m.group(1))] + (m.group(2) or "")
    elif prop.startswith("transition") or prop.startswith("animation"):
        val = motion_value(prop, val)
    val = color_value(val, prop)
    return prop + ":" + val


def is_token_rule(sel):
    s = re.sub(r"\s+", " ", sel.strip())
    return s in TOKEN_SELS


def process(nodes, inside_kf=False):
    out = []
    for pre, body in nodes:
        if body is None:
            if pre.startswith("@import") or pre.startswith("@charset"):
                out.append(pre + ";")
            continue
        if any(p.search(pre) for p in DROP_RULE):
            continue
        if pre.startswith("@keyframes"):
            inner = split_top(body)
            out.append(pre + "{" + "".join(p + "{" + ";".join(x for x in (fix_decl(p, d) for d in split_decls(b)) if x) + "}" for p, b in inner) + "}")
            continue
        if pre.startswith("@"):
            out.append(pre + "{" + process(split_top(body)) + "}")
            continue
        sel = re.sub(r"\s+", " ", pre)
        decls = split_decls(body)
        if is_token_rule(sel):
            keep = [d for d in decls if not d.strip().startswith("--") and not d.strip().startswith("color-scheme")]
            if sel in (":root", ":root[data-theme=light]", "[data-theme=light]", ":root[data-theme=light] body") and not keep:
                continue
            if not keep:
                continue
            decls = keep
        elif LAB_RE.match(sel):
            m = LAB_RE.match(sel)
            lab = m.group(2).replace("al-", "")
            th = "light" if m.group(1) else "dark"
            nd = []
            for d in decls:
                k, v = [x.strip() for x in d.split(":", 1)]
                if k == "--acc":
                    continue
                if k in ("--Z1", "--Z2") and v.startswith("#"):
                    tk = "--lab-%s-%s" % (lab, k[-1])
                    LABTOK[th].append(tk + ":" + v)
                    nd.append(k + ":var(" + tk + ")")
                else:
                    nd.append(d)
            decls = nd
            if not decls:
                continue
        elif "data-theme=light" in sel and any(d.strip().startswith("--") for d in decls) and all(d.strip().startswith("--") or d.strip().startswith("color") for d in decls):
            nd = []
            for d in decls:
                k = d.split(":", 1)[0].strip()
                if k in DARK_REMAP:
                    nd.append(k + ":" + DARK_REMAP[k])
                elif k.startswith("--"):
                    nd.append(d)
                else:
                    nd.append(d)
            decls = nd
        fixed = [x for x in (fix_decl(sel, d) for d in decls) if x]
        if not fixed:
            continue
        body2 = ";".join(fixed)
        if ":hover" in sel:
            hov, rest = gate_hover(sel)
            if rest:
                out.append(rest + "{" + body2 + "}")
            out.append("@media (hover:hover) and (pointer:fine){" + hov + "{" + body2 + "}}")
        else:
            out.append(sel + "{" + body2 + "}")
    return "\n".join(out)


LABTOK = {"dark": [], "light": []}


def run(css, extra):
    LABTOK["dark"].clear()
    LABTOK["light"].clear()
    nodes = split_top(css)
    body = process(nodes)
    t = TOKENS.replace(";--z-top:40}", ";--z-top:40;" + ";".join(LABTOK["dark"]) + "}", 1)
    t = t.replace(";--spot:rgba(20,25,34,.45)}", ";--spot:rgba(20,25,34,.45);" + ";".join(LABTOK["light"]) + "}", 1)
    for x,y in (("--lab-cx-1:#4fd8ff","--lab-cx-1:var(--dk-ax-x)"),("--lab-cx-2:#ff9a4a","--lab-cx-2:var(--dk-ax-y)"),("--lab-cx-1:#0b84a8","--lab-cx-1:#b23a3a"),("--lab-cx-2:#c45a12","--lab-cx-2:#1f7333")):
        t = t.replace(x, y)
    return t + body + "\n" + extra
