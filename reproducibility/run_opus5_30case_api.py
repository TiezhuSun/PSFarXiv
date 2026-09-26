#!/usr/bin/env python3
"""
Claude Opus 5 — 30-case PSF blind pilot runner.

Examples:
  pip install -U anthropic python-docx
  export ANTHROPIC_API_KEY="..."
  python run_opus5_30case_api.py --preflight-only
  python run_opus5_30case_api.py --run 1
  python run_opus5_30case_api.py --run all

Default total script-level spend cap across all 3 runs: $15.00.
The Manual is explicitly cached with a 1-hour TTL.

No automatic generation retries: on an API exception, execution stops because a
lost response might still have been billed.
"""
import argparse, json, os, sys, math
from datetime import datetime, timezone

from psf_api_common import *

MODEL = os.getenv("ANTHROPIC_MODEL", "claude-opus-5")
OUT_ROOT = HERE / "opus5_api_results"

def exact_input_count(client, system_blocks, prompt, schema):
    r = client.messages.count_tokens(
        model=MODEL,
        system=system_blocks,
        messages=[{"role":"user","content":prompt}],
        output_config={
            "effort": EFFORT,
            "format": {"type":"json_schema","schema":schema},
        },
    )
    return int(r.input_tokens)

def fallback_input_count(system_blocks, prompt, schema):
    chars = sum(len(x.get("text","")) for x in system_blocks) + len(prompt) + len(json.dumps(schema, separators=(",",":")))
    # Calibrated from the previous Opus 5 experiment: 17,508 input tokens / 49,190 prompt chars.
    return math.ceil(chars * (17508 / 49190) * 1.15)

