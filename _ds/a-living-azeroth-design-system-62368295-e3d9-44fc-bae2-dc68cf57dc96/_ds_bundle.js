/* @ds-bundle: {"format":4,"namespace":"ALivingAzerothDesignSystem_623682","components":[{"name":"Button","sourcePath":"components/controls/Button.jsx"},{"name":"FilterChip","sourcePath":"components/controls/FilterChip.jsx"},{"name":"SearchInput","sourcePath":"components/controls/SearchInput.jsx"},{"name":"Select","sourcePath":"components/controls/Select.jsx"},{"name":"EmptyState","sourcePath":"components/data/EmptyState.jsx"},{"name":"InterlockSpine","sourcePath":"components/data/InterlockSpine.jsx"},{"name":"ProposalTable","sourcePath":"components/data/ProposalTable.jsx"},{"name":"ProposalTooltip","sourcePath":"components/data/ProposalTooltip.jsx"},{"name":"ZonePicker","sourcePath":"components/data/ZonePicker.jsx"},{"name":"CiteRef","sourcePath":"components/document/CiteRef.jsx"},{"name":"DataField","sourcePath":"components/document/DataField.jsx"},{"name":"Note","sourcePath":"components/document/Note.jsx"},{"name":"Prose","sourcePath":"components/document/Prose.jsx"},{"name":"SectionHeading","sourcePath":"components/document/SectionHeading.jsx"},{"name":"TierBadge","sourcePath":"components/document/TierBadge.jsx"},{"name":"DocFooter","sourcePath":"components/navigation/DocFooter.jsx"},{"name":"SidebarTOC","sourcePath":"components/navigation/SidebarTOC.jsx"}],"sourceHashes":{"components/controls/Button.jsx":"e61358146a7e","components/controls/FilterChip.jsx":"766a91e7da3b","components/controls/SearchInput.jsx":"710ba5b340ae","components/controls/Select.jsx":"8fa81568dad8","components/data/EmptyState.jsx":"e2830c141058","components/data/InterlockSpine.jsx":"e92635c562cd","components/data/ProposalTable.jsx":"2511ccb6a4ac","components/data/ProposalTooltip.jsx":"4e89f83f8200","components/data/ZonePicker.jsx":"f36ba02034f5","components/document/CiteRef.jsx":"5862047d369c","components/document/DataField.jsx":"743fe59b8347","components/document/Note.jsx":"f789f2230167","components/document/Prose.jsx":"cbf51f7f5cd7","components/document/SectionHeading.jsx":"867f48abb011","components/document/TierBadge.jsx":"69dcc707ca52","components/navigation/DocFooter.jsx":"b49e12789f20","components/navigation/SidebarTOC.jsx":"555e3d56c8d8","ui_kits/living-azeroth/App.jsx":"8a66422e1130","ui_kits/living-azeroth/DocumentBody.jsx":"57600a1482b9","ui_kits/living-azeroth/Hero.jsx":"8f8f70799ea9","ui_kits/living-azeroth/ProposalBrowser.jsx":"43576cfff738","ui_kits/living-azeroth/SpineView.jsx":"f68837a99230","ui_kits/living-azeroth/ZoneView.jsx":"8d98e5eec60d"},"inlinedExternals":[],"unexposedExports":[{"name":"buildGraph","sourcePath":"components/data/InterlockSpine.jsx"},{"name":"neighboursOf","sourcePath":"components/data/InterlockSpine.jsx"}]} */

(() => {

const __ds_ns = (window.ALivingAzerothDesignSystem_623682 = window.ALivingAzerothDesignSystem_623682 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/controls/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function Button({
  variant = "default",
  size = "md",
  children,
  ...rest
}) {
  const cls = ["az-btn", variant !== "default" && "az-btn--" + variant, size === "sm" && "az-btn--sm"].filter(Boolean).join(" ");
  return /*#__PURE__*/React.createElement("button", _extends({
    type: "button",
    className: cls
  }, rest), children);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/controls/Button.jsx", error: String((e && e.message) || e) }); }

// components/controls/FilterChip.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function FilterChip({
  label,
  count,
  pressed = false,
  tier,
  onToggle,
  ...rest
}) {
  const cls = ["az-chip", tier && "az-chip--tier-" + tier].filter(Boolean).join(" ");
  return /*#__PURE__*/React.createElement("button", _extends({
    type: "button",
    className: cls,
    "aria-pressed": pressed,
    onClick: onToggle
  }, rest), tier ? /*#__PURE__*/React.createElement("span", {
    className: "az-tier__dot",
    style: {
      color: "var(--tier-" + tier + ")"
    }
  }) : null, label, count != null ? /*#__PURE__*/React.createElement("span", {
    className: "az-chip__count"
  }, count) : null);
}
Object.assign(__ds_scope, { FilterChip });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/controls/FilterChip.jsx", error: String((e && e.message) || e) }); }

// components/controls/SearchInput.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function SearchInput({
  value = "",
  onChange,
  placeholder = "Search proposals",
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    className: "az-search"
  }, rest), /*#__PURE__*/React.createElement("input", {
    type: "search",
    className: "az-search__input",
    value: value,
    placeholder: placeholder,
    onChange: e => onChange && onChange(e.target.value)
  }), value ? /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "az-search__clear",
    "aria-label": "Clear search",
    onClick: () => onChange && onChange("")
  }, "\xD7") : null);
}
Object.assign(__ds_scope, { SearchInput });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/controls/SearchInput.jsx", error: String((e && e.message) || e) }); }

// components/controls/Select.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function Select({
  label,
  value,
  options = [],
  onChange,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("label", _extends({
    className: "az-select"
  }, rest), label ? /*#__PURE__*/React.createElement("span", {
    className: "az-select__label"
  }, label) : null, /*#__PURE__*/React.createElement("select", {
    className: "az-select__control",
    value: value,
    onChange: e => onChange && onChange(e.target.value)
  }, options.map(o => {
    const opt = typeof o === "string" ? {
      value: o,
      label: o
    } : o;
    return /*#__PURE__*/React.createElement("option", {
      key: opt.value,
      value: opt.value
    }, opt.label);
  })));
}
Object.assign(__ds_scope, { Select });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/controls/Select.jsx", error: String((e && e.message) || e) }); }

// components/data/EmptyState.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function EmptyState({
  title = "Nothing matches",
  hint,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    className: "az-empty"
  }, rest), /*#__PURE__*/React.createElement("p", {
    className: "az-empty__title"
  }, title), hint ? /*#__PURE__*/React.createElement("p", {
    className: "az-empty__hint"
  }, hint) : null);
}
Object.assign(__ds_scope, { EmptyState });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/EmptyState.jsx", error: String((e && e.message) || e) }); }

