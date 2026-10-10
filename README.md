# Privacy Redaction Gateway

A local text-redaction pipeline with overlap handling, stable in-request placeholders, and audit counts.

**Status:** runnable portfolio reference implementation. Uses synthetic or hand-authored demonstration data. No employer code, customer data, or production performance claims.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
python -m unittest -v
```

The default command prints a reproducible JSON demonstration. See `app.py` for the reusable Python API. `example-output.json` records the locally executed demo; it is not an external benchmark.

## Architecture

Input text → regex candidates → card checksum → overlap resolution → per-request placeholders → counts-only audit. All processing is local.

## Validation

Tests exercise failure cases and behavioral invariants, in addition to the executable demo. The included `github-actions-tests.yml` defines tests and the demo on pushes and pull requests. Install it as `.github/workflows/tests.yml` to activate CI. CI has not run on GitHub until this repository is published.

## Limitations and next steps

Pattern matching is incomplete and may produce false positives. It misses names, addresses, non-US phone formats, obfuscation, and context-dependent sensitive information. This is not a compliance guarantee or complete DLP system. Add entity models and adversarial multilingual evaluation.

## Container

```bash
docker build -t privacy-redaction-gateway .
docker run --rm privacy-redaction-gateway
```

The Docker recipe is provided; local validation uses Python, not Docker.

## Responsible use

Review the code and understand its assumptions before deploying. Keep credentials in environment variables and exclude private data from commits. This project is an educational engineering baseline, not a production-certified service.
