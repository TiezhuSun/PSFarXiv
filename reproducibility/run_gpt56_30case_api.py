#!/usr/bin/env python3
"""
GPT-5.6 Sol — 30-case PSF blind pilot runner.

Examples:
  pip install -U openai python-docx
  export OPENAI_API_KEY="..."
  python run_gpt56_30case_api.py --preflight-only
  python run_gpt56_30case_api.py --run 1
  python run_gpt56_30case_api.py --run all

Default total script-level spend cap across all 3 runs: $12.50.
Override with --max-spend-usd or OPENAI_MAX_SPEND_USD.

IMPORTANT:
- One case = one stateless Responses API call.
- No web/tools.
- No automatic generation retries. A transport exception stops execution because a lost
  response could still have been billed, and retrying would weaken the spend cap.
"""
import argparse, json, os, sys, math
from datetime import datetime, timezone
from pathlib import Path

from psf_api_common import *

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-sol")
OUT_ROOT = HERE / "gpt56_api_results"
PROMPT_CACHE_KEY = "psf-30case-v1.1-manual-v0.2"

def output_format(schema):
    return {
        "type": "json_schema",
        "name": "psf_coding",
        "strict": True,
        "schema": schema,
    }

def exact_input_count(client, instructions, prompt, schema):
    # Uses OpenAI's Responses input-token counting endpoint.
    r = client.responses.input_tokens.count(
        model=MODEL,
        instructions=instructions,
        input=prompt,
        reasoning={"effort": EFFORT},
        text={"format": output_format(schema)},
    )
    return int(r.input_tokens)

def fallback_input_count(instructions, prompt, schema):
    # OpenAI's published rough English estimate is ~1 token / 4 chars.
    # Add 35% safety margin because JSON/XML/schema overhead can tokenize differently.
    chars = len(instructions) + len(prompt) + len(json.dumps(schema, separators=(",",":")))
    return math.ceil((chars / 4.0) * 1.35)