// components/data/InterlockSpine.jsx
try { (() => {
const TIER_META = {
  1: {
    name: "Cosmetic and behavioral",
    short: "Patchable anytime"
  },
  2: {
    name: "Contained new systems",
    short: "Post-launch, but planned"
  },
  3: {
    name: "Architectural",
    short: "Launch decision"
  }
};

/* The graph is read from dependsOn / enables. Nothing here is hand-placed. */
function buildGraph(proposals) {
  const byId = new Map(proposals.map(p => [p.id, p]));
  const seen = new Set();
  const edges = [];
  const push = (from, to) => {
    if (!byId.has(from) || !byId.has(to) || from === to) return;
    const k = from + ">" + to;
    if (seen.has(k)) return;
    seen.add(k);
    const a = byId.get(from),
      b = byId.get(to);
    const trade = p => p.systems.some(s => s === "Trade" || s === "Economy");
    edges.push({
      from,
      to,
      kind: trade(a) && trade(b) ? "cargo" : "enables"
    });
  };
  proposals.forEach(p => {
    (p.dependsOn || []).forEach(d => push(d, p.id));
    (p.enables || []).forEach(e => push(p.id, e));
  });
  const linked = new Set();
  edges.forEach(e => {
    linked.add(e.from);
    linked.add(e.to);
  });
  const nodes = proposals.filter(p => linked.has(p.id));
  const orphans = proposals.filter(p => !linked.has(p.id));
  const out = new Map(nodes.map(n => [n.id, []]));
  edges.forEach(e => out.get(e.from).push(e.to));
  const reach = new Map();
  const walk = (id, guard) => {
    if (reach.has(id)) return reach.get(id);
    if (guard.has(id)) return new Set();
    guard.add(id);
    const acc = new Set();
    out.get(id).forEach(t => {
      acc.add(t);
      walk(t, guard).forEach(x => acc.add(x));
    });
    guard.delete(id);
    reach.set(id, acc);
    return acc;
  };
  nodes.forEach(n => walk(n.id, new Set()));
  const weight = new Map(nodes.map(n => [n.id, reach.get(n.id).size]));
  const sub = new Map(nodes.map(n => [n.id, 0]));
  for (let i = 0; i < nodes.length; i++) {
    let moved = false;
    edges.forEach(e => {
      if (byId.get(e.from).tier !== byId.get(e.to).tier) return;
      const v = sub.get(e.from) + 1;
      if (v > sub.get(e.to)) {
        sub.set(e.to, v);
        moved = true;
      }
    });
    if (!moved) break;
  }
  return {
    nodes,
    orphans,
    edges,
    weight,
    sub,
    byId
  };
}
function neighboursOf(id, edges) {
  const set = new Set([id]);
  edges.forEach(e => {
    if (e.from === id) set.add(e.to);
    if (e.to === id) set.add(e.from);
  });
  return Array.from(set);
}
function wrap(title, per, max) {
  const words = title.split(" ");
  const lines = [];
  let cur = "";
  words.forEach(w => {
    if (!cur.length) cur = w;else if ((cur + " " + w).length <= per) cur += " " + w;else {
      lines.push(cur);
      cur = w;
    }
  });
  if (cur) lines.push(cur);
  if (lines.length > max) {
    const kept = lines.slice(0, max);
    kept[max - 1] = kept[max - 1].slice(0, per - 1).trimEnd() + "\u2026";
    return kept;
  }
  return lines;
}
const ICON = 44;
const HALF = ICON / 2;
function InterlockSpine({
  proposals = [],
  activeId = null,
  onSelect,
  columns = 6,
  animate = true,
  edgeLabels = {},
  showOrphans = true
}) {
  const g = React.useMemo(() => buildGraph(proposals), [proposals]);
  const {
    nodes,
    orphans,
    edges,
    weight,
    sub,
    byId
  } = g;
  const layout = React.useMemo(() => {
    const HEAD = 140,
      W = 128,
      H = 104,
      TOP = 34;
    const cols = Math.max(2, columns);
    const pos = new Map();
    const bands = [];
    let line = 0;
    [1, 2, 3].forEach(t => {
      const list = nodes.filter(n => n.tier === t);
      if (!list.length) return;
      const idx = new Map();
      list.sort((a, b) => {
        const sa = sub.get(a.id),
          sb = sub.get(b.id);
        if (sa !== sb) return sa - sb;
        return weight.get(b.id) - weight.get(a.id) || a.title.localeCompare(b.title);
      });
      const first = line;
      list.forEach((n, i) => {
        const ln = first + Math.floor(i / cols);
        const col = i % cols;
        idx.set(n.id, i);
        pos.set(n.id, {
          x: HEAD + col * W + W / 2,
          y: TOP + 46 + ln * H,
          line: ln,
          col
        });
      });
      const lines = Math.ceil(list.length / cols);
      bands.push({
        tier: t,
        first,
        lines,
        count: list.length,
        y: TOP + ln0(first, TOP, H)
      });
      line = first + lines;
    });
    function ln0(l, top, h) {
      return l * h;
    }
    const bodyLines = line;
    const oTop = TOP + bodyLines * H + 24;
    const oPos = new Map();
    let oLines = 0;
    if (showOrphans && orphans.length) {
      oLines = Math.ceil(orphans.length / cols);
      orphans.forEach((o, i) => {
        oPos.set(o.id, {
          x: HEAD + i % cols * W + W / 2,
          y: oTop + 66 + Math.floor(i / cols) * H,
          line: -1
        });
      });
    }
    return {
      pos,
      oPos,
      bands,
      HEAD,
      W,
      H,
      TOP,
      width: HEAD + cols * W + 16,
      height: oLines ? oTop + 66 + (oLines - 1) * H + 58 : TOP + bodyLines * H + 10,
      oTop
    };
  }, [nodes, orphans, sub, weight, columns, showOrphans]);
  const near = React.useMemo(() => activeId ? new Set(neighboursOf(activeId, edges)) : null, [activeId, edges]);

  /* Orthogonal talent-tree arrows: down a gutter, across a channel, into the top
     of the target. Same-line edges run above the icons. */
  function route(a, b) {
    if (a.line === b.line) {
      const dir = b.x > a.x ? 1 : -1;
      const y = a.y - 34;
      return {
        d: "M" + (a.x + dir * HALF) + " " + a.y + " L" + (a.x + dir * (HALF + 14)) + " " + a.y + " L" + (a.x + dir * (HALF + 14)) + " " + y + " L" + b.x + " " + y + " L" + b.x + " " + (b.y - HALF - 6),
        head: {
          x: b.x,
          y: b.y - HALF - 5,
          r: 0
        },
        mid: {
          x: (a.x + b.x) / 2,
          y: y - 5
        }
      };
    }
    const dir = b.x >= a.x ? 1 : -1;
    const gut = a.x + dir * (HALF + 22);
    const chan = b.y - 34;
    return {
      d: "M" + (a.x + dir * HALF) + " " + a.y + " L" + gut + " " + a.y + " L" + gut + " " + chan + " L" + b.x + " " + chan + " L" + b.x + " " + (b.y - HALF - 6),
      head: {
        x: b.x,
        y: b.y - HALF - 5,
        r: 0
      },
      mid: {
        x: gut + 7,
        y: (a.y + chan) / 2,
        anchor: "start"
      }
    };
  }
  const node = (n, p, independent) => {
    const dim = near && !near.has(n.id);
    const active = activeId === n.id;
    const q = "var(--tier-" + n.tier + ")";
    const rank = weight.get(n.id) || 0;
    const lines = wrap(n.title, 16, 2);
    return /*#__PURE__*/React.createElement("g", {
      key: n.id,
      className: "az-tree__node",
      "data-active": active ? "true" : "false",
      transform: "translate(" + p.x + "," + p.y + ")",
      tabIndex: 0,
      role: "button",
      "aria-label": n.title + ", tier " + n.tier + ", section " + n.section,
      opacity: dim ? 0.3 : 1,
      onClick: () => onSelect && onSelect(active ? null : n.id, neighboursOf(n.id, edges)),
      onKeyDown: e => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          onSelect && onSelect(active ? null : n.id, neighboursOf(n.id, edges));
        }
      }
    }, /*#__PURE__*/React.createElement("rect", {
      className: "az-tree__icon",
      x: -HALF,
      y: -HALF,
      width: ICON,
      height: ICON,
      rx: "2",
      stroke: q,
      strokeDasharray: independent ? "3 3" : undefined,
      fill: active ? q : undefined,
      fillOpacity: active ? 0.22 : 1
    }), /*#__PURE__*/React.createElement("text", {
      className: "az-tree__num",
      y: "1",
      fill: q
    }, n.section), rank > 0 ? /*#__PURE__*/React.createElement("g", {
      transform: "translate(" + (HALF - 3) + "," + (HALF - 3) + ")"
    }, /*#__PURE__*/React.createElement("rect", {
      className: "az-tree__rank",
      x: "-11",
      y: "-8",
      width: "22",
      height: "16",
      rx: "2"
    }), /*#__PURE__*/React.createElement("text", {
      className: "az-tree__rankn",
      y: "1"
    }, rank)) : null, lines.map((l, i) => /*#__PURE__*/React.createElement("text", {
      className: "az-tree__label",
      key: i,
      y: HALF + 15 + i * 13
    }, l)));
  };
  return /*#__PURE__*/React.createElement("svg", {
    className: "az-tree",
    viewBox: "0 0 " + layout.width + " " + layout.height,
    width: layout.width,
    height: layout.height,
    style: {
      width: layout.width,
      minWidth: layout.width,
      height: layout.height
    },
    role: "group",
    "aria-label": "Interlock tree: proposals by tier with dependency arrows"
  }, layout.bands.map(b => {
    const y = layout.TOP + b.first * layout.H;
    return /*#__PURE__*/React.createElement("g", {
      key: "b" + b.tier
    }, /*#__PURE__*/React.createElement("line", {
      className: "az-tree__tierrule",
      x1: "16",
      y1: y,
      x2: layout.width - 16,
      y2: y
    }), /*#__PURE__*/React.createElement("text", {
      className: "az-tree__tierlabel",
      x: "16",
      y: y + 26,
      fill: "var(--tier-" + b.tier + ")"
    }, "Tier " + b.tier), /*#__PURE__*/React.createElement("text", {
      className: "az-tree__tiersub",
      x: "16",
      y: y + 44
    }, TIER_META[b.tier].name), /*#__PURE__*/React.createElement("text", {
      className: "az-tree__tiersub",
      x: "16",
      y: y + 60
    }, TIER_META[b.tier].short), /*#__PURE__*/React.createElement("text", {
      className: "az-tree__tiersub",
      x: "16",
      y: y + 80
    }, b.count + (b.count === 1 ? " proposal" : " proposals")));
  }), /*#__PURE__*/React.createElement("g", null, edges.map((e, i) => {
    const a = layout.pos.get(e.from),
      b = layout.pos.get(e.to);
    if (!a || !b) return null;
    const cargo = e.kind === "cargo";
    const r = route(a, b);
    const w = cargo ? 1.6 + Math.min(weight.get(e.from), 6) * 0.5 : 1;
    const dim = near && !(near.has(e.from) && near.has(e.to));
    const label = cargo ? edgeLabels[e.from + ">" + e.to] : null;
    return /*#__PURE__*/React.createElement("g", {
      key: i,
      opacity: dim ? 0.12 : 1
    }, /*#__PURE__*/React.createElement("path", {
      className: "az-tree__arrow az-tree__arrow--" + e.kind + (animate && cargo ? " az-tree__draw" : ""),
      d: r.d,
      pathLength: "1",
      strokeWidth: cargo ? w : undefined,
      style: {
        "--len": 1,
        animationDelay: (byId.get(e.from).tier - 1) * 220 + "ms"
      }
    }), /*#__PURE__*/React.createElement("path", {
      className: "az-tree__head" + (cargo ? "" : " az-tree__head--enables"),
      d: "M" + (r.head.x - 4.5) + " " + (r.head.y - 6) + " L" + (r.head.x + 4.5) + " " + (r.head.y - 6) + " L" + r.head.x + " " + (r.head.y + 1) + " Z"
    }), label ? /*#__PURE__*/React.createElement("text", {
      className: "az-tree__cargo",
      x: r.mid.x,
      y: r.mid.y,
      textAnchor: r.mid.anchor || "middle"
    }, label) : null);
  })), /*#__PURE__*/React.createElement("g", null, nodes.map(n => node(n, layout.pos.get(n.id), false))), showOrphans && orphans.length ? /*#__PURE__*/React.createElement("g", null, /*#__PURE__*/React.createElement("line", {
    className: "az-tree__tierrule",
    x1: "16",
    y1: layout.oTop,
    x2: layout.width - 16,
    y2: layout.oTop
  }), /*#__PURE__*/React.createElement("text", {
    className: "az-tree__tierlabel",
    x: "16",
    y: layout.oTop + 26,
    fill: "var(--gold-dim)"
  }, "Independent"), /*#__PURE__*/React.createElement("text", {
    className: "az-tree__tiersub",
    x: "16",
    y: layout.oTop + 44
  }, "No dependency either way"), /*#__PURE__*/React.createElement("text", {
    className: "az-tree__tiersub",
    x: "16",
    y: layout.oTop + 64
  }, orphans.length + " proposals"), orphans.map(o => node(o, layout.oPos.get(o.id), true))) : null);
}
Object.assign(__ds_scope, { buildGraph, neighboursOf, InterlockSpine });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/InterlockSpine.jsx", error: String((e && e.message) || e) }); }

// components/data/ProposalTooltip.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const COST_REQ = {
  low: "Requires: patch slot",
  medium: "Requires: engineering",
  high: "Requires: launch decision"
};
function ProposalTooltip({
  proposal,
  showFlavor = true,
  ...rest
}) {
  if (!proposal) return null;
  const p = proposal;
  const line = (k, v, dim) => v ? /*#__PURE__*/React.createElement("li", {
    className: "az-tooltip__line" + (dim ? " az-tooltip__line--dim" : ""),
    key: k
  }, /*#__PURE__*/React.createElement("span", {
    className: "az-tooltip__key"
  }, k), /*#__PURE__*/React.createElement("span", null, v)) : null;
  return /*#__PURE__*/React.createElement("div", _extends({
    className: "az-tooltip az-tooltip--" + p.tier
  }, rest), /*#__PURE__*/React.createElement("p", {
    className: "az-tooltip__name az-tooltip__name--" + p.tier
  }, p.title), /*#__PURE__*/React.createElement("ul", {
    className: "az-tooltip__lines"
  }, line("Section", p.section), line("Tier", p.tier + " of 3"), line("Cost", p.cost), line("Systems", (p.systems || []).join(", ")), line("Zones", (p.zones || []).join(", "), true), line("Factions", (p.factions || []).join(", "), true), line("Depends on", (p.dependsOn || []).join(", ")), line("Enables", (p.enables || []).join(", "))), /*#__PURE__*/React.createElement("p", {
    className: "az-tooltip__req"
  }, COST_REQ[p.cost]), showFlavor && p.note ? /*#__PURE__*/React.createElement("p", {
    className: "az-tooltip__flavor"
  }, p.note) : null);
}
Object.assign(__ds_scope, { ProposalTooltip });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/ProposalTooltip.jsx", error: String((e && e.message) || e) }); }

