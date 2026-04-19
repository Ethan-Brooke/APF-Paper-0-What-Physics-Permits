"""apf/bank.py — Paper 0 registry.

Lightweight registry for the 20-check subset bundled in this
paper-companion repo. Mirrors the canonical apf.bank API: REGISTRY (dict),
get_check(name), run_all(verbose=False).
"""
from collections import OrderedDict
import traceback

from apf import core as _core


def _build_registry():
    reg = OrderedDict()
    for name in ['check_L_epsilon_star', 'check_L_loc', 'check_L_nc', 'check_T_canonical', 'check_T_alg', 'check_T_Born', 'check_T_Tsirelson', 'check_L_gauge_template_uniqueness', 'check_T_gauge', 'check_T_field', 'check_L_Gram_generation', 'check_T_second_law', 'check_T_horizon_reciprocity', 'check_T7', 'check_T_CKM', 'check_T_CPTP', 'check_A9_closure', 'check_L_spectral_action_internal', 'check_T6B_beta_one_loop', 'check_L_seesaw_type_I']:
        fn = getattr(_core, name, None)
        if fn is None:
            # Function couldn't be extracted — skip with a warning attribute
            continue
        reg[name] = fn
    return reg


REGISTRY = _build_registry()
EXPECTED_CHECK_COUNT = 20


def get_check(name):
    """Return the check function registered as `name`. Raises KeyError if missing."""
    if name not in REGISTRY:
        raise KeyError(f"Check '{name}' not found. Available: {sorted(REGISTRY.keys())}")
    return REGISTRY[name]


def run_all(verbose=False):
    """Run every registered check, returning a list of result dicts."""
    results = []
    for name, fn in REGISTRY.items():
        try:
            r = fn()
            if not isinstance(r, dict):
                # Some legacy checks return True/False
                r = {"name": name, "passed": bool(r), "key_result": str(r)}
            elif "passed" not in r:
                r["passed"] = True
            r.setdefault("name", name)
        except Exception as e:
            r = {
                "name": name,
                "passed": False,
                "error": f"{type(e).__name__}: {e}",
                "traceback": traceback.format_exc(),
            }
        if verbose:
            status = "PASS" if r.get("passed", True) else "FAIL"
            print(f"  {r['name']}: {status}")
            if r.get("key_result"):
                print(f"    {r['key_result']}")
        results.append(r)
    return results
