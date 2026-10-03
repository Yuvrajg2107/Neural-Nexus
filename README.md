# Neural Nexus

Preparation workspace for Round 2 of the Neural Nexus competition. The event task, dataset, scoring, and submission format have not been released yet. The current files provide a one-hour work plan and a configurable way to package a judge submission once the official rules arrive.

## Start on event day

1. Save the organizer's files locally in `organizer/` without changing the originals. That directory is ignored by Git until sharing the files is confirmed to be allowed.
2. Open this folder in Codex and follow the handoff prompt in [NEURAL_NEXUS_EVENT_PLAYBOOK.md](NEURAL_NEXUS_EVENT_PLAYBOOK.md).
3. Build and test the agent against the organizer's interface and evaluator. If training is useful, create a task-specific notebook for Kaggle or Colab and export the trained artifact.
4. Update [submission_manifest.json](submission_manifest.json) with the exact files and names required by the judges. Set `rules_confirmed` to `true` only after checking the released rules.
5. Run `python tools/package_submission.py`, test the copied files, then upload the format the judges request.

The packaging script intentionally refuses the provisional manifest. There is no trained model or event-specific agent in this repository yet.

## Local environment

The laptop has a project environment at `.venv/` with Python 3.13, pandas, NumPy, scikit-learn, joblib, and a Jupyter kernel. In VS Code, select `.venv\Scripts\python.exe` as the interpreter. The environment is ignored by Git and should not be submitted to judges. Kaggle and Colab need their own runtime setup, which the eventual training notebook will document.

## Files

| Path | Purpose |
|---|---|
| `NEURAL_NEXUS_EVENT_PLAYBOOK.md` | Event-day decisions, timing, notebook requirements, and judge handoff |
| `submission_manifest.json` | Provisional list of judge-facing files |
| `tools/package_submission.py` | Copies approved files into `handoff/` and optionally makes a ZIP |

The official competition rules take priority over this preparation material.

## License

This repository's original code and documentation are available under the [MIT License](LICENSE). Organizer-provided files, datasets, and third-party model weights are not covered by that license.