// components/data/ZonePicker.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function ZonePicker({
  zones = [],
  value = null,
  onChange,
  showCounts = true,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    className: "az-zones"
  }, rest), zones.map(z => {
    const zone = typeof z === "string" ? {
      name: z
    } : z;
    const on = value === zone.name;
    return /*#__PURE__*/React.createElement("button", {
      key: zone.name,
      type: "button",
      className: "az-zone",
      "aria-pressed": on,
      onClick: () => onChange && onChange(on ? null : zone.name)
    }, zone.name, showCounts && zone.count != null ? /*#__PURE__*/React.createElement("span", {
      className: "az-zone__n"
    }, zone.count) : null);
  }));
}
Object.assign(__ds_scope, { ZonePicker });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/ZonePicker.jsx", error: String((e && e.message) || e) }); }

// components/document/CiteRef.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function CiteRef({
  n,
  href,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("a", _extends({
    className: "az-cite",
    href: href || "#source-" + n,
    title: "Source " + n
  }, rest), "[", n, "]");
}
Object.assign(__ds_scope, { CiteRef });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/document/CiteRef.jsx", error: String((e && e.message) || e) }); }

// components/document/DataField.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function DataField({
  label,
  value,
  children,
  inline = false,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    className: "az-field" + (inline ? " az-field--inline" : "")
  }, rest), /*#__PURE__*/React.createElement("span", {
    className: "az-field__label"
  }, label), /*#__PURE__*/React.createElement("span", {
    className: "az-field__value"
  }, children != null ? children : value));
}
Object.assign(__ds_scope, { DataField });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/document/DataField.jsx", error: String((e && e.message) || e) }); }

// components/document/Note.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function Note({
  label,
  accent = "default",
  children,
  ...rest
}) {
  const map = {
    route: "az-note--route",
    1: "az-note--1",
    2: "az-note--2",
    3: "az-note--3"
  };
  return /*#__PURE__*/React.createElement("aside", _extends({
    className: ["az-note", map[accent]].filter(Boolean).join(" ")
  }, rest), label ? /*#__PURE__*/React.createElement("span", {
    className: "az-note__label"
  }, label) : null, /*#__PURE__*/React.createElement("div", {
    className: "az-note__body"
  }, children));
}
Object.assign(__ds_scope, { Note });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/document/Note.jsx", error: String((e && e.message) || e) }); }

// components/document/Prose.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function Prose({
  children,
  narrow = false,
  as: Tag = "div",
  ...rest
}) {
  return /*#__PURE__*/React.createElement(Tag, _extends({
    className: "az-prose" + (narrow ? " az-prose--narrow" : "")
  }, rest), children);
}
Object.assign(__ds_scope, { Prose });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/document/Prose.jsx", error: String((e && e.message) || e) }); }

// components/document/SectionHeading.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
function SectionHeading({
  number,
  title,
  id,
  level = 2,
  rule = false,
  kicker,
  ...rest
}) {
  const Tag = "h" + level;
  return /*#__PURE__*/React.createElement("header", _extends({
    className: "az-heading",
    id: id
  }, rest), number ? /*#__PURE__*/React.createElement("span", {
    className: "az-eyebrow"
  }, number, kicker ? " \u00b7 " + kicker : "") : null, /*#__PURE__*/React.createElement(Tag, {
    className: "az-heading__title"
  }, title), rule ? /*#__PURE__*/React.createElement("hr", {
    className: "az-heading__rule"
  }) : null);
}
Object.assign(__ds_scope, { SectionHeading });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/document/SectionHeading.jsx", error: String((e && e.message) || e) }); }

