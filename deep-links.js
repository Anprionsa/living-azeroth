// Deep links: the sections are built after load, so the browser's own jump to #s-7 lands before
// s-7 exists. Wait for it, scroll to it, and hold it in place while late content (data views,
// images) changes the height above it. Stop as soon as the reader scrolls or presses a key.
(function(){
  var held = true, settleTimer = null, observer = null;
  function release(){ held = false; if (observer) observer.disconnect(); clearTimeout(settleTimer); }
  ['wheel','touchstart','keydown','mousedown'].forEach(function(e){ addEventListener(e, release, {passive:true, once:true}); });
  function target(){
    var h = location.hash.slice(1);
    try { h = decodeURIComponent(h); } catch (e) { return null; }
    return h && /^[\w.:-]+$/.test(h) ? document.getElementById(h) : null;
  }
  function align(){ var el = target(); if (el && held) el.scrollIntoView({block:'start', behavior:'instant'}); return !!el; }
  function holdUntilSettled(){
    align();
    if (typeof ResizeObserver !== 'function') return;
    observer = new ResizeObserver(function(){ if (!held) return; align(); clearTimeout(settleTimer); settleTimer = setTimeout(release, 3000); });
    observer.observe(document.documentElement);
    settleTimer = setTimeout(release, 3000);
    setTimeout(release, 20000);
  }
  function start(){
    if (!location.hash) return;
    var tries = 0;
    (function wait(){ if (!held) return; if (target()) return holdUntilSettled(); if (++tries < 150) setTimeout(wait, 100); })();
  }
  addEventListener('hashchange', function(){ held = true; align(); held = false; });
  if (document.readyState === 'loading') addEventListener('DOMContentLoaded', start); else start();
})();
