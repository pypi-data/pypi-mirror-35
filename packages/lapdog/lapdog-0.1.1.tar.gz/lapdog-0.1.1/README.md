# Lapdog

[![PyPI](https://img.shields.io/pypi/v/lapdog.svg)](https://pypi.io/project/lapdog)

A relaxed wrapper for dalmatian and FISS

## Installing
1. Install lapdog via pip: `pip install lapdog`
  - If you already have lapdog installed, you can upgrade it with
  `pip install --upgrade lapdog`
2. (Optional) Install additional dependencies for the user interface:
  - Install `node` and `npm` if you don't already have them installed
  - Run `lapdog ui --install`. This may take a while

## Usage
1. `lapdog` may be imported within python as a drop-in replacement for `dalmatian`
  - lapdog presents a superset of features available in dalmatian
  - `WorkspaceManager`s in lapdog cache data when communicating with Firecloud.
  If Firecloud experiences an intermittent failure, the `WorkspaceManager` may be
  able to continue running in offline mode. Calling `WorkspaceManager.sync()` will
  reconnect to Firecloud, pushing out any data updates that were queued while in offline mode
  - `WorkspaceManager`s in lapdog present the execution api via `WorkspaceManager.execute()`.
  Executions differ from submissions in that they run directly on Google and results are
  uploaded back to Firecloud afterwards
2. `lapdog` may be used as a command line tool.
  - The tool provides the necessary functions to create a workspace, fill it with data,
  import or upload methods and configurations, and submit jobs (or execute them directly)
  - Run `lapdog --help` to get the list of available commands
3. `lapdog` may be used via an interactive user interface which serves to run and
  monitor lapdog executions
  - Run `lapdog api` to launch the user interface

---

### TODO
1. Rework submission adapter reader
  - On first call: create singleton reader object
  - On all calls:
    - Poll singleton for data and store to buffer
    - Return BytesIO of buffer
2. Improve caching latency
3. Sort out adapter cache hierarchy
4. Add submission-level cost calculation and add to get_submission endpoint
5. Add external cache
    - On startup, create a `~/.caches/lapdog/` folder, if it doesn't exist
    - When a long value is requested (log text, operation status, submission cost, etc)
    check if a cache file exists for it in the folder
    - If it does, return the value
      - If a tag for the file exists, check the timestamp
      - If the tag has expired, delete the file and return not found
    - If not, compute it directly
      - If the value is expected to never change (finished operations, logs of finished submissions, cost of finished submission)
      Store in a file
      - If the value is large (>512kb) tag it