def preflight(client, system_blocks, schema, cases):
    counts = {}
    for cid in sorted(cases):
        prompt = make_user_prompt(cases[cid])
        try:
            counts[cid] = exact_input_count(client, system_blocks, prompt, schema)
        except Exception as e:
            counts[cid] = fallback_input_count(system_blocks, prompt, schema)
            print(f"WARNING: exact token count failed for {cid}; using conservative fallback: {e}", file=sys.stderr)

    one_run = sum(counts.values())
    all_runs = one_run * 3
    expected_out = 90 * 1100
    conservative_out = 90 * 1800
    max_out = 90 * MAX_OUTPUT_TOKENS
    p = ANTHROPIC_PRICING
    report = {
        "provider": "Anthropic",
        "model": MODEL,
        "pricing_snapshot": "2026-09-17",
        "input_token_count_by_case": counts,
        "input_tokens_one_run": one_run,
        "input_tokens_three_runs": all_runs,
        "output_assumptions": {
            "expected_per_case": 1100,
            "conservative_per_case": 1800,
            "hard_request_cap_per_case": MAX_OUTPUT_TOKENS,
        },
        "projected_cost_usd_no_cache": {
            "expected": all_runs*p["input"]/1e6 + expected_out*p["output"]/1e6,
            "conservative": all_runs*p["input"]/1e6 + conservative_out*p["output"]/1e6,
            "all_calls_hit_max_output": all_runs*p["input"]/1e6 + max_out*p["output"]/1e6,
        },
        "theoretical_all_input_1h_cache_write_plus_max_output_usd":
            all_runs*p["cache_write_1h"]/1e6 + max_out*p["output"]/1e6,
        "default_script_spend_cap_usd": DEFAULT_ANTHROPIC_SPEND_CAP_USD,
        "note": "Actual cost should usually be lower because the manual uses explicit 1h caching. Token-count endpoint itself is free per Anthropic docs.",
    }
    (HERE / "anthropic_preflight_cost.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report

def usage_fields(message):
    u = message.usage
    creation = getattr(u, "cache_creation", None)
    return {
        "input_tokens": int(getattr(u, "input_tokens", 0) or 0),
        "cache_read_input_tokens": int(getattr(u, "cache_read_input_tokens", 0) or 0),
        "cache_creation_input_tokens": int(getattr(u, "cache_creation_input_tokens", 0) or 0),
        "cache_creation_5m_tokens": int(getattr(creation, "ephemeral_5m_input_tokens", 0) or 0) if creation else 0,
        "cache_creation_1h_tokens": int(getattr(creation, "ephemeral_1h_input_tokens", 0) or 0) if creation else 0,
        "output_tokens": int(getattr(u, "output_tokens", 0) or 0),
        "thinking_tokens": int(getattr(getattr(u, "output_tokens_details", None), "thinking_tokens", 0) or 0),
    }

def response_text(message):
    return "\n".join(
        block.text for block in message.content
        if getattr(block, "type", None) == "text"
    ).strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", choices=["1","2","3","all"], default="all")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--max-spend-usd", type=float,
                        default=float(os.getenv("ANTHROPIC_MAX_SPEND_USD", DEFAULT_ANTHROPIC_SPEND_CAP_USD)))
    args = parser.parse_args()

    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit("ANTHROPIC_API_KEY is not set.")

    try:
        import anthropic
    except ImportError as e:
        raise SystemExit("Install dependency: pip install -U anthropic python-docx") from e

    manual, corpus, manifests, schema, cases = load_inputs()
    system_blocks = make_anthropic_system(manual)
    client = anthropic.Anthropic(max_retries=0)

    report = preflight(client, system_blocks, schema, cases)
    print(json.dumps({
        "model": MODEL,
        "input_tokens_three_runs": report["input_tokens_three_runs"],
        "projected_cost_usd_no_cache": report["projected_cost_usd_no_cache"],
        "theoretical_all_input_1h_cache_write_plus_max_output_usd":
            report["theoretical_all_input_1h_cache_write_plus_max_output_usd"],
        "script_spend_cap_usd": args.max_spend_usd,
    }, indent=2))
    if args.preflight_only:
        return

    OUT_ROOT.mkdir(exist_ok=True)
    runs = [1,2,3] if args.run == "all" else [int(args.run)]

    for run_num in runs:
        run_dir = OUT_ROOT / f"run_{run_num}"
        run_dir.mkdir(parents=True, exist_ok=True)
        order = manifests[f"run_{run_num}"]["order"]

        for idx,cid in enumerate(order, start=1):
            out_path = run_dir / f"{cid}.json"
            if out_path.exists():
                print(f"[Opus run {run_num} {idx:02d}/30] {cid}: exists, skip")
                continue

            spent = existing_spend_usd(OUT_ROOT)
            prompt = make_user_prompt(cases[cid])
            try:
                input_count = exact_input_count(client, system_blocks, prompt, schema)
            except Exception:
                input_count = fallback_input_count(system_blocks, prompt, schema)

            reserve = anthropic_next_call_worst_case(input_count)
            if spent + reserve > args.max_spend_usd:
                stop = {
                    "status": "SPEND_CAP_STOP",
                    "provider": "Anthropic",
                    "model": MODEL,
                    "spent_recorded_usd": spent,
                    "next_call_worst_case_usd": reserve,
                    "max_spend_usd": args.max_spend_usd,
                    "next_case": cid,
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                }
                (OUT_ROOT / "SPEND_CAP_STOP.json").write_text(json.dumps(stop, indent=2), encoding="utf-8")
                raise SystemExit(
                    f"Spend cap stop before {cid}: recorded ${spent:.4f} + "
                    f"next worst ${reserve:.4f} > cap ${args.max_spend_usd:.2f}"
                )

            print(f"[Opus run {run_num} {idx:02d}/30] {cid} | spent=${spent:.4f} | reserve=${reserve:.4f}")
            try:
                message = client.messages.create(
                    model=MODEL,
                    max_tokens=MAX_OUTPUT_TOKENS,
                    system=system_blocks,
                    messages=[{"role":"user","content":prompt}],
                    output_config={
                        "effort": EFFORT,
                        "format": {"type":"json_schema","schema":schema},
                    },
                    service_tier="standard_only",
                )
            except Exception as e:
                fail = {
                    "status": "API_EXCEPTION_STOPPED_NO_RETRY",
                    "run_id": f"opus5_run_{run_num}",
                    "case_id": cid,
                    "error": repr(e),
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                    "warning": "Execution stopped because a lost response might still have been billed.",
                }
                (run_dir / f"{cid}.failure.json").write_text(json.dumps(fail, indent=2), encoding="utf-8")
                raise

            usage = usage_fields(message)
            # If an older SDK omits cache_creation breakdown, conservatively price all creation tokens as 1h.
            c5 = usage["cache_creation_5m_tokens"]
            c1 = usage["cache_creation_1h_tokens"]
            if usage["cache_creation_input_tokens"] and (c5 + c1 == 0):
                c1 = usage["cache_creation_input_tokens"]

            cost = anthropic_actual_cost(
                usage["input_tokens"], usage["cache_read_input_tokens"],
                c5, c1, usage["output_tokens"]
            )
            raw = response_text(message)
            coding = None
            parse_error = None
            try:
                coding = parse_json_text(raw)
            except Exception as e:
                parse_error = repr(e)

            errors, warnings = (["JSON parse failed: "+str(parse_error)], []) if coding is None else validate_result(coding, cases[cid])
            api_complete = getattr(message, "stop_reason", None) == "end_turn"
            status = "VALID" if api_complete and coding is not None and not errors else (
                "INCOMPLETE" if not api_complete else "INVALID"
            )

            rec = {
                "status": status,
                "provider": "Anthropic",
                "run_id": f"opus5_run_{run_num}",
                "case_id": cid,
                "coding": coding,
                "validation_errors": errors,
                "validation_warnings": warnings,
                "api_meta": {
                    "model_requested": MODEL,
                    "model_returned": getattr(message, "model", None),
                    "stop_reason": getattr(message, "stop_reason", None),
                    **usage,
                },
                "actual_cost_usd": cost,
                "spend_cap_usd": args.max_spend_usd,
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "provenance": {
                    "protocol_version": PROTOCOL_VERSION,
                    "prompt_version": PROMPT_VERSION,
                    "manual_sha256": sha256_path(MANUAL_PATH),
                    "corpus_sha256": sha256_path(CORPUS_PATH),
                    "manifest_sha256": sha256_path(MANIFEST_PATH),
                    "schema_sha256": sha256_path(SCHEMA_PATH),
                    "prompt_sha256": sha256_text(json.dumps(system_blocks, sort_keys=True) + "\n" + prompt),
                },
            }
            out_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"  {status} | cost=${cost:.4f} | output={usage['output_tokens']} | thinking={usage['thinking_tokens']}")

    total = existing_spend_usd(OUT_ROOT)
    print(f"Recorded Opus spend: ${total:.4f} / cap ${args.max_spend_usd:.2f}")

if __name__ == "__main__":
    main()
