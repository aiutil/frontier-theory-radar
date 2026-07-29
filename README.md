# Frontier Theory Radar

[简体中文](README.zh-CN.md) · [Live site](https://radar.aiutil.com) · [AIUtil](https://aiutil.com)

Frontier Theory Radar is a daily research system for deciding which papers are
worth reading now, tracking as a trend, or retaining as long-term research
material. It records the evidence and reasoning behind each decision instead
of publishing generic summaries.

The public site is generated from the structured records under `docs/data/`.
Research reports are kept in `daily/`, `papers/`, `trends/`, and `insights/`.

## Run and verify

```bash
./run_daily.sh
python3 -m pytest tests
```

The daily publishing job runs in the private AIUtil automation environment.
Credentials and runtime memory are intentionally not stored in this repository.

## License

Apache License 2.0. See [NOTICE](NOTICE).
