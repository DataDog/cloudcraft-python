# Cloudcraft-Python Development Playgrounds


## Orientation

Examples of Cloudcraft API Client to demonstrate usage.

Code should work when configured to run against production
with source or using built package...
```
[use non-localhost config (default)]
cloudcraft = Cloudcraft()
```


## Development Notes

### Running Playground (Examples)

```
% cd {repo-directory}
% poetry env use python3.10
% poetry shell
% poetry install
% export CLOUDCRAFT_API_KEY={{ api-key }}
% export CLOUDCRAFT_TEST_ROLE={{ your-test-role-arn }}
% python3 dev_playgrounds/accounts.py
% python3 dev_playgrounds/blueprints.py
% python3 dev_playgrounds/budgets.py
% python3 dev_playgrounds/exports.py
% python3 dev_playgrounds/snapshots.py
% python3 dev_playgrounds/users.py
```
