# Neural Nexus — one-hour event playbook

**Use this file when the Round 2 materials arrive.** Put the organizer's files in this folder, open a new chat in this workspace, and paste the handoff prompt in [Tomorrow: first message](#tomorrow-first-message). This playbook is a decision guide, not a fixed model recipe. Replace its assumptions with the actual rules, data, and evaluator.

## What we know as of 4 October 2026

The organizer describes Round 2, “The Agent Nexus,” as a live challenge in which teams submit an autonomous decision agent, possibly named `agent.py`, plus any required model file and code. A standard environment or script and training data will be supplied. The agent may receive real-time state and return strategic decisions under changing constraints. Teams may compete against one another, with programmatic evaluation. The theme, exact format, and scoring are withheld until the event; the stated coding window is **one hour**. Internet access is expected. AI coding assistants are said to be permitted, **subject to a possible final rule change**. The organizer also says basic Python, preprocessing, training, exporting, and evaluation knowledge should suffice.

These statements leave major unknowns: whether the task is ordinary prediction, sequential control, or a game; whether “accuracy” is the actual metric; the input/output schema; available compute; allowed packages and internet at evaluation time; model-size and latency limits; and whether external pretrained models are legal. **No architecture can be guaranteed to win before those details are known.** Our advantage is to identify the real objective quickly, build a valid baseline, and spend remaining time on measured improvements.

## Local laptop setup verified on 4 October 2026

The BYOD requirement is covered on this Windows laptop. Python 3.13.2 is installed and a project environment lives in `.venv/`. It contains NumPy 2.5.3, pandas 3.0.6, scikit-learn 1.9.1, joblib 1.6.0, and ipykernel 7.4.0. Imports, a small scikit-learn fit/predict run, and joblib save/reload passed. VS Code is installed with its Python and Jupyter extensions. The user has Kaggle and Colab accounts; those cloud sessions were not tested here. TensorFlow, PyTorch, and XGBoost are optional and were not installed because the task is still unknown.

**Use this interpreter locally:** `.venv\Scripts\python.exe` from the Neural Nexus folder. The plain `python` command points to a separate Python 3.14 installation that does not contain these packages. In VS Code, open this folder, choose **Python: Select Interpreter**, and select `.venv\Scripts\python.exe`; choose the same environment as the notebook kernel. A quick check is:

```powershell
& '.\.venv\Scripts\python.exe' -c "import pandas, numpy, sklearn, joblib; print('ML environment ready')"
```

The `.venv/` directory is for this laptop only. Never include it in the judge package or upload it to Kaggle/Colab. Their hosted runtimes need their own package checks in the event notebook. Recheck package availability tomorrow if the organizer requires a different Python version or framework.

## Tomorrow: first message

Copy this into a new chat in this folder, then attach or paste every released file and rule. If the event prohibits AI assistance, follow that rule and use this document yourself.

> We are in Neural Nexus Round 2. Read `NEURAL_NEXUS_EVENT_PLAYBOOK.md` in this workspace. The organizer has now released the attached rules, starter code, data, and evaluator. We have about [remaining minutes] minutes. First inspect every file and state the actual submission interface, metric, constraints, and uncertainty. Then build and run the smallest valid submission. If training is needed, automatically create a complete multi-cell `.ipynb` notebook and give me separate Kaggle and Colab setup and artifact-download steps. Measure the result with the supplied evaluator. Improve only what the evidence supports, test the final packaged artifact through the exact entry point, and prepare the judge handoff using `tools/package_submission.py` after adapting `submission_manifest.json` to the released rules. Give me the exact file(s) to hand to the judges. The released rules override the playbook. Do not assume that accuracy is the metric or that a complex model is best. Here are any organizer announcements or changes: [paste].

Send the **original files**, not screenshots if files are available. Include the deadline/time remaining, platform and hardware, Python version if known, internet/package rules, and any error/output from the official evaluator. Keep each new organizer announcement in the chat; it may change the solution.

Suggested workspace layout after release (create only what is useful):