def preflight(client, instructions, schema, cases, manifests):
    counts = {}
    for cid in sorted(cases):
        prompt = make_user_prompt(cases[cid])
        try:
            counts[cid] = exact_input_count(client, instructions, prompt, schema)
        except Exception as e:
            counts[cid] = fallback_input_count(instructions, prompt, schema)
            print(f"WARNING: exact token count failed for {cid}; using conservative fallback: {e}", file=sys.stderr)

    one_run = sum(counts.values())
    all_runs = one_run * 3
    expected_out = 30 * 3 * 1100
    conservative_out = 30 * 3 * 1800
    max_out = 30 * 3 * MAX_OUTPUT_TOKENS
    p = OPENAI_PRICING
    report = {
        "provider": "OpenAI",
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
        "theoretical_all_input_cache_write_plus_max_output_usd":
            all_runs*p["cache_write"]/1e6 + max_out*p["output"]/1e6,
        "default_script_spend_cap_usd": DEFAULT_OPENAI_SPEND_CAP_USD,
        "note": "Actual cost can be lower through prompt caching. Output-token projections are assumptions; reasoning tokens are included in billed output.",
    }
    (HERE / "openai_preflight_cost.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report

def usage_fields(resp):
    u = resp.usage
    details = getattr(u, "input_tokens_details", None)
    out_details = getattr(u, "output_tokens_details", None)
    return {
        "input_tokens": int(getattr(u, "input_tokens", 0) or 0),
        "cached_tokens": int(getattr(details, "cached_tokens", 0) or 0) if details else 0,
        "cache_write_tokens": int(getattr(details, "cache_write_tokens", 0) or 0) if details else 0,
        "output_tokens": int(getattr(u, "output_tokens", 0) or 0),
        "reasoning_tokens": int(getattr(out_details, "reasoning_tokens", 0) or 0) if out_details else 0,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", choices=["1","2","3","all"], default="all")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--max-spend-usd", type=float,
                        default=float(os.getenv("OPENAI_MAX_SPEND_USD", DEFAULT_OPENAI_SPEND_CAP_USD)))
    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set.")

    try:
        from openai import OpenAI
    except ImportError as e:
        raise SystemExit("Install dependency: pip install -U openai python-docx") from e

    manual, corpus, manifests, schema, cases = load_inputs()
    instructions = make_openai_instructions(manual)
    client = OpenAI(max_retries=0)

    report = preflight(client, instructions, schema, cases, manifests)
    print(json.dumps({
        "model": MODEL,
        "input_tokens_three_runs": report["input_tokens_three_runs"],
        "projected_cost_usd_no_cache": report["projected_cost_usd_no_cache"],
        "theoretical_all_input_cache_write_plus_max_output_usd":
            report["theoretical_all_input_cache_write_plus_max_output_usd"],
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
                print(f"[GPT run {run_num} {idx:02d}/30] {cid}: exists, skip")
                continue

            spent = existing_spend_usd(OUT_ROOT)
            prompt = make_user_prompt(cases[cid])
            try:
                input_count = exact_input_count(client, instructions, prompt, schema)
            except Exception:
                input_count = fallback_input_count(instructions, prompt, schema)

            reserve = openai_next_call_worst_case(input_count)
            if spent + reserve > args.max_spend_usd:
                stop = {
                    "status": "SPEND_CAP_STOP",
                    "provider": "OpenAI",
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

            print(f"[GPT run {run_num} {idx:02d}/30] {cid} | spent=${spent:.4f} | reserve=${reserve:.4f}")
            try:
                resp = client.responses.create(
                    model=MODEL,
                    instructions=instructions,
                    input=prompt,
                    reasoning={"effort": EFFORT},
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                    text={"format": output_format(schema)},
                    store=False,
                    prompt_cache_key=PROMPT_CACHE_KEY,
                )
            except Exception as e:
                fail = {
                    "status": "API_EXCEPTION_STOPPED_NO_RETRY",
                    "run_id": f"gpt56_run_{run_num}",
                    "case_id": cid,
                    "error": repr(e),
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                    "warning": "Execution stopped because a lost response might still have been billed.",
                }
                (run_dir / f"{cid}.failure.json").write_text(json.dumps(fail, indent=2), encoding="utf-8")
                raise

            usage = usage_fields(resp)
            cost = openai_actual_cost(
                usage["input_tokens"], usage["cached_tokens"],
                usage["cache_write_tokens"], usage["output_tokens"]
            )
            raw = resp.output_text or ""
            coding = None
            parse_error = None
            try:
                coding = parse_json_text(raw)
            except Exception as e:
                parse_error = repr(e)

            errors, warnings = (["JSON parse failed: "+str(parse_error)], []) if coding is None else validate_result(coding, cases[cid])
            api_complete = getattr(resp, "status", None) == "completed"
            status = "VALID" if api_complete and coding is not None and not errors else (
                "INCOMPLETE" if not api_complete else "INVALID"
            )

            rec = {
                "status": status,
                "provider": "OpenAI",
                "run_id": f"gpt56_run_{run_num}",
                "case_id": cid,
                "coding": coding,
                "validation_errors": errors,
                "validation_warnings": warnings,
                "api_meta": {
                    "model_requested": MODEL,
                    "model_returned": getattr(resp, "model", None),
                    "response_status": getattr(resp, "status", None),
                    "incomplete_details": str(getattr(resp, "incomplete_details", None)),
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
                    "prompt_sha256": sha256_text(instructions + "\n" + prompt),
                },
            }
            out_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"  {status} | cost=${cost:.4f} | output={usage['output_tokens']} | reasoning={usage['reasoning_tokens']}")

    total = existing_spend_usd(OUT_ROOT)
    print(f"Recorded GPT spend: ${total:.4f} / cap ${args.max_spend_usd:.2f}")

if __name__ == "__main__":
    main()