// components/document/TierBadge.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const TIERS = {
  1: {
    name: "Cosmetic and behavioral",
    short: "Patchable anytime"
  },
  2: {
    name: "Contained new systems",
    short: "Post-launch, but planned"
  },
  3: {
    name: "Architectural",
    short: "Launch decision"
  }
};
function TierBadge({
  tier = 1,
  label,
  variant = "default",
  size = "md",
  dot = true,
  ...rest
}) {
  const t = TIERS[tier] || TIERS[1];
  const cls = ["az-tier", "az-tier--" + tier, variant === "bare" && "az-tier--bare", size === "sm" && "az-tier--sm"].filter(Boolean).join(" ");
  return /*#__PURE__*/React.createElement("span", _extends({
    className: cls,
    title: "Tier " + tier + ": " + t.name + ". " + t.short + "."
  }, rest), dot ? /*#__PURE__*/React.createElement("span", {
    className: "az-tier__dot"
  }) : null, label || "Tier " + tier);
}
Object.assign(__ds_scope, { TierBadge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/document/TierBadge.jsx", error: String((e && e.message) || e) }); }

// components/data/ProposalTable.jsx
try { (() => {
const COST_ORDER = {
  low: 0,
  medium: 1,
  high: 2
};
const COLUMNS = [{
  key: "title",
  label: "Proposal"
}, {
  key: "section",
  label: "Section"
}, {
  key: "tier",
  label: "Tier"
}, {
  key: "cost",
  label: "Cost"
}, {
  key: "zones",
  label: "Zones"
}];
function compare(a, b, key) {
  if (key === "tier") return a.tier - b.tier;
  if (key === "cost") return (COST_ORDER[a.cost] || 0) - (COST_ORDER[b.cost] || 0);
  if (key === "zones") return (a.zones || []).length - (b.zones || []).length;
  if (key === "section") return String(a.section).localeCompare(String(b.section), undefined, {
    numeric: true
  });
  return String(a.title).localeCompare(String(b.title));
}
function ProposalTable({
  proposals = [],
  caption,
  emptyHint = "Clear a tier or zone filter to bring rows back.",
  expandedId,
  onExpand,
  highlightIds
}) {
  const [sort, setSort] = React.useState({
    key: "section",
    dir: 1
  });
  const [localOpen, setLocalOpen] = React.useState(null);
  const open = expandedId !== undefined ? expandedId : localOpen;
  const setOpen = id => onExpand ? onExpand(id) : setLocalOpen(id);
  const highlight = highlightIds ? new Set(highlightIds) : null;
  const rows = React.useMemo(() => proposals.slice().sort((a, b) => compare(a, b, sort.key) * sort.dir), [proposals, sort]);
  if (!rows.length) {
    return /*#__PURE__*/React.createElement(__ds_scope.EmptyState, {
      title: "No proposals match these filters",
      hint: emptyHint
    });
  }
  const toggleSort = key => setSort(s => s.key === key ? {
    key,
    dir: -s.dir
  } : {
    key,
    dir: 1
  });
  return /*#__PURE__*/React.createElement("table", {
    className: "az-table"
  }, caption ? /*#__PURE__*/React.createElement("caption", null, caption) : null, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, COLUMNS.map(c => {
    const active = sort.key === c.key;
    return /*#__PURE__*/React.createElement("th", {
      key: c.key,
      scope: "col",
      "aria-sort": active ? sort.dir === 1 ? "ascending" : "descending" : "none",
      onClick: () => toggleSort(c.key),
      tabIndex: 0,
      onKeyDown: e => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          toggleSort(c.key);
        }
      }
    }, c.label, /*#__PURE__*/React.createElement("span", {
      className: "az-sortmark"
    }, active ? sort.dir === 1 ? "\u25b2" : "\u25bc" : "\u25b3"));
  }))), /*#__PURE__*/React.createElement("tbody", null, rows.map(p => {
    const isOpen = open === p.id;
    const dim = highlight && !highlight.has(p.id);
    return [/*#__PURE__*/React.createElement("tr", {
      key: p.id,
      className: "az-row" + (isOpen ? " az-row--open" : ""),
      style: dim ? {
        opacity: 0.42
      } : undefined,
      onClick: () => setOpen(isOpen ? null : p.id),
      tabIndex: 0,
      "aria-expanded": isOpen,
      onKeyDown: e => {
        if (e.key === "Enter") setOpen(isOpen ? null : p.id);
      }
    }, /*#__PURE__*/React.createElement("td", {
      className: "az-row__title"
    }, /*#__PURE__*/React.createElement("span", {
      className: "az-row__marker"
    }, isOpen ? "\u2212" : "+"), p.title), /*#__PURE__*/React.createElement("td", {
      className: "az-row__section"
    }, p.section), /*#__PURE__*/React.createElement("td", null, /*#__PURE__*/React.createElement(__ds_scope.TierBadge, {
      tier: p.tier,
      variant: "bare",
      size: "sm",
      label: "T" + p.tier
    })), /*#__PURE__*/React.createElement("td", {
      className: "az-row__cost"
    }, p.cost), /*#__PURE__*/React.createElement("td", {
      className: "az-row__zones"
    }, (p.zones || []).length)), /*#__PURE__*/React.createElement("tr", {
      key: p.id + "-d",
      className: "az-row__detail",
      style: isOpen ? undefined : {
        display: "none"
      }
    }, /*#__PURE__*/React.createElement("td", {
      colSpan: 5
    }, /*#__PURE__*/React.createElement(__ds_scope.ProposalTooltip, {
      proposal: p
    })))];
  })));
}
Object.assign(__ds_scope, { ProposalTable });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/data/ProposalTable.jsx", error: String((e && e.message) || e) }); }

// components/navigation/DocFooter.jsx
try { (() => {
function DocFooter({
  columns = [],
  disclaimer,
  children
}) {
  return /*#__PURE__*/React.createElement("footer", {
    className: "az-footer"
  }, /*#__PURE__*/React.createElement("div", {
    className: "az-footer__cols"
  }, columns.map(c => /*#__PURE__*/React.createElement("div", {
    key: c.label
  }, /*#__PURE__*/React.createElement("div", {
    className: "az-footer__label"
  }, c.label), /*#__PURE__*/React.createElement("ul", {
    className: "az-footer__list"
  }, c.items.map((it, i) => /*#__PURE__*/React.createElement("li", {
    key: i
  }, it.href ? /*#__PURE__*/React.createElement("a", {
    href: it.href
  }, it.label) : it.label)))))), children, disclaimer ? /*#__PURE__*/React.createElement("p", {
    className: "az-footer__disclaimer"
  }, disclaimer) : null);
}
Object.assign(__ds_scope, { DocFooter });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/navigation/DocFooter.jsx", error: String((e && e.message) || e) }); }

// components/navigation/SidebarTOC.jsx
try { (() => {
function SidebarTOC({
  items = [],
  activeId,
  onSelect,
  label
}) {
  const groups = [];
  items.forEach(it => {
    const g = it.group || "";
    let last = groups[groups.length - 1];
    if (!last || last.name !== g) {
      last = {
        name: g,
        items: []
      };
      groups.push(last);
    }
    last.items.push(it);
  });
  return /*#__PURE__*/React.createElement("nav", {
    className: "az-toc",
    "aria-label": label || "Table of contents"
  }, groups.map((g, gi) => /*#__PURE__*/React.createElement("div", {
    className: "az-toc__group",
    key: g.name + gi
  }, g.name ? /*#__PURE__*/React.createElement("span", {
    className: "az-toc__grouplabel"
  }, g.name) : null, g.items.map(it => /*#__PURE__*/React.createElement("a", {
    key: it.id,
    className: "az-toc__item",
    href: "#" + it.id,
    "aria-current": activeId === it.id ? "true" : undefined,
    onClick: e => {
      if (onSelect) {
        e.preventDefault();
        onSelect(it.id);
      }
    }
  }, /*#__PURE__*/React.createElement("span", {
    className: "az-toc__num"
  }, it.number), /*#__PURE__*/React.createElement("span", null, it.title))))));
}
Object.assign(__ds_scope, { SidebarTOC });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/navigation/SidebarTOC.jsx", error: String((e && e.message) || e) }); }

// ui_kits/living-azeroth/App.jsx
try { (() => {
const {
  SidebarTOC,
  DocFooter,
  Button
} = window.ALivingAzerothDesignSystem_623682;
const TOC = [{
  id: "s-0",
  number: "0",
  title: "Status and Scope",
  group: "Sections"
}, {
  id: "s-1",
  number: "1",
  title: "Ambient Life",
  group: "Sections"
}, {
  id: "s-2",
  number: "2",
  title: "Roads and Traffic",
  group: "Sections"
}, {
  id: "s-3",
  number: "3",
  title: "The Trade Network",
  group: "Sections"
}, {
  id: "s-4",
  number: "4",
  title: "Wildlife and Ecology",
  group: "Sections"
}, {
  id: "s-5",
  number: "5",
  title: "The Middle Tier",
  group: "Sections"
}, {
  id: "s-7",
  number: "7",
  title: "Loot Logic",
  group: "Sections"
}, {
  id: "s-8",
  number: "8",
  title: "Professions",
  group: "Sections"
}, {
  id: "s-9",
  number: "9",
  title: "Economy",
  group: "Sections"
}, {
  id: "s-10",
  number: "10",
  title: "Implementation Tiers",
  group: "Sections"
}, {
  id: "v-zone",
  number: "\u2014",
  title: "Zone view",
  group: "Interactive views"
}, {
  id: "v-spine",
  number: "\u2014",
  title: "Interlock spine",
  group: "Interactive views"
}, {
  id: "v-browser",
  number: "\u2014",
  title: "Proposal browser",
  group: "Interactive views"
}];
function useScrollSpy(ids) {
  const [active, setActive] = React.useState(ids[0]);
  React.useEffect(() => {
    const obs = new IntersectionObserver(entries => {
      const vis = entries.filter(e => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (vis.length) setActive(vis[0].target.id);
    }, {
      rootMargin: "-12% 0px -70% 0px"
    });
    ids.forEach(id => {
      const el = document.getElementById(id);
      if (el) obs.observe(el);
    });
    return () => obs.disconnect();
  }, [ids.join(",")]);
  return active;
}
function App({
  data
}) {
  const [dark, setDark] = React.useState(false);
  const [sheet, setSheet] = React.useState(false);
  const [focus, setFocus] = React.useState(null);
  const [highlight, setHighlight] = React.useState(null);
  const active = useScrollSpy(TOC.map(t => t.id));
  React.useEffect(() => {
    document.documentElement.setAttribute("data-theme", dark ? "dark" : "light");
  }, [dark]);
  const go = id => {
    setSheet(false);
    const el = document.getElementById(id);
    if (el) window.scrollTo({
      top: el.getBoundingClientRect().top + window.scrollY - 24,
      behavior: "smooth"
    });
  };
  const onSpineSelect = (id, neighbours) => {
    setFocus(id);
    setHighlight(id ? neighbours : null);
    if (id) {
      const el = document.getElementById("v-browser");
      if (el) window.scrollTo({
        top: el.getBoundingClientRect().top + window.scrollY - 24,
        behavior: "smooth"
      });
    }
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "shell"
  }, /*#__PURE__*/React.createElement("aside", {
    className: "rail" + (sheet ? " rail--open" : "")
  }, /*#__PURE__*/React.createElement("div", {
    className: "rail__inner"
  }, /*#__PURE__*/React.createElement("a", {
    className: "rail__mark",
    href: "#top",
    onClick: e => {
      e.preventDefault();
      go("top");
    }
  }, "A Living Azeroth"), /*#__PURE__*/React.createElement(SidebarTOC, {
    items: TOC,
    activeId: active,
    onSelect: go
  }), /*#__PURE__*/React.createElement("div", {
    className: "rail__foot"
  }, /*#__PURE__*/React.createElement(Button, {
    size: "sm",
    variant: "quiet",
    onClick: () => setDark(!dark)
  }, dark ? "Light ground" : "Dark ground")))), /*#__PURE__*/React.createElement("button", {
    className: "sheetbtn",
    onClick: () => setSheet(!sheet)
  }, sheet ? "Close" : "Contents"), /*#__PURE__*/React.createElement("main", {
    className: "main"
  }, /*#__PURE__*/React.createElement(Hero, {
    data: data
  }), /*#__PURE__*/React.createElement(DocumentBody, {
    part: "opening",
    data: data
  }), /*#__PURE__*/React.createElement(ZoneView, {
    data: data
  }), /*#__PURE__*/React.createElement(DocumentBody, {
    part: "trade",
    data: data
  }), /*#__PURE__*/React.createElement(DocumentBody, {
    part: "ecology",
    data: data
  }), /*#__PURE__*/React.createElement(DocumentBody, {
    part: "loot",
    data: data
  }), /*#__PURE__*/React.createElement(SpineView, {
    data: data,
    activeId: focus,
    onSelect: onSpineSelect
  }), /*#__PURE__*/React.createElement(DocumentBody, {
    part: "tiers",
    data: data
  }), /*#__PURE__*/React.createElement(ProposalBrowser, {
    data: data,
    highlightIds: highlight,
    onClearHighlight: () => {
      setFocus(null);
      setHighlight(null);
    }
  }), /*#__PURE__*/React.createElement(DocFooter, {
    columns: [{
      label: "Document",
      items: [{
        label: "Version " + data.meta.version
      }, {
        label: "July 2026"
      }, {
        label: "28 proposals, 10 sections"
      }]
    }, {
      label: "Lore references",
      items: [{
        label: "Wowpedia",
        href: "https://wowpedia.fandom.com"
      }, {
        label: "Warcraft Wiki",
        href: "https://warcraft.wiki.gg"
      }, {
        label: "Wowhead Classic zone maps",
        href: "https://www.wowhead.com/classic"
      }]
    }, {
      label: "Reporting",
      items: [{
        label: "Massively Overpowered",
        href: "https://massivelyop.com"
      }, {
        label: "MMORPG.com",
        href: "https://www.mmorpg.com"
      }, {
        label: "Kotaku",
        href: "https://kotaku.com"
      }]
    }],
    disclaimer: "Unofficial fan work. Not affiliated with or endorsed by Blizzard Entertainment. Sources on unannounced products are community reporting on unconfirmed rumors and should be treated as such."
  })));
}
Object.assign(window, {
  App
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/living-azeroth/App.jsx", error: String((e && e.message) || e) }); }

// ui_kits/living-azeroth/DocumentBody.jsx
try { (() => {
const {
  SectionHeading,
  Prose,
  Note,
  TierBadge,
  CiteRef,
  DataField
} = window.ALivingAzerothDesignSystem_623682;
function Named({
  tier,
  children
}) {
  return /*#__PURE__*/React.createElement("span", {
    className: "named"
  }, children, /*#__PURE__*/React.createElement(TierBadge, {
    tier: tier,
    variant: "bare",
    size: "sm",
    label: "T" + tier
  }));
}
function Section({
  number,
  title,
  id,
  kicker,
  children
}) {
  return /*#__PURE__*/React.createElement("section", {
    className: "section",
    id: id
  }, /*#__PURE__*/React.createElement(SectionHeading, {
    number: number,
    kicker: kicker,
    title: title,
    level: 2
  }), children);
}
function StatusSection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "0",
    title: "Status and Scope",
    id: "s-0"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "As of July 2026, Blizzard has not announced a product called \"Classic+.\" What is on the record is narrower: at the State of Azeroth stream on January 29, 2026, Blizzard said clarity on Classic's future would come at BlizzCon 2026 ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 1
  }), ". Everything else is community inference built on a real but ambiguous evidence base ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 2
  }), "."), /*#__PURE__*/React.createElement("p", null, "This document assumes nothing about what Blizzard is actually building. It is a design proposal, not a prediction. Almost every proposal follows the same method: find something the existing lore already asserts, and make the world show it.")), /*#__PURE__*/React.createElement(Note, {
    label: "Constraint"
  }, "Every proposal is anchored to a named vanilla location, faction, or NPC. \"Add wandering merchants\" is not a design. \"Run a Venture Company ore wagon down the Talondeep Path into the Barrens\" is."));
}
function AmbientSection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "1",
    title: "Ambient Life: NPCs Doing Their Jobs",
    id: "s-1"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "The cheapest immersion win in the game is idle animation variety tied to what a faction actually does for a living. Not combat behavior. Not quest hooks. Just work, rest, and downtime. ", /*#__PURE__*/React.createElement(Named, {
    tier: 1
  }, "NPC idle behavior and work animations"), " covers sections 1.1 through 1.5."), /*#__PURE__*/React.createElement("p", null, "Windshear Crag has been clear-cut by Venture Company logging under the leprous gnome Gerenzo Wrenchwhistle ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 9
  }), ". That is a described industrial operation, and the zone shows almost none of it in motion. Build the work chain visibly: a chopper crew felling a marked tree, a shredder hauling the log to a stacking yard, a foreman with a clipboard checking loads between hauls."), /*#__PURE__*/React.createElement("p", null, "The stacked lumber is the cargo. That is the connection to Section 2, and it is why", " ", /*#__PURE__*/React.createElement(Named, {
    tier: 1
  }, "city density with shift and daily routines"), " and", " ", /*#__PURE__*/React.createElement(Named, {
    tier: 1
  }, "hidden lore NPCs in hard-to-reach locations"), " sit in the same tier: none of it touches a drop table.")));
}
function RoadsSection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "2",
    title: "Roads and Traffic",
    id: "s-2"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, /*#__PURE__*/React.createElement(Named, {
    tier: 2
  }, "Cart and caravan routes"), " is the load-bearing feature of the whole document, because it connects the ambient layer to the economic layer. Vanilla already contains every component: escort NPCs pathing long distances under attack", " ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 10
  }), ", and NPCs running circuits between named locations ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 12
  }), ". What it lacks is that behavior as standing world furniture rather than as a quest object."), /*#__PURE__*/React.createElement("p", null, "Kalimdor's trade web should read as opportunistic and recent. Eastern Kingdoms should read as centuries deep: standing checkpoints, established schedules, roads with names.")), /*#__PURE__*/React.createElement(Note, {
    label: "Visibility tiers"
  }, "Walkable and interactive. Visible but not reachable, such as ships leaving Menethil on a schedule. Geographically impossible, such as a Dark Iron cart on a ledge across an unreachable ravine. ", /*#__PURE__*/React.createElement(Named, {
    tier: 1
  }, "Observational-only traffic"), " is the last two."));
}
function TradeSection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "3",
    title: "The Trade Network",
    id: "s-3"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "The Steamwheedle Cartel controls four cities in Classic: Booty Bay, Ratchet, Gadgetzan, and Everlook. It is in direct commercial competition with the Venture Company, with neither side above sabotage or murder ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 8
  }), ". That is a fully formed economic conflict sitting unused."), /*#__PURE__*/React.createElement("p", null, "Venture is the extraction arm. Steamwheedle buys and redistributes. The friction point is the Stranglethorn coast, where Bloodsail raiders can harass a shipment moving between Ratchet and Booty Bay, which turns them from a reputation grind into a visible commercial threat. ", /*#__PURE__*/React.createElement(Named, {
    tier: 3
  }, "Trade network stock movement"), " is where this lands.")), /*#__PURE__*/React.createElement(Note, {
    label: "Lore accuracy",
    accent: "route"
  }, "Everlook is a Steamwheedle Cartel city, not a Venture Company holding. If a Winterspring route is wanted, the interesting version is a hard, high-level Steamwheedle supply run down through Felwood ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 8
  }), "."));
}
function EcologySection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "4",
    title: "Wildlife and Ecology",
    id: "s-4"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "Vanilla's beasts are combat units with animal models. Every one of them notices you at the same radius, approaches the same way, and stands in the same place until it does.", " ", /*#__PURE__*/React.createElement(Named, {
    tier: 1
  }, "Creature rest and sleep cycles"), " has the largest gameplay consequence in the section: a bedded pack creates a live decision, sneak past or wake the den deliberately."), /*#__PURE__*/React.createElement("p", null, "The ecosystem stops being a separate system the moment it can threaten cargo.", " ", /*#__PURE__*/React.createElement(Named, {
    tier: 2
  }, "Predator threats to caravans"), " aims hyenas at draft animals rather than guards, which produces a different failure mode: the cargo is lost because the team bolted, not because it was stolen.")));
}
const MIDDLE_TIER = [{
  name: "Gnolls",
  zones: "Elwynn, Westfall, Redridge, Wetlands",
  body: "Design basis is hyena social structure, so show a crude hierarchy: a larger named model eating first, smaller ones squabbling over what is left. Unlike wolves, gnolls visibly use tools and hold loot. Stolen goods piled in a camp rather than existing only in a drop table.",
  cite: 12
}, {
  name: "Murlocs",
  zones: "Coastal, all continents",
  body: "The best just-above-animal case in the game, because their identity is a screeching alarm network rather than individuals. Keep the swarm alert. Add spear fishing at tide pools and shiny objects hoarded near huts, which finally explains the loot tables."
}, {
  name: "Kobolds",
  zones: "Elwynn, Westfall, Loch Modan",
  body: "Visibly the weakest of this tier: skittish, prone to breaking as a group when their strongest member dies rather than fighting to the last. The Jangolode Mine kobolds have Defias connections, which makes them a good candidate for showing a subordinate relationship between two hostile groups.",
  cite: 12
}, {
  name: "Harpies",
  zones: "Stonetalon, northern Barrens, Thousand Needles",
  body: "Airborne and nest-based rather than ground-camp based. Perch on cliff edges and dead trees, dive at what passes below, with nests tucked into cliffside terrain holding eggs and stolen shinies.",
  cite: 15
}, {
  name: "Quilboar",
  zones: "The Barrens, Razorfen",
  body: "Territorial and thorn-themed, so show it in the terrain: staked perimeters, crude thornbrush barricades, totemic markers. Quilboar defend ground. Gnolls raid it. That distinction should be legible without reading a single quest."
}];
function MiddleTierSection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "5",
    title: "The Middle Tier",
    kicker: "Gnolls, murlocs, kobolds, harpies, quilboar",
    id: "s-5"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "There is a behavioral gap between beasts and civilized factions that vanilla never dramatizes. These creatures have camps, hierarchy, tools, and territory, but they are not the Defias or the Scarlet Crusade. They should read as neither.", " ", /*#__PURE__*/React.createElement(Named, {
    tier: 1
  }, "Middle-tier humanoid camp behavior"), " is one proposal covering all five, and it is what ", /*#__PURE__*/React.createElement(Named, {
    tier: 2
  }, "unscripted faction flare-ups"), " depends on.")), /*#__PURE__*/React.createElement("dl", {
    className: "deflist"
  }, MIDDLE_TIER.map(m => /*#__PURE__*/React.createElement("div", {
    className: "deflist__row",
    key: m.name
  }, /*#__PURE__*/React.createElement("dt", null, /*#__PURE__*/React.createElement("span", {
    className: "deflist__name"
  }, m.name), /*#__PURE__*/React.createElement("span", {
    className: "deflist__meta"
  }, m.zones)), /*#__PURE__*/React.createElement("dd", null, m.body, m.cite ? /*#__PURE__*/React.createElement(React.Fragment, null, " ", /*#__PURE__*/React.createElement(CiteRef, {
    n: m.cite
  })) : null)))));
}
const COIN_BY_TYPE = [{
  type: "Beasts",
  coin: "None, ever",
  drops: "Pelts, fangs, claws, meat. Lost value pushed into vendor prices on those materials."
}, {
  type: "Bandit humanoids",
  coin: "Primary source",
  drops: "Defias, Syndicate, Bloodsail, Southsea. Lockpicks and stolen deeds; pilfered goblin hardware."
}, {
  type: "Military humanoids",
  coin: "Coin plus gear",
  drops: "Rank-scaled. A footman drops a common blade; a centurion drops officer-tier gear."
}, {
  type: "Cultists",
  coin: "Minimal",
  drops: "Twilight's Hammer, Burning Blade. Ritual components, robes, corrupted trinkets."
}, {
  type: "Constructs and elementals",
  coin: "None",
  drops: "Elemental materials only. Ghosts drop nothing physical beyond a memento."
}];
const COIN_BY_ZONE = [{
  zone: "Westfall",
  rule: "Poor across the board outside the Defias, reinforcing a depressed region rather than a farming ground."
}, {
  zone: "Un'goro Crater",
  rule: "No coin at any level, no exceptions. Nothing in the fiction explains a raptor carrying money."
}, {
  zone: "Stranglethorn and Booty Bay",
  rule: "Conspicuously plentiful, to make Westfall and Un'goro read as intentional rather than stingy."
}];
function LootSection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "7",
    title: "Loot Logic",
    id: "s-7"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "A timber wolf in Ashenvale drops silver coins. Nothing in the fiction explains this, and it breaks immersion at a rate of several times per minute during leveling.", " ", /*#__PURE__*/React.createElement(Named, {
    tier: 2
  }, "Coin removal from beasts"), " is the flavor version of the fix.", " ", /*#__PURE__*/React.createElement(Named, {
    tier: 3
  }, "Coin rebalance as income repricing"), " is the same change read as a deliberate reduction in leveling gold, which moves mount timing, respec affordability, and consumable access for every player.")), /*#__PURE__*/React.createElement("table", {
    className: "looptable"
  }, /*#__PURE__*/React.createElement("caption", null, "7.2 Coin by creature type"), /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Creature type"), /*#__PURE__*/React.createElement("th", null, "Coin"), /*#__PURE__*/React.createElement("th", null, "Instead"))), /*#__PURE__*/React.createElement("tbody", null, COIN_BY_TYPE.map(r => /*#__PURE__*/React.createElement("tr", {
    key: r.type
  }, /*#__PURE__*/React.createElement("td", null, r.type), /*#__PURE__*/React.createElement("td", {
    className: "looptable__mono"
  }, r.coin), /*#__PURE__*/React.createElement("td", null, r.drops))))), /*#__PURE__*/React.createElement("table", {
    className: "looptable"
  }, /*#__PURE__*/React.createElement("caption", null, "7.3 Coin by zone"), /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Zone"), /*#__PURE__*/React.createElement("th", null, "Economic character"))), /*#__PURE__*/React.createElement("tbody", null, COIN_BY_ZONE.map(r => /*#__PURE__*/React.createElement("tr", {
    key: r.zone
  }, /*#__PURE__*/React.createElement("td", null, r.zone), /*#__PURE__*/React.createElement("td", null, r.rule))))), /*#__PURE__*/React.createElement(Note, {
    label: "Tuning",
    accent: 2
  }, /*#__PURE__*/React.createElement(Named, {
    tier: 2
  }, "Swallowed remains and rare story loot"), " is framed as what the creature ate, not what it owned. These should not be findable on purpose in any efficient way. If a player grinds for one, that is allowed and it should be a bad idea."));
}
const PROFESSIONS = [{
  n: "8.1",
  id: "jewelcrafting",
  title: "Jewelcrafting",
  tier: 2,
  body: "Sockets arrived with The Burning Crusade, so a vanilla scribe of gems has to be a finished-goods profession: rings, necks and trinkets crafted whole, competing with dungeon jewelry.",
  cite: 19
}, {
  n: "8.2",
  id: "inscription",
  title: "Inscription",
  tier: 2,
  body: "Glyphs presuppose a far more granular talent system than vanilla has. A vanilla scribe makes scrolls and caster offhands instead, staying away from talents entirely."
}, {
  n: "8.3",
  id: "woodcutting",
  title: "Woodcutting",
  tier: 2,
  body: "Gives lumber an economic identity, supplies the cart network with a crafted input, and creates direct competition with Venture over the same forests."
}, {
  n: "8.4",
  id: "regional-cooking",
  title: "Regional cooking recipes",
  tier: 2,
  body: "Ties recipes to geography and gives the trade network something to carry."
}, {
  n: "8.5",
  id: "trapping",
  title: "Trapping",
  tier: 2,
  body: "The only proposal that interacts with wildlife without killing anything. Everything else in the ecology and loot sections is kill-and-loot."
}, {
  n: "8.6",
  id: "relic-hunting",
  title: "Relic hunting",
  tier: 2,
  body: "Explicitly no power progression, so it never competes with the real profession economy. It exists to give the hidden content something to connect to."
}, {
  n: "8.7",
  id: "cross-tier-materials",
  title: "Cross-tier material requirements",
  tier: 3,
  body: "A level 60 alchemist farming silverleaf because it is cost-effective, not because a quest sent them, is the goal state."
}, {
  n: "8.8",
  id: "cross-profession-dependencies",
  title: "Cross-profession dependencies",
  tier: 2,
  body: "Fishing into alchemy turns specific lakes into destinations for alchemists, not just anglers. Crushed low-tier gems give jewelcrafting and enchanting a reason to trade."
}, {
  n: "8.9",
  id: "craftable-vendor-goods",
  title: "Craftable vendor trade goods",
  tier: 2,
  body: "Coarse thread, weak flux, empty vials. Every one of those purchases is a dead gold sink that bypasses the player economy.",
  cite: 21
}];
function ProfessionsSection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "8",
    title: "Professions",
    id: "s-8"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "Nine proposals, seven of them Tier 2, and the densest part of the document. New professions land in Tier 2 rather than Tier 3 because adding a profession does not require touching the ones that already exist.")), /*#__PURE__*/React.createElement("ol", {
    className: "proflist"
  }, PROFESSIONS.map(p => /*#__PURE__*/React.createElement("li", {
    key: p.id
  }, /*#__PURE__*/React.createElement("div", {
    className: "proflist__head"
  }, /*#__PURE__*/React.createElement("span", {
    className: "proflist__n"
  }, p.n), /*#__PURE__*/React.createElement("span", {
    className: "proflist__title"
  }, p.title), /*#__PURE__*/React.createElement(TierBadge, {
    tier: p.tier,
    variant: "bare",
    size: "sm",
    label: "T" + p.tier
  })), /*#__PURE__*/React.createElement("p", {
    className: "proflist__body"
  }, p.body, p.cite ? /*#__PURE__*/React.createElement(React.Fragment, null, " ", /*#__PURE__*/React.createElement(CiteRef, {
    n: p.cite
  })) : null)))));
}
function EconomySection() {
  return /*#__PURE__*/React.createElement(Section, {
    number: "9",
    title: "Economy: Vendors as Supply Nodes",
    id: "s-9"
  }, /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, /*#__PURE__*/React.createElement(Named, {
    tier: 3
  }, "Vendor restock economy"), " proposes that selling to an NPC vendor stocks that vendor's inventory rather than deleting the item and conjuring gold from nowhere. Vendor shelves reflect what has actually been sold locally, and they can run dry.")), /*#__PURE__*/React.createElement("div", {
    className: "claimgrid"
  }, /*#__PURE__*/React.createElement("div", {
    className: "claim"
  }, /*#__PURE__*/React.createElement(DataField, {
    label: "Produces",
    value: "Real regional shortages"
  }), /*#__PURE__*/React.createElement("p", null, "If nobody has been supplying flux in Ironforge, Ironforge runs low on flux. Emergent commerce created by nothing more than a stock counter.")), /*#__PURE__*/React.createElement("div", {
    className: "claim"
  }, /*#__PURE__*/React.createElement(DataField, {
    label: "Produces",
    value: "A load-bearing trade network"
  }), /*#__PURE__*/React.createElement("p", null, "Sections 2 and 3 become economically necessary rather than decorative the moment goods have to physically move to rebalance supply.")), /*#__PURE__*/React.createElement("div", {
    className: "claim"
  }, /*#__PURE__*/React.createElement(DataField, {
    label: "Produces",
    value: "A floor under the player economy"
  }), /*#__PURE__*/React.createElement("p", null, "The auction house keeps finished and rare goods. Raw materials route through vendors, so a new player has baseline supply on a thin server."))), /*#__PURE__*/React.createElement(Note, {
    label: "Failure mode",
    accent: 3
  }, "A large guild or gold farmer floods one vendor to crash local prices, or starves one to manufacture a shortage. The mitigation is a soft cap: a vendor pays well for the first N of an item per day, then its buy price drops sharply. Tuned per item category, not globally."));
}
function TiersSection({
  tiers
}) {
  return /*#__PURE__*/React.createElement("section", {
    className: "section",
    id: "s-10"
  }, /*#__PURE__*/React.createElement(SectionHeading, {
    number: "10",
    title: "Implementation Tiers and Rollout",
    level: 2
  }), /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "These proposals are not equally expensive, and more importantly they are not equally reversible. A live-service game can patch in animation work indefinitely. It cannot casually retrofit a new economic model onto a server that has been running for eight months on the old one.")), /*#__PURE__*/React.createElement("div", {
    className: "tiergrid"
  }, tiers.map(t => /*#__PURE__*/React.createElement("article", {
    className: "tiercard",
    key: t.id,
    style: {
      borderTopColor: "var(--tier-" + t.id + ")"
    }
  }, /*#__PURE__*/React.createElement(TierBadge, {
    tier: t.id
  }), /*#__PURE__*/React.createElement("h4", null, t.name), /*#__PURE__*/React.createElement("p", {
    className: "tiercard__short"
  }, t.short), /*#__PURE__*/React.createElement("p", {
    className: "tiercard__desc"
  }, t.description)))), /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "The fresh-realm-as-testbed model resolves the Tier 3 problem cleanly, and Blizzard has already run the play with Season of Discovery ", /*#__PURE__*/React.createElement(CiteRef, {
    n: 5
  }), ". Launch Tier 3 changes only on a new realm, run Tier 1 and Tier 2 as ongoing content, and fold forward what the originating realm's players actually want.")));
}
function DocumentBody({
  part,
  data
}) {
  if (part === "opening") return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(StatusSection, null), /*#__PURE__*/React.createElement(AmbientSection, null), /*#__PURE__*/React.createElement(RoadsSection, null));
  if (part === "trade") return /*#__PURE__*/React.createElement(TradeSection, null);
  if (part === "ecology") return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(EcologySection, null), /*#__PURE__*/React.createElement(MiddleTierSection, null));
  if (part === "loot") return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(LootSection, null), /*#__PURE__*/React.createElement(ProfessionsSection, null), /*#__PURE__*/React.createElement(EconomySection, null));
  return /*#__PURE__*/React.createElement(TiersSection, {
    tiers: data.meta.tiers
  });
}
Object.assign(window, {
  DocumentBody
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/living-azeroth/DocumentBody.jsx", error: String((e && e.message) || e) }); }

// ui_kits/living-azeroth/Hero.jsx
try { (() => {
const {
  InterlockSpine
} = window.ALivingAzerothDesignSystem_623682;
const FRAGMENT = ["npc-idle-behavior", "woodcutting", "cart-caravan-routes", "craftable-vendor-goods", "vendor-restock-economy", "trade-network-stock"];
function Hero({
  data
}) {
  const frag = data.proposals.filter(p => FRAGMENT.includes(p.id));
  return /*#__PURE__*/React.createElement("header", {
    className: "hero",
    id: "top"
  }, /*#__PURE__*/React.createElement("div", {
    className: "hero__text"
  }, /*#__PURE__*/React.createElement("span", {
    className: "eyebrow"
  }, data.meta.subtitle, " \xA0\xB7\xA0 Version ", data.meta.version, " \xA0\xB7\xA0 ", data.meta.date), /*#__PURE__*/React.createElement("h1", null, "A Living Azeroth"), /*#__PURE__*/React.createElement("p", {
    className: "hero__thesis"
  }, "Vanilla asserts things in quest text that the world never shows. The Kolkar are breaking through Horde lines. Venture is stripping Stonetalon bare. Steamwheedle and Venture are in open commercial war. The camps face each other and nothing happens."), /*#__PURE__*/React.createElement("p", {
    className: "hero__sub"
  }, "Twenty-eight proposals for world texture, each anchored to a named vanilla location and sorted by how deeply it touches the game's architecture."), /*#__PURE__*/React.createElement("div", {
    className: "hero__meta"
  }, /*#__PURE__*/React.createElement("span", null, "28 proposals"), /*#__PURE__*/React.createElement("span", null, "10 sections"), /*#__PURE__*/React.createElement("span", null, "3 appendices"), /*#__PURE__*/React.createElement("span", null, "~8,000 words"))), /*#__PURE__*/React.createElement("figure", {
    className: "hero__spine panel"
  }, /*#__PURE__*/React.createElement(InterlockSpine, {
    proposals: frag,
    columns: 2,
    showOrphans: false
  }), /*#__PURE__*/React.createElement("figcaption", null, "A fragment of the interlock spine. Logging feeds the cart route, which feeds vendor restock, which feeds the trade network.")));
}
Object.assign(window, {
  Hero
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/living-azeroth/Hero.jsx", error: String((e && e.message) || e) }); }

// ui_kits/living-azeroth/ProposalBrowser.jsx
try { (() => {
const {
  ProposalTable,
  FilterChip,
  SearchInput,
  Select,
  Button,
  SectionHeading,
  Prose
} = window.ALivingAzerothDesignSystem_623682;
const SYSTEMS = ["Ambient life", "Traversal", "Trade", "Economy", "Ecology", "Loot", "Professions", "Emergent conflict", "Exploration", "Art"];
const COSTS = ["low", "medium", "high"];
function ProposalBrowser({
  data,
  highlightIds,
  onClearHighlight
}) {
  const [tiers, setTiers] = React.useState([]);
  const [systems, setSystems] = React.useState([]);
  const [cost, setCost] = React.useState("all");
  const [q, setQ] = React.useState("");
  React.useEffect(() => {
    const p = new URLSearchParams(location.search);
    if (tiers.length) p.set("tier", tiers.join(","));else p.delete("tier");
    if (systems.length) p.set("system", systems.join(","));else p.delete("system");
    if (cost !== "all") p.set("cost", cost);else p.delete("cost");
    if (q) p.set("q", q);else p.delete("q");
    history.replaceState(null, "", location.pathname + (p.toString() ? "?" + p : "") + location.hash);
  }, [tiers, systems, cost, q]);
  const toggle = (list, set, v) => set(list.includes(v) ? list.filter(x => x !== v) : list.concat(v));
  const filtered = data.proposals.filter(p => {
    if (tiers.length && !tiers.includes(p.tier)) return false;
    if (systems.length && !p.systems.some(s => systems.includes(s))) return false;
    if (cost !== "all" && p.cost !== cost) return false;
    if (q) {
      const hay = [p.title, p.note, p.zones.join(" "), p.factions.join(" "), p.systems.join(" ")].join(" ").toLowerCase();
      if (!hay.includes(q.toLowerCase())) return false;
    }
    return true;
  });
  const count = fn => data.proposals.filter(fn).length;
  const dirty = tiers.length || systems.length || cost !== "all" || q;
  return /*#__PURE__*/React.createElement("section", {
    className: "section view",
    id: "v-browser"
  }, /*#__PURE__*/React.createElement(SectionHeading, {
    number: "Interactive view",
    title: "Proposal browser",
    level: 2
  }), /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "All 28 proposals, filterable and sortable. Rows expand to the implementation note and the dependency edges. Filters are written into the URL, so a filtered view can be shared as-is.")), /*#__PURE__*/React.createElement("div", {
    className: "filters"
  }, /*#__PURE__*/React.createElement("div", {
    className: "filters__row"
  }, /*#__PURE__*/React.createElement("span", {
    className: "filters__label"
  }, "Tier"), [1, 2, 3].map(t => /*#__PURE__*/React.createElement(FilterChip, {
    key: t,
    label: "Tier " + t,
    tier: t,
    count: count(p => p.tier === t),
    pressed: tiers.includes(t),
    onToggle: () => toggle(tiers, setTiers, t)
  }))), /*#__PURE__*/React.createElement("div", {
    className: "filters__row"
  }, /*#__PURE__*/React.createElement("span", {
    className: "filters__label"
  }, "System"), SYSTEMS.map(s => /*#__PURE__*/React.createElement(FilterChip, {
    key: s,
    label: s,
    count: count(p => p.systems.includes(s)),
    pressed: systems.includes(s),
    onToggle: () => toggle(systems, setSystems, s)
  }))), /*#__PURE__*/React.createElement("div", {
    className: "filters__row filters__row--controls"
  }, /*#__PURE__*/React.createElement(Select, {
    label: "Cost",
    value: cost,
    options: ["all"].concat(COSTS),
    onChange: setCost
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: "1 1 240px",
      maxWidth: 320,
      alignSelf: "flex-end"
    }
  }, /*#__PURE__*/React.createElement(SearchInput, {
    value: q,
    onChange: setQ,
    placeholder: "Search title, zone, faction"
  })), dirty ? /*#__PURE__*/React.createElement("span", {
    style: {
      alignSelf: "flex-end"
    }
  }, /*#__PURE__*/React.createElement(Button, {
    onClick: () => {
      setTiers([]);
      setSystems([]);
      setCost("all");
      setQ("");
    }
  }, "Clear filters")) : null, highlightIds ? /*#__PURE__*/React.createElement("span", {
    style: {
      alignSelf: "flex-end"
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "quiet",
    onClick: onClearHighlight
  }, "Clear spine focus")) : null)), /*#__PURE__*/React.createElement(ProposalTable, {
    proposals: filtered,
    caption: filtered.length + " of " + data.proposals.length + " proposals",
    highlightIds: highlightIds,
    emptyHint: "Remove a tier or system filter, or clear the search field."
  }));
}
Object.assign(window, {
  ProposalBrowser
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/living-azeroth/ProposalBrowser.jsx", error: String((e && e.message) || e) }); }

// ui_kits/living-azeroth/SpineView.jsx
try { (() => {
const {
  InterlockSpine,
  SectionHeading,
  Prose,
  Button
} = window.ALivingAzerothDesignSystem_623682;

/* What physically moves along each cargo edge. Named from the document, not invented. */
const CARGO = {
  "woodcutting>cart-caravan-routes": "lumber",
  "cart-caravan-routes>vendor-restock-economy": "haulage",
  "craftable-vendor-goods>vendor-restock-economy": "thread, flux, vials",
  "vendor-restock-economy>trade-network-stock": "stock levels",
  "cart-caravan-routes>trade-network-stock": "ore and lumber",
  "cart-caravan-routes>regional-cooking": "spices, plains game"
};

/* Columns are chosen from the measured panel width so the tree never scrolls:
   HEAD 140 + columns x 128 + 16 has to fit. */
function SpineView({
  data,
  activeId,
  onSelect
}) {
  const wrap = React.useRef(null);
  const [cols, setCols] = React.useState(5);
  React.useEffect(() => {
    const fit = () => {
      const w = wrap.current ? wrap.current.clientWidth : 940;
      setCols(Math.max(2, Math.min(5, Math.floor((w - 156 - 16) / 128))));
    };
    fit();
    const ro = new ResizeObserver(fit);
    if (wrap.current) ro.observe(wrap.current);
    return () => ro.disconnect();
  }, []);
  return /*#__PURE__*/React.createElement("section", {
    className: "section view view--wide",
    id: "v-spine"
  }, /*#__PURE__*/React.createElement(SectionHeading, {
    number: "Interactive view",
    title: "The interlock spine",
    level: 2
  }), /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "The graph is drawn as a vanilla talent tree, because that is structurally what it is: tiers as rows, dependency arrows between nodes, and a counter on each node for how much rides on it. Every edge in the data runs Tier 1 to Tier 2, Tier 2 to Tier 3, or stays flat within a tier. Not one runs backward, which is the argument of Section 10 stated as a drawing: cheap behavioral work is what makes the expensive architectural work viable."), /*#__PURE__*/React.createElement("p", null, "Tiers run top to bottom. Every arrow in the data runs Tier 1 to Tier 2, Tier 2 to Tier 3, or stays flat inside a tier, and none run backward, which is Section 10's argument stated as a drawing. Arrow weight is downstream reach, so the trunk emerges on its own: extraction into haulage, haulage into exchange, exchange into stock. Click a node to focus it and its neighbours in the browser below.")), /*#__PURE__*/React.createElement("div", {
    className: "spinewrap panel",
    ref: wrap
  }, /*#__PURE__*/React.createElement("div", {
    className: "spinewrap__scroll"
  }, /*#__PURE__*/React.createElement(InterlockSpine, {
    proposals: data.proposals,
    activeId: activeId,
    columns: cols,
    edgeLabels: CARGO,
    onSelect: onSelect
  })), /*#__PURE__*/React.createElement("div", {
    className: "spinelegend"
  }, /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("svg", {
    width: "34",
    height: "10"
  }, /*#__PURE__*/React.createElement("path", {
    d: "M1 5h32",
    stroke: "var(--spine-line)",
    strokeWidth: "3.5",
    fill: "none",
    strokeLinecap: "round"
  })), "Carries cargo"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("svg", {
    width: "34",
    height: "10"
  }, /*#__PURE__*/React.createElement("path", {
    d: "M1 5h32",
    stroke: "var(--spine-line)",
    strokeWidth: "1",
    strokeDasharray: "3 4",
    opacity: ".55",
    fill: "none"
  })), "Makes possible"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("i", {
    style: {
      background: "var(--tier-1)"
    }
  }), "Tier 1"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("i", {
    style: {
      background: "var(--tier-2)"
    }
  }), "Tier 2"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("i", {
    style: {
      background: "var(--tier-3)"
    }
  }), "Tier 3"), activeId ? /*#__PURE__*/React.createElement(Button, {
    size: "sm",
    variant: "quiet",
    onClick: () => onSelect(null, null)
  }, "Clear focus") : null)), /*#__PURE__*/React.createElement("p", {
    className: "spinelegend__hint"
  }, "Cargo edges are weighted by how much depends on their source and labelled with what moves along them. Behavior edges mean \"makes possible\" and carry nothing, so they are drawn thin and dashed. Node identifiers are the document's own section numbers, and the counter is how many proposals depend on that node downstream."));
}
Object.assign(window, {
  SpineView
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/living-azeroth/SpineView.jsx", error: String((e && e.message) || e) }); }

// ui_kits/living-azeroth/ZoneView.jsx
try { (() => {
const {
  ZonePicker,
  SectionHeading,
  Prose,
  TierBadge,
  DataField,
  EmptyState
} = window.ALivingAzerothDesignSystem_623682;
function zoneIndex(proposals) {
  const m = new Map();
  proposals.forEach(p => p.zones.forEach(z => m.set(z, (m.get(z) || 0) + 1)));
  return Array.from(m, ([name, count]) => ({
    name,
    count
  })).sort((a, b) => b.count - a.count || a.name.localeCompare(b.name));
}
function ZoneView({
  data
}) {
  const zones = React.useMemo(() => zoneIndex(data.proposals), [data]);
  const [zone, setZone] = React.useState("The Barrens");
  const hits = zone ? data.proposals.filter(p => p.zones.includes(zone)) : [];
  const factions = Array.from(new Set(hits.flatMap(p => p.factions)));
  return /*#__PURE__*/React.createElement("section", {
    className: "section view",
    id: "v-zone"
  }, /*#__PURE__*/React.createElement(SectionHeading, {
    number: "Interactive view",
    title: "Zone view",
    level: 2
  }), /*#__PURE__*/React.createElement(Prose, null, /*#__PURE__*/React.createElement("p", null, "The document is organised by system. The content is organised by geography. Pick a zone to see every proposal that touches it, which is information the prose does not carry anywhere.")), /*#__PURE__*/React.createElement(ZonePicker, {
    zones: zones,
    value: zone,
    onChange: setZone
  }), !zone ? /*#__PURE__*/React.createElement(EmptyState, {
    title: "No zone selected",
    hint: "Pick a zone above to list the proposals that touch it."
  }) : /*#__PURE__*/React.createElement("div", {
    className: "zonebody"
  }, /*#__PURE__*/React.createElement("div", {
    className: "zonebody__head"
  }, /*#__PURE__*/React.createElement("h3", null, zone), /*#__PURE__*/React.createElement("div", {
    className: "zonebody__meta"
  }, /*#__PURE__*/React.createElement(DataField, {
    label: "Proposals",
    value: String(hits.length)
  }), /*#__PURE__*/React.createElement(DataField, {
    label: "Tiers",
    value: Array.from(new Set(hits.map(p => p.tier))).sort().map(t => "T" + t).join(", ")
  }), /*#__PURE__*/React.createElement(DataField, {
    label: "Factions",
    value: factions.length ? factions.join(", ") : "\u2014"
  }))), /*#__PURE__*/React.createElement("ul", {
    className: "zonelist"
  }, hits.sort((a, b) => a.tier - b.tier).map(p => /*#__PURE__*/React.createElement("li", {
    key: p.id
  }, /*#__PURE__*/React.createElement("div", {
    className: "zonelist__top"
  }, /*#__PURE__*/React.createElement(TierBadge, {
    tier: p.tier,
    variant: "bare",
    size: "sm",
    label: "T" + p.tier
  }), /*#__PURE__*/React.createElement("span", {
    className: "zonelist__title"
  }, p.title), /*#__PURE__*/React.createElement("span", {
    className: "zonelist__sec"
  }, p.section)), /*#__PURE__*/React.createElement("p", {
    className: "zonelist__note"
  }, p.note))))));
}
Object.assign(window, {
  ZoneView
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/living-azeroth/ZoneView.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Button = __ds_scope.Button;

__ds_ns.FilterChip = __ds_scope.FilterChip;

__ds_ns.SearchInput = __ds_scope.SearchInput;

__ds_ns.Select = __ds_scope.Select;

__ds_ns.EmptyState = __ds_scope.EmptyState;

__ds_ns.InterlockSpine = __ds_scope.InterlockSpine;

__ds_ns.ProposalTable = __ds_scope.ProposalTable;

__ds_ns.ProposalTooltip = __ds_scope.ProposalTooltip;

__ds_ns.ZonePicker = __ds_scope.ZonePicker;

__ds_ns.CiteRef = __ds_scope.CiteRef;

__ds_ns.DataField = __ds_scope.DataField;

__ds_ns.Note = __ds_scope.Note;

__ds_ns.Prose = __ds_scope.Prose;

__ds_ns.SectionHeading = __ds_scope.SectionHeading;

__ds_ns.TierBadge = __ds_scope.TierBadge;

__ds_ns.DocFooter = __ds_scope.DocFooter;

__ds_ns.SidebarTOC = __ds_scope.SidebarTOC;

})();