```text
Neural Nexus/
  NEURAL_NEXUS_EVENT_PLAYBOOK.md
  submission_manifest.json  # provisional packaging template; fill after rules arrive
  tools/package_submission.py
  organizer/          # untouched copies of released files
  work/               # notebooks, experiments, models, and agent source
  handoff/            # generated judge files after manifest is confirmed
  results.md          # measured scores, times, and decisions
```

Do not overwrite the organizer's originals. If their required layout differs, use theirs.

## What to hand the judges

The current announcement says teams submit the agent code, described as `agent.py`, and its model file/code according to a structure the organizers will provide. **It does not yet specify an upload method, archive format, function signature, or exact file list.** For now, expect to hand over the final `agent.py` plus every inference artifact it needs; do not hand over the training dataset or notebook unless the final rules request them. A notebook is for *you* to train and export the model. The judges need a runnable inference package.

After reading tomorrow's instructions, update `submission_manifest.json`: set `rules_confirmed` to `true`, list each required source file and its exact judge-facing name, and set `make_zip` to `true` only if a ZIP is accepted or requested. Run `python tools/package_submission.py`. It copies only listed files to `handoff/judge_submission/`, checks for missing files and unsafe paths, writes a local receipt with names, sizes, and hashes, and optionally creates `handoff/judge_submission.zip`. The receipt stays in `handoff/`; it is **not** part of the judge package unless their rules explicitly request it. Do not upload both folder and ZIP blindly: use the format in the final rules.

Before handing anything over, run the organizer's evaluator against the **copied files in `handoff/judge_submission/`**, ideally from a fresh process. Check that the agent can load its model, returns the required type and legal values, and meets time limits. Then tell the user, plainly: exact path(s) to upload, whether to upload individual files or ZIP, the observed local score/test result, and any unverified constraint. If the organizer requires a direct notebook, single script, model-only file, or special portal submission, change the manifest and handoff instructions to match. The script is a helper, never a substitute for the official rules.

## The one-hour run order

| Clock | Action | Exit condition |
|---|---|---|
| 0–5 min | Read rules, starter interface, sample input/output, evaluator, metric, limits, and submission path. Inventory data and environment. | Can explain exactly what one valid prediction/action looks like. |
| 5–12 min | Build a minimal valid `agent.py` or requested entry point. Run the official sample or evaluator end to end. | A complete submission runs without schema or import errors. |
| 12–25 min | Inspect data and make one honest validation split. Train a fast baseline or code a simple policy. | Baseline score and runtime recorded. |
| 25–45 min | Target the main error source. Try a small number of justified candidates, retaining the best measured version. | Best candidate beats baseline on a trustworthy test or has a clear strategic reason. |
| 45–55 min | Rehearse the final environment: fresh process, exact file paths, allowed dependencies, time/memory, output format, and repeated calls. | Final artifact passes the official entry point. |
| 55–60 min | Freeze, package, upload, and verify receipt/result if the platform allows. | Required files are submitted before deadline. |

If the time remaining is shorter, preserve the ordering: **valid submission → honest measurement → improvement → final rehearsal**. Stop tuning early enough to submit. Record a working fallback each time an experiment starts.

## First five minutes: contract before model

Read the official materials and write these answers in `results.md`:

1. **Task type:** classification, regression, ranking, forecasting, computer vision, text, multimodal, optimization, or interactive/game agent? Can the agent learn during a match, or must it be fixed?
2. **Exact entry point:** required filename, callable/class signature, command, argument types, return type, serialization format, working directory, and whether the process stays alive across decisions.
3. **Metric:** accuracy, F1, log loss, reward, win rate, regret, time, or a weighted score? Are invalid actions penalized? Is performance averaged over multiple seeds/opponents?
4. **Limits:** wall time, per-action latency, memory, CPU/GPU, storage, allowed libraries, network access during training versus evaluation, model size, and any forbidden external data/models.
5. **Data:** file types, rows, labels, missing values, leakage candidates, time/entity/group structure, class balance, train/test differences, and whether hidden test examples are independent.
6. **Evaluator:** how to run locally; whether it includes public cases only; whether it can simulate full episodes and multiple seeds.

Treat the starter code and tests as executable specifications, but reconcile them with written rules. Ask the organizer when those disagree. Never train on hidden evaluation labels or exploit access outside the provided rules.

## Pick the solution path from the actual task

### A. Ordinary tabular prediction

Start with a constant/majority baseline and a fast strong model. For numeric/categorical tables, try CatBoost if installed and permitted; otherwise HistGradientBoosting, ExtraTrees/RandomForest, or a regularized linear model through a preprocessing pipeline. Choose based on data size, feature types, training time, and observed score. For small data, regularization and validation design usually matter more than a deeper model. For high-cardinality IDs, check whether they encode legitimate information or cause leakage.

Match the objective to the metric. Stratify classification splits when appropriate. For grouped records, split by group. For time-dependent data, validate on later time. Tune the decision threshold only on validation data, and only for threshold-sensitive metrics such as F1. If the score is probability based, retain calibrated probabilities and inspect log loss. Do not report training accuracy as generalization.

### B. Text, images, audio, or mixed data

Check what pretrained assets, packages, hardware, and network use are actually allowed. Fast text baselines include TF-IDF with a linear classifier; embedding models can follow if time and runtime permit. For images, a permitted pretrained feature extractor plus a lightweight classifier can be faster than training a network; simple image features or a small CNN may be the fallback. For multimodal data, establish one model per modality and combine only if validation proves a gain. Cache expensive features during training if the submission rules permit including the cache/model.

### C. Sequential decisions or competitive agent

Inspect the state schema, legal-action list, transition rules, reward, termination, and whether hidden information exists. First build a legal, deterministic policy that never crashes. Simulate full episodes across several seeds and, where possible, several opponents. Evaluate **mean reward/win rate, invalid moves, worst-case failures, and per-action latency**, not just one lucky run.

Use the simplest strategy supported by the environment: rules/heuristics, one-step expected-value scoring, lookahead/search under a strict time budget, or a learned value/policy model trained from supplied data. If the opponent adapts, test against varied opponents. Keep a legal fallback action and guard against missing fields or new states. A learned model is useful only when it improves decisions after accounting for runtime and distribution shift.

### D. Forecasting, ranking, or optimization

Forecast with chronological validation and leakage-safe lag features. Rank with query/group-aware evaluation. For constrained optimization, make feasibility and valid output a hard requirement before optimizing score; compare greedy, local search, or exact solvers when allowed. Use the organizer's objective formula rather than a convenient proxy.

## How to decide whether a hybrid or ensemble helps

A distinctive solution should come from the task structure. Candidate ideas include combining a learned score with rule-based feasibility checks, a fast baseline plus a specialized model for rare cases, model predictions feeding a bounded search, or two diverse predictors blended by validation performance. Try an ensemble only after individual models work. Measure its **incremental score and latency** on the same split or seeds. Correlated models often add complexity without gain. Prefer the simpler model when the difference is within validation noise or threatens the deadline.

Use small, targeted experiments. Maintain a table: candidate, change, split/seeds, score, runtime, and decision. Never choose a model from a single public leaderboard result alone; it may overfit the visible cases. If the supplied evaluator exposes only a tiny sample, use it for interface checks and make a separate local validation set.

## Cloud training notebook: automatic handoff

**Trigger:** When the revealed solution needs model training and Kaggle or Colab is useful, create a runnable `.ipynb` file in this workspace without waiting for a separate notebook request. Give the user a direct file link. If training is unnecessary or the rules forbid cloud compute, explain why and deliver the required agent code instead. The notebook must be built for the actual released problem; do not prepare a speculative training notebook tonight.

Write the notebook as a sequence of short, numbered Markdown and code cells so the user can run it from top to bottom with **Run all**. Include, as applicable:

1. A first-cell summary of the task, expected input files, platform setting, outputs, estimated resource needs, and the exact official metric. Mark unknown estimates as estimates.
2. One configuration cell for paths, seed, target/ID columns or state fields, runtime budget, and permitted options. Avoid scattered manual edits.
3. A minimal dependency cell with pinned versions only when needed and allowed. Check installed packages first; do not install heavy packages by habit.
4. Platform-specific data discovery/mount or upload cells that detect Kaggle (`/kaggle/input`) and Colab (`/content` or Drive) and show what files were found. Fail with a clear message if required data is absent.
5. Data/schema inspection and contract checks, followed by preprocessing that prevents leakage and handles missing/unseen values.
6. A baseline, a suitable validation split or simulator, the exact metric, and a printed result. Add improved candidates only when the time budget supports them.
7. Final fitting and export of the model plus any preprocessing, label map, configuration, and metadata needed by inference. Write them into a clearly named output directory.
8. A local inference smoke test that loads the **saved** artifact in a fresh object/process when feasible and checks the expected input/output schema, legal values, latency, and sample evaluator call.
9. A final manifest listing exact files to download and submit, their sizes, and where Kaggle/Colab stored them. Zip artifacts if that makes transfer safer and the rules permit it.

Keep the training notebook separate from the production `agent.py` unless the organizer explicitly requests a notebook submission. The agent must load the exported artifact without access to notebook variables, training data, or cloud-only paths. If the evaluator runs offline, the agent must run offline. Do not put secrets, API tokens, or private Drive paths into the notebook. Save checkpoints when training could exceed the session or contest deadline.

**For every notebook handoff, give both setup routes in the answer:**

- **Kaggle:** create a new Notebook; upload the `.ipynb` if the interface supports it or import it as a notebook; add the released dataset/files as Notebook input; select CPU/GPU based on the selected model and current availability; set internet only if allowed and required; verify the data path in the configuration cell; run cells top to bottom; download the exported files from the notebook output area.
- **Colab:** upload/open the `.ipynb` in Colab; select CPU/GPU according to the model; upload the organizer files to the runtime or mount Drive only if useful; set the configuration path; run cells top to bottom; download the exported artifact bundle from `/content` or the specified Drive output folder.

Tomorrow, replace these general UI steps with the **actual notebook filename, paths, file names, runtime choice, expected outputs, and transfer steps**. If Kaggle and Colab differ in package availability or filesystem layout, make the notebook detect the platform or provide clearly labeled platform cells. Test notebook structure and syntax locally where possible; do not claim a cloud run succeeded unless it actually did. If the user runs it and sends an error or score, diagnose that result and update the same notebook promptly.

## Submission engineering

- Make inference independent of the training script. Save only approved artifacts and load them with paths relative to the submission file or a documented working directory.
- Match the exact output schema, data types, label names, action IDs, and legal constraints. Handle empty, missing, unseen, or malformed values according to the contract.
- Keep imports and model loading within time/memory limits. Avoid downloads, network calls, and nondeterministic external services at evaluation time unless explicitly allowed and guaranteed.
- Set seeds for reproducible training. Keep preprocessing identical at training and inference; a single saved pipeline is useful for standard supervised tasks.
- Run a clean-process test with the exact submitted files and command. If interactive, test repeated calls, multiple complete episodes, and timeout behavior.
- Preserve the last working artifact before replacing it. When an experiment fails or time runs low, submit the proven fallback.

## If the event changes the rules

At each announcement, pause implementation briefly and update the contract: what changed, which files or code are affected, and whether the current artifact is still valid. Run the official smoke test again. A changed metric may require different thresholding or a different objective; a changed schema may require adapter code; new time limits may rule out a heavy model; a ban on AI assistants means stop using them. Do not discard a working solution until the replacement passes the revised interface.

If files arrive late, begin with rule/interface inspection and a valid placeholder. If training data is missing, create a rules-based or constant baseline and ask the organizer for the promised files. If the evaluator is unavailable, use documented examples and local validation, then mark scores as unverified. If packages cannot be installed, use the available standard library or installed tools. If the task is entirely different from these categories, derive the input/output contract and metric first, then make a valid baseline before specializing.

## Final five-minute checklist

- [ ] Current rules permit the tools, data, models, and packages used.
- [ ] Exact required filename(s) and callable/command are present.
- [ ] Fresh process loads the artifact using only submitted files.
- [ ] Sample inputs and edge cases return valid outputs within limits.
- [ ] Best measured version is selected; fallback is available.
- [ ] Upload completed and receipt or platform status checked where possible.

**Reminder:** the organizers' description is broad and may change. Follow the released problem statement and evaluator tomorrow. The goal is the best *measured valid submission within the hour*, not complexity for its own sake.
